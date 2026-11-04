# Contributing to Awesome Agent Recovery

This is a **selectively curated research bibliography**, not a general agent resource list. Contributions are welcome when they meaningfully strengthen the evidence for **how a failed LLM agent can recover safely**.

## Before proposing a paper

1. Read the [scope and evidence policy](docs/research-decision.md) and [November 2026 curation audit](docs/curation-audit-2026-11-04.md).
2. Search [the current catalog](data/resources.csv) for the same paper under alternate preprint, proceedings, project or title URLs.
3. Verify the primary scholarly source, authors, year and publication status. Do not assume an arXiv preprint was peer-reviewed.
4. Explain the **specific agent failure**, the corrective action (or recovery-specific benchmark), the baseline, **how the outcome was measured**, and limitations.
5. State what makes this source **distinct and stronger** than the closest existing entry. A second generic reflection or retry paper is rarely enough.

**Do not propose** standalone code/project links, generic agent frameworks, product documentation, unconnected surveys, prevention-only material, or papers that just have *reliability* or *recovery* in their title.

Companion implementations belong in an accepted paper's optional `code` column; they are not separate catalog items.

## Editing the catalog

[`data/resources.csv`](data/resources.csv) is the single editorial source. Each row must have `kind=paper`, a canonical scholarly URL, precise descriptive annotation, and a candid evidence/limitations note. Then run:

```bash
python scripts/validate.py --sync-json
python scripts/validate.py
python -m unittest discover -s tests -v
python examples/ambiguous_write_demo.py
```

Update the paper annotation in [README.md](README.md) only if accepted. Keep the README focused; do not append an entire paper abstract or inflate the reading list merely for recency.

## Pull request checklist

- [ ] Original scholarly publication, not duplicate/preprint mirror.
- [ ] A failed **tool-using LLM agent** and a recovery-relevant mechanism or evaluation are central to the paper.
- [ ] The baseline, intervention or controlled failure, verifier, and recovery denominator are described.
- [ ] The contribution is distinguishable from retained papers; nearest overlap is identified.
- [ ] Publication status, code availability, generalization limits, and author-reported results are accurate.
- [ ] `kind=paper`, canonical research URL, and synchronized JSON pass validation.
- [ ] README, metadata, and relevant documentation remain consistent.

Corrections and **removals of low-fit entries** are as valuable as additions. Git history preserves the original catalog so curation can be revisited without hiding prior decisions.
