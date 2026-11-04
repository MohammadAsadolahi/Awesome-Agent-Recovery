# Recovery Benchmarks and Evaluation Protocol

**Updated: 4 November 2026.** All quantitative claims are from their authors unless independently reproduced. These benchmarks cover different environments and metrics; **do not build a cross-paper leaderboard**.

## Benchmarks that test recovery after failure

| Publication | Failure / intervention | What is actually measured |
| --- | --- | --- |
| [Recovery-Bench](https://openreview.net/forum?id=8FZRnDgDxq) | Restart in an inherited failed terminal-task state | Post-failure task completion, distinct from clean-task competence |
| [CUA-Recovery](https://arxiv.org/abs/2610.27645) | Persistent inherited desktop errors | Recognition and successful correction of inherited error states |
| [ReTrace](https://arxiv.org/abs/2610.27954) | Controlled GUI mistakes and goal-oriented replay | Transition-consistent recovery, not mere screenshot similarity |
| [CUADebug](https://aclanthology.org/2026.findings-emnlp.530/) | Annotated GUI trajectory errors and corrected reruns | Root-cause localization and restored task success separately |
| [GUI-RobustEval](https://proceedings.mlr.press/v306/bu26b.html) | Executable GUI policy mistakes | Failed-state recovery and trajectory-synthesis effectiveness |
| [ToolMaze](https://arxiv.org/abs/2606.05806) | Transient/permanent and explicit/silent tool faults | Dynamic replanning and completed recovery under tool perturbations |
| [ToolMisuseBench](https://aclanthology.org/2026.realm-1.28/) | Deterministic typed tool faults | Recoverability and output-grounded recovery scoring |
| [RITE](https://arxiv.org/abs/2610.27777) | Matched correct, explicit-error and plausible-wrong tool values | Recognition, verification and end-to-end task recovery |
| [ParaRecover](https://aclanthology.org/2026.emnlp-main.975/) | Parallel tool branches and error propagation | Process-level localization and bounded repair/replanning |
| [BENCH2ROBUST](https://arxiv.org/abs/2608.11977) | Retryable, fallback-required and impossible tool conditions | Retry / switch / abstain policy effectiveness |
| [Agent Error Dataset](https://arxiv.org/abs/2609.40111) | 50,228 error/diagnosis records with checkpoint-matched subset | Correction success on matched replays, not external transactions |
| [AgentCheck](https://arxiv.org/abs/2607.11098) | Repeatable MCP tool errors with matched mitigation trials | Failure reproduction, rerun and concrete mitigation outcomes |
| [UndoBench](https://arxiv.org/abs/2610.05622) | Paired lost-ACK business writes in different mutation phases | Conditional recovery vs nominal competence, duplicates and missing effects |
| [LIMBO](https://arxiv.org/abs/2609.29095) | Service-level lost ACK, late commit, redelivery, partial batch | **Actual effect ledgers** and contract-dependent duplicate effects |
| [ReplayRCA](https://arxiv.org/abs/2610.41025) | Single corrected action after reset to a chosen failed step | Causal repair score against original-action placebo replay |

Several methods study **whether an intervention helps at all**: [From Credit Assignment to Repair](https://aclanthology.org/2026.realm-1.15/), [Oracle-State Intervention](https://aclanthology.org/2026.realm-1.6/), [Repairs for Whom?](https://arxiv.org/abs/2610.38610), and [When to Intervene?](https://arxiv.org/abs/2610.36471). Negative results are important: diagnosis or a stronger evaluator can fail to improve the executed outcome.

## Minimum reproducible experimental record

For each failure/recovery case report:

- **Task and agent:** environment, model/executor, exact software/benchmark version and limits.
- **Failure:** injected or observed cause, fault timing, affected tool or state, clean-run paired control.
- **Recovery plan:** trigger, decision to continue/retry/switch/compensate/restore/stop, and intervention budget.
- **Evidence:** what was observed before and after intervention, and which authoritative independent verifier was used.
- **External effects:** committed, duplicate, missing or irreversible writes; in-flight requests; idempotency and consistency assumptions.
- **Metrics:** conditional recovery denominator; false-positive/negative intervention rate; genuine postcondition success; collateral effects; tokens/latency/cost; safe abstention.
- **Reproducibility:** number of runs, confidence intervals where possible, seeds, known exclusions, code and data license when released.

## Five-stage reporting taxonomy

| Stage | Minimum observable result | Do not claim |
| --- | --- | --- |
| 1. Detect | Failed action noticed, with clean controls | Root cause identified |
| 2. Attribute | Causal step/hypothesis grounded in evidence | Proposed repair works |
| 3. Decide | Bounded correction, restore, compensation or abstention plan | Corrected execution |
| 4. Execute | Rerun or live intervention changes task outcome | Correct external state |
| 5. Verify | Independent postconditions and effect ledger correct | General performance beyond tested boundaries |

**Known pitfalls:** an empty status read can precede a late commit; an oracle-state intervention may still fail to rescue a task; a clean-task-success percentage is not conditional recovery success; and a model can report success while causing unintended side effects.

For implementation-relevant safety boundaries, see the [field guide](field-guide.md). For the reason the benchmark list was cut down, see the [full audit](curation-audit-2026-11-04.md).
