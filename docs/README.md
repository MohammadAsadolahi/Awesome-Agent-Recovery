# Documentation

**A focused research bibliography about recovering failed tool-using LLM agents.** Start with the [main 57-paper index](../README.md) rather than dated historical collections.

| Need | Document |
| --- | --- |
| Find and compare high-value recovery publications | [Curated README](../README.md#curated-papers) |
| Understand the strict inclusion/exclusion test | [Curation and evidence policy](research-decision.md) |
| See why each prior item was kept or removed | [Complete 4 November 2026 audit](curation-audit-2026-11-04.md) |
| Choose benchmarks and recovery outcome measures | [Benchmark protocol](benchmarks.md) |
| Handle ambiguous effects, bounded retry and restoration | [Recovery field guide](field-guide.md) |
| Get answers to common recovery questions | [Focused FAQ](faq.md) |
| Submit a directly relevant publication | [Contribution guide](../CONTRIBUTING.md) |
| Work with machine-readable sources | [CSV](../data/resources.csv) · [JSON](../data/resources.json) |

## Reproducible maintenance

The only editable catalog is `data/resources.csv`; the JSON copy is generated and kept in sync:

```bash
python scripts/validate.py --sync-json
python scripts/validate.py
python -m unittest discover -s tests
```

The catalog contains **57 original research publications** as of 4 November 2026. General runtime/product catalogs and prior superseded research roundups are no longer part of the active repository; their history remains available through Git.
