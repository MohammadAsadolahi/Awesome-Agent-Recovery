# Documentation and Resource Map

Start with the task you want to accomplish. This is a curated research/engineering reference, **not** a recovery library or a promise of automated rollback.

| You want to… | Start here | Next step |
| --- | --- | --- |
| Choose a response after a live failure | [Field guide](field-guide.md) | [Decision flow in README](../README.md#the-agent-recovery-decision-flow) |
| Diagnose the first causal mistake | [Research papers](../README.md#failure-detection-localization-and-diagnosis) | [Evaluation levels](benchmarks.md#evaluation-taxonomy-do-not-collapse-distinct-success-measures) |
| Design or evaluate a recovery benchmark | [Benchmarks](benchmarks.md) | [Resource metadata](../data/resources.csv) |
| Safely resume a crashed workflow | [Production systems](production-systems.md) | [Ambiguous-write demo](../examples/ambiguous_write_demo.py) |
| Compare new research and decide what to add | [29 October 2026 review](research-update-2026-10-29.md) | [Evidence and scope policy](research-decision.md) |
| Find definitions and common questions | [FAQ](faq.md) | [llms.txt](../llms.txt) |
| Suggest papers or fixes | [Contribution guide](../CONTRIBUTING.md) | [Machine-readable catalog](../data/resources.json) |

## Data maintenance

The single editable resource index is [`data/resources.csv`](../data/resources.csv). Generate [`data/resources.json`](../data/resources.json) with `python scripts/validate.py --sync-json`; then run `python scripts/validate.py` and `python -m unittest discover -s tests`. Annotations should name the **failure boundary** and **verification limit** rather than just saying a framework improves reliability.

The [main README](../README.md) contains the shorter hand-curated reading paths and recovery decision table. Detailed guides stay in `docs/` so the homepage remains approachable.
