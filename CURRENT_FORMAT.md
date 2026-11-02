# Current-law data format, version 1

```text
data/current/
  catalog.json
  manifest.json
  quality-report.json
  10000138/
    act.json
    titel.md
    art-010.md
  10001597/
    act.json
    art-002/par-0024.md
```

The eight-digit RIS Gesetzesnummer is the instrument key. The catalog maps it to a title and abbreviation.
One Markdown file represents each source article, paragraph, title or annex. Ordered `provisions` in `act.json`
preserve source order. Existing historical law folders are unchanged.

## Legal text

UTF-8 Markdown retains visible source wording, punctuation, numbering, headings and nested lists. Each paragraph
is one logical source line, with one blank line between blocks. Layout whitespace, RIS styles and hidden
accessibility restatements are removed. No legal wording is rewritten by a model. Markdown syntax is escaped
where it would swallow legal numbering or signal patterns.

Ordinary tables use Markdown. Merged/nested tables retain minimal semantic table markup with row/column spans.
Superscripts and subscripts retain semantic inline tags. Source citations remain links. Invalid nested source
anchors and empty links are accounted for in an explicit additional-reference section; their labels are never
substituted for legal wording. PDF-only annexes and source images remain explicit links, marked `linked_only`.
Embedded `ris-attachment://` references are retained as source extensions; they are not claimed to be mirrored
assets or converted image text. Do not infer text through OCR.

## Metadata and provenance

`act.json` records schema version, Gesetzesnummer, title, abbreviation, instrument type, snapshot date, title-record
validity, source URL/retrieval time/hashes, and an ordered list of provisions. Each provision records the source
index designation, actual heading when available, source-law context, Markdown path/hash, source fingerprint,
notes, links, images, table cells/spans, and unusual source-extension fields.

The title's NOR identifier and validity dates are explicitly scoped to `title_record`. Whole-law responses do
not provide NOR identifiers or validity windows for every provision. `source_record_id: null` means unknown.
A source block index is an audit locator, not a durable legal identifier. `snapshot_as_of` is an observation date,
not an enactment date. Null/missing title start dates retain `unknown_missing_start_date` plus RIS notes.

Raw responses and the capture manifest remain in the local cache. The clean manifest hashes each metadata file;
metadata hashes every Markdown file. The source manifest hash connects the clean candidate to its raw acquisition.

## Repeated designations

Do not overwrite repeated RIS designations. Prefer an explicit source-law qualifier, such as
`art-032--bgbl-i-1997-140.md`. Retain treaty suffixes from actual source headings, such as `art-005bis.md`, while
also recording the RIS index's original designation.

Where the downloaded source still cannot distinguish legal identities, `tools/current-identities.json` freezes
reviewed local record keys against exact visible-source fingerprints. `--record-<key>` is a repository key,
not an invented NOR number or legal citation. Text-identical duplicate entries are both retained, with separate
occurrence keys. Changes to ambiguous text or duplicate counts invalidate that mapping and require review;
never match a changed ambiguous record by position or silently reassign it. An unmatched fallback filename may
exist in a failed local candidate, but `identity_review_required` blocks export.

## Completeness and review gates

Every catalog instrument and every source block must be accounted for exactly once, with unique safe paths.
An independent Markdown renderer must preserve all visible non-whitespace characters (soft hyphens normalized),
source links, image references, table row/cell spans, superscripts and subscripts. Unknown structures are flagged.
No-op reruns are byte deterministic. Semantic diffs exclude acquisition timestamps and source block positions.

A complete build can still fail quality checks: `complete` means source accounting completed; `blocking_issues`
must also be empty. Export requires successful checks and an explicit review receipt tied to the exact manifest.
Representative rendered documents must be inspected, including complex tables, attachment-only annexes,
repeated designations and unknown dates. Automated checks do not certify legal interpretation or the content
of external images/PDFs.
