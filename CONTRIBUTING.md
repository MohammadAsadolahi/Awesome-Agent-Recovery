# Contributing

Thank you for helping build a research-to-production reference for agent recovery.

## Submit a resource

1. Check that it is not already in the [CSV index](data/resources.csv).
2. Provide its **canonical primary-source URL**, date, and precise failure class.
3. Explain **what fails**, **how recovery works**, **what state is restored**, and limitations.
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