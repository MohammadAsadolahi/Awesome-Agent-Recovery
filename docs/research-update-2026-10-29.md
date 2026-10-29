# Research Update: Agent Recovery and Curation Patterns — 29 October 2026

This update extends the prior 28 October review. Sources below were checked against primary publisher/arXiv records and linked author/project materials. Reported results are **author claims, not independent reproduction**. Published venue pages take precedence over earlier abstract or project summaries when numbers differ.

## Selection criteria

Each accepted paper contributes a different failure mode, method, or evaluation tool to the existing set: (1) explicit agent failure relevance, (2) verifiable primary source, (3) a distinguishable recovery or diagnosis boundary, (4) actionable engineering or evaluation implications, and (5) stated limitations. Strongest priority: a path from a *diagnosed* failure to a *bounded verified* rerun, and systematic failure injection.

## Eight additions

| Source | What is new for this repository | What the evidence does **not** establish |
| --- | --- | --- |
| [AgentDebugX](https://aclanthology.org/2026.emnlp-demos.52/) ([code](https://github.com/AgentDebugX/AgentDebugX)) | Detect → attribute → recover → rerun; reports 13 of 73 GAIA failed tasks repaired in one rerun | Independent replication or arbitrary external rollback; error-memory sharing must be scrubbed and opt-in |
| [AgentRx](https://aclanthology.org/2026.findings-emnlp.598/) ([code](https://github.com/microsoft/AgentRx)) | Step-constraint checks and evidence-backed validation log; final publication benchmarks 170 annotated traces | A recovery action or restored state. Early Microsoft summaries describe **115** traces, a version difference |
| [CUADebug](https://aclanthology.org/2026.findings-emnlp.530/) ([project](https://cuadebug.github.io/)) | 204 computer-use failure annotations and screenshot-grounded root-cause correction; single reroll recovery 13.89% → 29.86% in an evaluated subset | Live remote transaction safety; reroll comparisons rely on specific controlled restart conventions |
| [TRAJDEBUG](https://aclanthology.org/2026.findings-emnlp.437/) ([code](https://github.com/THU-KEG/TrajDebug)) | Tracks error lifecycle and persistence, so self-corrected local mistakes are not mistaken for the terminal causal error; 486 annotated failures | Guaranteed recovery of environment state or side-effect compensation |
| [AgentChaosBench](https://arxiv.org/abs/2608.14680) ([code and data](https://github.com/kevinzck8k/agentic-fault-diagnosis)) | 275 traces, 10 injected fault classes, with MCP/A2A/guardrail and matched no-fault reference | End-task recovery after intervention; primary benchmark evaluates detection/localization |
| [Agent Error Simulator](https://grc.iit.edu/publications/bateman-2026-agent-error-simulator-3c7d/) ([code](https://github.com/Keith-Bateman/agent-error-simulator)) | Declarative transparent-proxy injection of format, logic and tool-call faults in planner/worker/aggregator roles | Broad generalization beyond the evaluated workflows and HPC environment |
| [PROBE](https://arxiv.org/abs/2605.08717) | Evidence-gated, structured recovery guidance across software engineering and operations; authors report 21.79% recovery on 257 initially unresolved cases | Correct diagnosis by itself repairing the task; independent validation of the reported rate |
| [Agent Error Dataset / AET](https://arxiv.org/abs/2609.40111) | 50,228 error–diagnosis pairs; 3,062 matched replay comparisons under compatible reset settings | Recovery in non-resettable external environments; claims are from a preprint |

## Comparison to existing papers (deduplication)

- **Traverse** already addresses first-error detection. **AgentRx** adds auditable constraint evidence; **TRAJDEBUG** adds resolved-vs-persistent error lifecycle.
- **CUA-Recovery** tests inherited persistent desktop mistakes. **CUADebug** instead localizes an agent's earlier causal GUI step and tests conditional re-execution.
- **ToolMaze** perturbs tools and replanning. **AgentChaosBench** broadens to A2A delegation and guardrail faults while measuring telemetry diagnosis; **Agent Error Simulator** adds a declarative proxy injector for workflow experiments.
- **Sentry** adds test-time lessons. **PROBE** restricts engineering recovery guidance using a telemetry/diagnosis gate; **AED/AET** evaluates correction proposals with checkpoint-matched replay when possible.

## Evaluation recommendations

Track fault recognition, causal localization, bounded recovery proposal, rerun success, and independent authoritative state verification as **separate stages**. For every result record the denominator, test task domain, checkpoint alignment, whether restart steps are predicted/human-labeled, duplicate side effects, cost/latency, and what cannot be reversed. An error detector is not an external transaction manager.

## Lessons from highly starred Awesome collections

Studied [sindresorhus/awesome](https://github.com/sindresorhus/awesome) and its [manifesto](https://github.com/sindresorhus/awesome/blob/main/awesome.md), [vinta/awesome-python](https://github.com/vinta/awesome-python), [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted), [avelino/awesome-go](https://github.com/avelino/awesome-go), and [papers-we-love/papers-we-love](https://github.com/papers-we-love/papers-we-love).

| Pattern | Adaptation here | Deliberate non-adoption |
| --- | --- | --- |
| Clear short scope statement and readable sections | Keep prominent failure question; add task-to-research map and documentation index | No sprawling generic AI tools taxonomy |
| Discoverable categories and quick navigation | Group by failure/repair mechanism and benchmark purpose | No hundreds of near-empty categories |
| Consistent descriptions and curation over accumulation | Add narrow paper summaries, source/limitations and a review checklist | No artificial star rankings or unsupported "best" labels |
| Contributor instructions and reproducible validation | CSV-as-source, JSON sync, repo tests and contribution checklist | No automatic admission of unrelated link submissions |
| Reader-friendly formats | README, documentation map, CSV, JSON and optional llms.txt | No new external website or paid service dependency |

## Deferred / excluded

Broad observability dashboards without demonstrated corrective actions; generic agent-safety/benchmark surveys without recovery-specific tests; duplicate arXiv vs venue versions; claims that checkpointing undoes remote writes; preprints or code not verifiable at a primary source. No claims are made that this update surveyed *every* publication through this date.
