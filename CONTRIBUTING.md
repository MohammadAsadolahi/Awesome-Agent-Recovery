# Contributing

Thank you for helping build a research-to-production reference for agent recovery.

## Submit a resource

1. Check that it is not already in the [CSV index](data/resources.csv), including alternate titles, venues, preprint and published versions.
2. Provide its **canonical primary-source URL**, date, and precise failure class.
3. Explain **what fails**, **how recovery works**, **what state is restored**, **how success is independently verified**, and limitations. Specify if the contribution measures only detection or diagnosis.
4. Distinguish **author-reported results** from **independently replicated** results.
5. Add a row to the CSV and run: python scripts/validate.py --sync-json.
6. Add a short annotated README entry if it improves navigation.
7. Run: python scripts/validate.py and python -m unittest discover -s tests.

Prefer peer-reviewed articles where available; label preprints and unreleased code accurately. Do not include promotional links, fake results, personal information, tokens, or private logs.

## In scope

Failure detection and attribution that leads to repair, test-time recovery and intervention, fault injection, safe retry/reconciliation, checkpointing, rollback, durable execution, and multi-agent containment.

## Out of scope

Generic agent framework dumps, unrelated benchmarks, undemonstrated product claims, affiliate links, and duplicate catalogs.

Pull requests should be small, factual, and easy to verify. Corrections to existing entries are welcome.
## Pull request review checklist

- [ ] Primary scholarly or official documentation URL verified; paper title, date and venue match.
- [ ] Scope is failure-specific and meaningfully non-duplicative; record whether it detects, diagnoses, repairs, reruns or verifies.
- [ ] Any claimed numbers are **author-reported**, with benchmark, denominator and environment named.
- [ ] Code/project link was inspected; no unsupported runnable/released-code claim.
- [ ] CSV edited as the source of truth, JSON regenerated with `python scripts/validate.py --sync-json`.
- [ ] README, relevant docs, and any resource-count badge updated when needed.
- [ ] `python scripts/validate.py` and `python -m unittest discover -s tests` pass; avoid unrelated rewriting.

For the intended document layout, see [documentation index](docs/README.md) and [curation policy](docs/research-decision.md). A recent example of a sourced batch is [the October research update](docs/research-update-2026-10-29.md).
