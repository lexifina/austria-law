"""Deterministic offline RIS normalization and independent preservation checks."""

from __future__ import annotations
from collections import Counter
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import re
from html import escape
from lxml import html
from markdown_it import MarkdownIt

MD = MarkdownIt("commonmark", {"html": True}).enable("table")
BLOCK_TAGS = {"div", "p", "h4", "h5", "ol", "ul", "li", "table", "dl", "dt", "dd"}
KNOWN_TAGS = BLOCK_TAGS | {
    "h2",
    "h3",
    "span",
    "a",
    "br",
    "img",
    "tbody",
    "tr",
    "td",
    "th",
    "thead",
    "tfoot",
    "gs",
    "binary",
    "src",
    "haushaltsleitendes",
    "bezeichnung",
    "lieferant",
    "datum",
    "fortlaufende",
    "regelreservetyp",
}
EXTENSION_TAGS = {
    "gs",
    "binary",
    "src",
    "haushaltsleitendes",
    "bezeichnung",
    "lieferant",
    "datum",
    "fortlaufende",
    "regelreservetyp",
}
KNOWN_SECTIONS = {
    "Text",
    "Langtitel",
    "Präambel/Promulgationsklausel",
    "Ratifikationstext",
    "Sonstige Textteile",
    "Beachte für folgende Bestimmung",
    "Beachte zur ganzen Rechtsvorschrift",
    "Umsetzungshinweis für folgende Bestimmung",
    "Vertragsparteien",
    "Änderung",
    "Begleitende Dokumente",
}


def clean(text):
    return re.sub(r"\s+", " ", text.replace("\u00ad", "")).strip()


def checksum(data):
    return hashlib.sha256(
        data if isinstance(data, bytes) else data.encode()
    ).hexdigest()


def visible(node):
    copy = deepcopy(node)
    for hidden in list(
        copy.xpath(
            './/*[contains(concat(" ",normalize-space(@class)," ")," sr-only ")]'
        )
    ):
        hidden.drop_tree()
    return copy


def plain(node):
    """Independent text extraction: no formatting or Markdown generation."""
    result = []

    def walk(n):
        if not isinstance(n.tag, str):
            return
        if n.tag in {
            "br",
            "p",
            "div",
            "h2",
            "h3",
            "h4",
            "h5",
            "li",
            "td",
            "tr",
            "dt",
            "dd",
        }:
            result.append(" ")
        result.append(n.text or "")
        for c in n:
            walk(c)
            result.append(c.tail or "")
        if n.tag in {
            "br",
            "p",
            "div",
            "h2",
            "h3",
            "h4",
            "h5",
            "li",
            "td",
            "tr",
            "dt",
            "dd",
        }:
            result.append(" ")

    walk(node)
    return clean("".join(result))


def escaped(text):
    text = re.sub(r"([\\`*_\[\]<>|])", r"\\\1", text)
    text = re.sub(r"^(\d+)([.)])(?=\s|$)", r"\1\\\2", text)
    if re.match(r"^[#>+-]\s", text):
        text = "\\" + text
    return text


def inline(node):
    if node.tag == "img":
        return " \ufff0" + node.get("src", "") + "\ufff1 "
    bits = [node.text or ""]
    for c in node:
        if not isinstance(c.tag, str):
            continue
        cls = c.get("class", "").split()
        if c.tag == "br":
            bits.append(" ")
        elif c.tag == "img":
            # Keep image-only legal content visible as an explicit source reference.
            bits.append(" \ufff0" + c.get("src", "") + "\ufff1 ")
        else:
            separated = c.tag in {"p", "div", "h4", "h5", "li", "tr", "td", "dt", "dd"}
            if separated:
                bits.append(" ")
            val = inline(c)
            bits.append(val)
            if separated:
                bits.append(" ")
            if "Absatzzahl" in cls:
                bits.append(" ")
        bits.append(c.tail or "")
    result = "".join(bits)
    if "Hoch" in node.get("class", "").split():
        result = "<sup>" + result + "</sup>"
    if "Tief" in node.get("class", "").split():
        result = "<sub>" + result + "</sub>"
    if "Absatzzahl" in node.get("class", "").split():
        result += " "
    # Some RIS responses contain nested anchors. Markdown cannot represent nested links;
    # keep the innermost link here and expose other source URLs in the reference section.
    if node.tag == "a" and node.get("href") and not node.xpath(".//a[@href]"):
        result = (
            "\ufff2" + node.get("href").encode().hex() + "\ufff3" + result + "\ufff4"
        )
    return result


def inline_md(node):
    # Escape source punctuation, allowing only our explicit semantic super/subscript tags.
    return format_inline(inline(node))


def link_destination(url):
    return escape(url.replace(">", "%3E"), quote=False)


def format_inline(text):
    text = clean(text)
    tokens = re.split(
        r"(</?(?:sup|sub)>|\ufff0.*?\ufff1|\ufff2[0-9a-f]*\ufff3|\ufff4)", text
    )
    out = []
    urls = []
    for t in tokens:
        if t.startswith("\ufff0"):
            out.append("[Source image](<" + link_destination(t[1:-1]) + ">)")
        elif t.startswith("\ufff2"):
            urls.append(bytes.fromhex(t[1:-1]).decode())
            out.append("[")
        elif t == "\ufff4":
            out.append("](<" + link_destination(urls.pop()) + ">)")
        elif re.fullmatch(r"</?(?:sup|sub)>", t):
            out.append(t)
        else:
            out.append(escaped(t))
    return "".join(out)


def paragraph(text):
    return {"kind": "paragraph", "markdown": clean(text)}


def is_symbol(node):
    return any(
        c.startswith(("GldSymbol", "SymE")) for c in node.get("class", "").split()
    )


def render_table(node):
    rows = []
    for tr in node.xpath("./tr|./tbody/tr|./thead/tr|./tfoot/tr"):
        if (
            tr.get("height") == "0"
            and not plain(tr)
            and not tr.xpath(".//img|.//a[@href]|.//binary")
        ):
            continue
        cells = [c for c in tr if c.tag in {"td", "th"}]
        rows.append(
            [
                {
                    "text": plain(c),
                    "rowspan": int(c.get("rowspan") or "1"),
                    "colspan": int(c.get("colspan") or "1"),
                    "element": c,
                }
                for c in cells
            ]
        )
    rich = any(c["rowspan"] != 1 or c["colspan"] != 1 for row in rows for c in row)
    nested = bool(node.xpath(".//table|.//ol|.//ul"))
    uniform = len({len(r) for r in rows}) <= 1
    if not rows:
        return {"kind": "table", "markdown": "", "rows": []}
    if not rich and not nested and uniform:
        out = []
        for i, row in enumerate(rows):
            out.append("| " + " | ".join(inline_md(c["element"]) for c in row) + " |")
            if i == 0:
                out.append("| " + " | ".join("---" for c in row) + " |")
        rendered = "\n".join(out)
    else:
        # Merged-cell semantics need actual spans. Keep only table/row/cell markup, never RIS classes/styles.
        out = ["<table>"]
        for row in rows:
            out.append("  <tr>")
            for cell in row:
                attrs = "".join(
                    f' {k}="{cell[k]}"' for k in ["rowspan", "colspan"] if cell[k] != 1
                )
                content = MD.render(markdown(blocks(cell["element"]))).strip()
                out.append(f"    <td{attrs}>{content}</td>")
            out.append("  </tr>")
        out.append("</table>")
        rendered = "\n".join(out)
    grid = [
        [{k: v for k, v in c.items() if k != "element"} for c in row] for row in rows
    ]
    return {"kind": "table", "markdown": rendered, "cells": grid, "merged_cells": rich}


def blocks(node):
    tag = node.tag
    if not isinstance(tag, str):
        return []
    if tag == "table":
        return [render_table(node)]
    if tag in {"h4", "h5"}:
        if is_symbol(node):
            return [paragraph(inline_md(node))]
        out = []
        buffer = node.text or ""

        def add():
            nonlocal buffer
            if clean(buffer):
                out.append(
                    {
                        "kind": "heading",
                        "level": 3 if "UeberschrPara" in node.get("class", "") else 2,
                        "markdown": format_inline(buffer),
                    }
                )
            buffer = ""

        for c in node:
            if c.tag == "br":
                add()
            elif "display:block" in c.get("style", "").replace(" ", ""):
                add()
                buffer = inline(c)
                add()
            else:
                buffer += inline(c)
            buffer += c.tail or ""
        add()
        return out
    if tag in {"ol", "ul"}:
        result = []
        for li in node:
            if li.tag != "li":
                continue
            items = container(li)
            if "wai-absatz-list" not in node.get("class", "").split():
                items = [{"kind": "list_item", "children": items}]
            result.extend(items)
        return result
    if tag in {"p", "dt"}:
        return [paragraph(inline_md(node))] if clean(inline(node)) else []
    if tag == "img":
        return []
    return container(node)


def container(node):
    result = []
    buffer = node.text or ""
    symbol = ""

    def flush():
        nonlocal buffer
        if clean(buffer):
            result.append(paragraph(format_inline(buffer)))
        buffer = ""

    for c in node:
        if not isinstance(c.tag, str):
            continue
        # RIS renders paragraph/list symbols in floated sibling wrappers. Attach them to the first text paragraph.
        symbol_wrapper = is_symbol(c) or (
            c.tag == "div" and any(is_symbol(x) for x in c.iter() if x is not c)
        )
        if symbol_wrapper and not c.xpath(".//ol|.//p"):
            flush()
            symbol += (" " if symbol else "") + inline_md(c)
        elif c.tag in BLOCK_TAGS:
            flush()
            items = blocks(c)
            if symbol and items:

                def attach(items):
                    for item in items:
                        if item["kind"] == "paragraph":
                            item["markdown"] = symbol + " " + item["markdown"]
                            return True
                        if item["kind"] == "list_item" and attach(item["children"]):
                            return True
                    return False

                if attach(items):
                    symbol = ""
            result.extend(items)
        elif c.tag == "img":
            buffer += " \ufff0" + c.get("src", "") + "\ufff1 "
        elif c.tag == "br":
            buffer += " "
        else:
            buffer += inline(c)
        buffer += c.tail or ""
    flush()
    if symbol:
        if result and result[0]["kind"] == "paragraph":
            result[0]["markdown"] = symbol + " " + result[0]["markdown"]
        else:
            result.insert(0, paragraph(symbol))
    return result


def markdown(nodes, indent=0):
    out = []
    for n in nodes:
        kind = n["kind"]
        value = n.get("markdown", "")
        if kind == "list_item":
            value = markdown(n["children"]).strip()
            lines = value.splitlines()
            if lines:
                lines[0] = re.sub(r"^(\d+)\.(?=\s|$)", r"\1\\.", lines[0])
            if lines:
                out.append(
                    "- "
                    + lines[0]
                    + "\n"
                    + "\n".join("  " + line if line else "" for line in lines[1:])
                )
        elif kind == "heading":
            out.append("#" * n["level"] + " " + value)
        elif value:
            if kind == "paragraph":
                value = re.sub(r"^(\d+)([.)])(?=\s|$)", r"\1\\\2", value)
                if re.match(r"^(?:[-+>](?:\s|$)|(?:[-_*]\s*){3,}$|#+(?:\s|$))", value):
                    value = "\\" + value
            out.append(value)
    return "\n\n".join(v.rstrip() for v in out if v.strip()) + "\n"


def file_of(label):
    import build

    return build.file_of(label)


def context(block):
    texts = [plain(n) for n in block.xpath('.//h4|.//p[contains(@class,"ErlText")]')]
    for text in texts:
        if "Anm.: aus" in text:
            match = re.search(
                r"(BGBl\.|RGBl\.|StGBl\.|JGS)\s*(I{1,3})?\s*(?:Nr\.\s*)?(\d+)\s*/\s*(\d{4})",
                text,
            )
            if match:
                org, part, num, year = match.groups()
                return match.group(0), "-".join(
                    x
                    for x in [
                        org.rstrip(".").lower(),
                        part.lower() if part else "",
                        year,
                        num,
                    ]
                    if x
                )
    return None, None


def source_heading(block):
    heads = block.xpath(".//h4")
    if heads:
        return plain(heads[0])
    sections = block.xpath('./div[h3[normalize-space(.)="Text"]]')
    if sections:
        text = plain(sections[0])
        match = re.match(
            r"^Text\s+((?:Artikel|Art\.)\s+\d+(?:bis|ter|quater|quinquies|sexies|septies|octies|nonies|decies)?\.?|§\s*\d+[a-z]*\.?)",
            text,
            re.I,
        )
        if match:
            return match[1]
    return None


def slug(text):
    text = (
        text.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    )
    text = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return (
        text if len(text) <= 70 else text[:55].rstrip("-") + "-" + checksum(text)[:12]
    )


def planned_files(source_blocks, labels):
    names = []
    info = []
    for original in source_blocks:
        b = visible(original)
        label = clean("".join(b.xpath("./h2")[0].itertext()))
        citation, key = context(b)
        name = file_of(label)
        heading = source_heading(b)
        if labels[label] > 1:
            # RIS may index Article 4bis/4ter under the same "Art. 4" search designation.
            match = re.search(
                r"^Artikel\s+(\d+)(bis|ter|quater|quinquies|sexies|septies|octies|nonies|decies)\b",
                heading or "",
                re.I,
            )
            indexed = re.fullmatch(r"Art\.\s*(\d+)", label)
            if match and indexed and match[1] == indexed[1]:
                name = f"art-{int(match[1]):03d}{match[2].lower()}.md"
            if key:
                name = name[:-3] + "--" + key + ".md"
        names.append(name)
        info.append((b, heading, citation))
    groups = {
        name: [i for i, n in enumerate(names) if n == name]
        for name, count in Counter(names).items()
        if count > 1
    }
    for name, indices in groups.items():
        qualifiers = []
        for i in indices:
            b, heading, _ = info[i]
            headings = [
                plain(n) for n in b.xpath(".//h4") if not plain(n).startswith("(Anm.:")
            ]
            descriptive = [
                h
                for h in headings
                if not re.fullmatch(r"(?:Artikel|Art\.)\s*[0-9IVXLCDM]+\.?", h)
            ]
            notes = [
                plain(n)
                for n in b.xpath('.//h4|.//p[contains(@class,"ErlText")]')
                if plain(n).startswith("(Anm.:")
            ]
            qualifier = slug(descriptive[0]) if descriptive else ""
            if not qualifier and notes:
                qualifier = "scope-" + checksum(" ".join(notes))[:12]
            if not qualifier and heading:
                qualifier = slug(heading)
            qualifiers.append(qualifier)
        counts = Counter(qualifiers)
        for i, q in zip(indices, qualifiers):
            if q and counts[q] == 1:
                names[i] = name[:-3] + "--" + q + ".md"
    return names


def source_fingerprint(block):
    evidence = {
        "text": plain(block),
        "links": [a.get("href") for a in block.xpath(".//a[@href]")],
        "images": [a.get("src") for a in block.xpath(".//img")],
        "tables": [
            [
                [int(c.get("rowspan") or 1), int(c.get("colspan") or 1)]
                for c in table.xpath("./tr/td|./tr/th|./tbody/tr/td|./tbody/tr/th")
            ]
            for table in block.xpath(".//table")
        ],
    }
    return checksum(json.dumps(evidence, sort_keys=True, ensure_ascii=False))


def table_signatures(root):
    signatures = []
    for table in root.xpath(".//table"):
        rows = []
        for tr in table.xpath("./tr|./tbody/tr|./thead/tr|./tfoot/tr"):
            if (
                tr.get("height") == "0"
                and not plain(tr)
                and not tr.xpath(".//img|.//a[@href]|.//binary")
            ):
                continue
            rows.append(
                [
                    (
                        int(c.get("rowspan") or 1),
                        int(c.get("colspan") or 1),
                        re.sub(r"\s+", "", plain(c)),
                    )
                    for c in tr
                    if c.tag in {"td", "th"}
                ]
            )
        if not rows:
            continue
        signatures.append(rows)
    return signatures


def convert(row, root, output=None, *, date, selected=None, resolutions=None):
    warnings = []
    source = (root / row["file"]).read_bytes()
    doc = html.fromstring(source.decode("utf-8-sig"))
    if checksum(source) != row["sha256"]:
        raise ValueError("snapshot hash mismatch")
    all_blocks = doc.xpath('//div[@class="documentContent"]')
    labels = Counter(row["provisions"])
    if len(all_blocks) != len(row["provisions"]):
        raise ValueError("source entry count mismatch")
    if [clean("".join(b.xpath("./h2")[0].itertext())) for b in all_blocks] != row[
        "provisions"
    ]:
        raise ValueError("source designations mismatch")
    names = planned_files(all_blocks, labels)
    pending_names = Counter(names)
    fingerprints = [source_fingerprint(visible(b)) for b in all_blocks]
    fingerprint_counts = Counter(fingerprints)
    seen_fingerprints = Counter()
    records = []
    written = set()
    checks = []
    directory = output / row["nr"] if output else None
    for position, original in enumerate(all_blocks):
        label = clean("".join(original.xpath("./h2")[0].itertext()))
        if selected and label not in selected:
            continue
        block = visible(original)
        citation, key = context(block)
        for tag in sorted(
            {n.tag for n in block.iter() if isinstance(n.tag, str)} - KNOWN_TAGS
        ):
            warnings.append("unreviewed_source_tag:" + tag)
        filename = names[position]
        identity_review = pending_names[filename] > 1
        source_key = fingerprints[position]
        seen_fingerprints[source_key] += 1
        resolution = (resolutions or {}).get(
            row["nr"] + ":" + source_key + ":" + str(seen_fingerprints[source_key])
        )
        if (
            resolution
            and resolution.get("expected_occurrences") != fingerprint_counts[source_key]
        ):
            identity_review = True
            resolution = None
        if resolution:
            filename = resolution["file"]
            identity_review = False
        if (
            Path(filename).is_absolute()
            or ".." in Path(filename).parts
            or not filename.endswith(".md")
        ):
            raise ValueError("unsafe resolved provision path")
        base = filename
        if filename in written:
            count = 2
            while filename in written:
                filename = base[:-3] + f"--entry-{count}.md"
                count += 1
            identity_review = True
            warnings.append(f"ambiguous_identity:{row['nr']}:{label}")
        written.add(filename)
        metadata = []
        body = []
        sources = []
        for section in block:
            if section.tag != "div":
                continue
            heads = section.xpath("./h3")
            if not heads:
                raise ValueError("unheaded RIS section")
            name = clean("".join(heads[0].itertext()))
            if name not in KNOWN_SECTIONS:
                warnings.append("unreviewed_source_section:" + name)
            content = deepcopy(section)
            for head in list(content.xpath("./h3")):
                head.drop_tree()
            if name in {
                "Text",
                "Präambel/Promulgationsklausel",
                "Ratifikationstext",
                "Sonstige Textteile",
            }:
                body.extend(blocks(content))
                sources.append(content)
            elif name == "Langtitel":
                # The source title belongs in metadata; a concise act index will display it.
                metadata.append({"kind": name, "text": plain(content)})
                body.extend(blocks(content))
                sources.append(content)
            elif name == "Begleitende Dokumente":
                metadata.append(
                    {
                        "kind": name,
                        "text": plain(content),
                        "attachments": [
                            {
                                "url": a.get("href"),
                                "title": clean(
                                    a.get("title")
                                    or "".join(a.itertext())
                                    or "Source attachment"
                                ),
                                "status": "linked_only",
                            }
                            for a in content.xpath(".//a[@href]")
                        ],
                    }
                )
            else:
                metadata.append({"kind": name, "text": plain(content)})
        text = markdown(body)
        if not text.strip():
            if label == "§ 0":
                text = ""
            elif any(x.get("attachments") for x in metadata):
                pass
            else:
                warnings.append(f"empty_legal_text:{row['nr']}:{label}")
        # Compare visible source characters against independently rendered Markdown. Ignore whitespace only.
        baseline = "".join(plain(x) for x in sources)
        rendered = html.fragment_fromstring("<div>" + MD.render(text) + "</div>")
        expected_images = Counter(
            n.get("src") for source in sources for n in source.xpath(".//img")
        )
        actual_images = Counter(
            n.get("href")
            for n in rendered.xpath('.//a[normalize-space(.)="Source image"]')
        )
        media_ok = expected_images == actual_images
        expected_links = Counter(
            MD.normalizeLink(a.get("href"))
            for source in sources
            for a in source.xpath(".//a[@href]")
        )
        rendered_links = Counter(
            MD.normalizeLink(a.get("href"))
            for a in rendered.xpath(".//a[@href]")
            if a.get("href") not in expected_images
        )
        extra_links = expected_links - rendered_links
        link_ok = not (rendered_links - expected_links)
        units_ok = all(
            sum(
                bool(plain(n))
                for source in sources
                for n in source.xpath(
                    './/span[contains(concat(" ",normalize-space(@class)," ")," '
                    + cls
                    + ' ")]'
                )
            )
            == sum(bool(plain(n)) for n in rendered.xpath(".//" + tag))
            for cls, tag in [("Hoch", "sup"), ("Tief", "sub")]
        )
        for generated in list(
            rendered.xpath('.//a[normalize-space(.)="Source image"]')
        ):
            if generated.get("href") in {n.get("src") for n in block.xpath(".//img")}:
                generated.drop_tree()
        actual = plain(rendered)
        table_ok = [
            sig for source in sources for sig in table_signatures(source)
        ] == table_signatures(rendered)
        norm = lambda x: re.sub(r"\s+", "", x.replace("\u00ad", ""))
        ok = norm(baseline) == norm(actual) if baseline else True
        issue = None
        if not ok:
            a, b = norm(baseline), norm(actual)
            prefix = next(
                (i for i, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b))
            )
            issue = {
                "nr": row["nr"],
                "designation": label,
                "source": a[max(0, prefix - 60) : prefix + 180],
                "converted": b[max(0, prefix - 60) : prefix + 180],
            }
        attachments = [
            a for section in metadata for a in section.get("attachments", [])
        ]
        if extra_links:
            text = (
                text.rstrip()
                + "\n\n## Weitere Quellenverweise\n\n"
                + "\n".join(
                    "- [Source reference](<" + link_destination(url) + ">)"
                    for url, count in extra_links.items()
                    for _ in range(count)
                )
                + "\n"
            )
        final_links = Counter(
            MD.normalizeLink(a.get("href"))
            for a in html.fragment_fromstring(
                "<div>" + MD.render(text) + "</div>"
            ).xpath(".//a[@href]")
            if a.get("href") not in expected_images
        )
        link_ok = link_ok and final_links == expected_links
        if attachments:
            text = (
                text.rstrip()
                + "\n\n## Begleitende Dokumente\n\n"
                + "\n".join(
                    "- ["
                    + escaped(a["title"])
                    + "](<"
                    + link_destination(a["url"])
                    + ">)"
                    for a in attachments
                )
                + "\n"
            )
        links = [
            {"text": clean("".join(a.itertext())), "url": a.get("href")}
            for a in block.xpath(".//a[@href]")
        ]
        images = [
            {
                "url": n.get("src"),
                "alt": n.get("alt")
                if not (n.get("alt") or "").startswith("|")
                else None,
                "status": "linked_only",
            }
            for n in block.xpath(".//img")
            if "Icon" not in n.get("class", "").split()
        ]
        checks.append(
            {
                "designation": label,
                "source_position": position,
                "characters_preserved": ok,
                "image_references_preserved": media_ok,
                "superscript_subscript_preserved": units_ok,
                "links_preserved": link_ok,
                "table_structure_preserved": table_ok,
                **({"issue": issue} if not ok else {}),
            }
        )
        entry = {
            "designation": label,
            "source_heading": source_heading(block),
            "source_record_id": None,
            "source_locator": {
                "kind": "documentContent_index",
                "index": position,
                "stable_identity": False,
            },
            "file": filename,
            "source_context": citation,
            "identity_review_required": identity_review,
            "identity_basis": "reviewed_local_key"
            if resolution
            else "source_designation_and_context",
            "source_fingerprint": source_key,
            "sha256": checksum(text),
            "notes": metadata,
            "links": links,
            "images": images,
            "source_extensions": [
                {"tag": n.tag, "attributes": dict(n.attrib), "text": plain(n)}
                for n in block.iter()
                if n.tag in EXTENSION_TAGS
            ],
            "tables": [
                {"cells": n["cells"], "merged_cells": n["merged_cells"]}
                for n in flatten(body)
                if n["kind"] == "table"
            ],
        }
        records.append(entry)
        if output:
            target = directory / filename
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text)
    metadata = {
        "sample_only": selected is not None,
        "included_provisions": len(records),
        "source_provision_count": len(all_blocks),
        "schema_version": 1,
        "gesetzesnummer": row["nr"],
        "short_title": row["catalog"]["kurztitel"],
        "abbreviation": row["catalog"]["abkuerzung"],
        "instrument_type": row["catalog"]["typ"],
        "snapshot_as_of": date,
        "scope": "Current RIS display; no amendment history reconstructed.",
        "title_record": {
            "ris_id": row["catalog"]["document_id"],
            "valid_from": row["catalog"]["in_force_from"],
            "valid_to": row["catalog"]["in_force_to"],
            "validity_status": row["catalog"].get("validity_status"),
            "notes": row["catalog"].get("ris_notes"),
        },
        "source": {
            "url": row["source"]["url"],
            "retrieved_at": row["source"]["retrieved_at"],
            "response_sha256": row["source"]["sha256"],
            "snapshot_sha256": row["sha256"],
            "publisher": "Rechtsinformationssystem des Bundes (RIS), Bundeskanzleramt",
            "license": "CC-BY-4.0",
        },
        "provisions": records,
    }
    if output:
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "act.json").write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2) + "\n"
        )
    return metadata, checks, warnings


def flatten(nodes):
    for n in nodes:
        yield n
        if n["kind"] == "list_item":
            yield from flatten(n["children"])
