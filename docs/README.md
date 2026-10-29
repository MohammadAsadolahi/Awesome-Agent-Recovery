# Documentation directory

**Awesome Agent Recovery** is a curated, evidence-first guide to agent failure detection, safe intervention, environment repair, durable execution and independently verified recovery.

| I want to… | Start here | Follow with |
| --- | --- | --- |
| Decide what to do after a tool timeout or ambiguous write | [Recovery field guide](field-guide.md) | [Decision flow](../README.md#the-agent-recovery-decision-flow) |
| Understand idempotency, late commits, compensation and effect ledgers | [Transactional recovery review](research-update-2026-10-29-transactional.md) | [Production boundaries](production-systems.md) |
| Diagnose a long-horizon trajectory | [Failure localization papers](../README.md#failure-detection-localization-and-diagnosis) | [Previous research review](research-update-2026-10-29.md) |
| Choose a benchmark or fault-injection protocol | [Benchmarks and evaluation](benchmarks.md) | [Recovery-specific metrics](benchmarks.md#side-effect-correctness-and-the-recovery-denominator) |
| Compare workflow durability and checkpoint implementations | [Production systems](production-systems.md) | [Controlled simulation](../examples/ambiguous_write_demo.py) |
| Find definitions and interpretation guidance | [FAQ](faq.md) | [Curation policy](research-decision.md) |
| Contribute another paper or correction | [Contributing](../CONTRIBUTING.md) | [Catalog](../data/resources.csv) |

## Catalog conventions

[CSV](../data/resources.csv) is the **single editorial source of truth**; [JSON](../data/resources.json) is a synchronized derived representation. Both include IDs, kind, area, canonical URL, year/date, a one-sentence reason for inclusion, an optional code link, and an evidence/limitations note.

To validate a change:

```bash
python scripts/validate.py --sync-json
python scripts/validate.py
python -m unittest discover -s tests
```

The [main README](../README.md) deliberately favors **reading paths and decision aids**. Detailed evidence qualifications and experimental assumptions belong in these guides rather than in inflated README claims.
