# Benchmarks and Evaluation Protocol

_Updated 2026-10-28. Numbers below are as reported by authors, not independently reproduced._

## Recovery-specific benchmarks

| Benchmark | Paper | Target failure | Caution |
| --- | --- | --- | --- |
| ReInBench | [When to Intervene?](https://arxiv.org/abs/2610.36471) | 1,403 errors in 1,259 traces; when self-recovery occurs | Intervention is not always beneficial |
| CUA-Recovery | [CUA-Recovery](https://arxiv.org/abs/2610.27645) | 2,250 inherited desktop error states | Detection and recovered completion differ |
| ToolMaze | [When Tools Fail](https://arxiv.org/abs/2606.05806) | Explicit/implicit, transient/permanent tool faults | Semantic corruption can look successful |
| Traverse | [Locating Hidden Failures](https://arxiv.org/abs/2609.17930) | First error across long trajectories | Does not measure external rollback |
| RegretBench | [Back Up Before You Regret](https://arxiv.org/abs/2610.28934) | Backup awareness over 205 coding tasks | Backup cannot reverse every external effect |
| MettleBench | [AgentRewind](https://arxiv.org/abs/2608.14380) | Controlled long-horizon engineering tasks | Results are environment-specific |

No results above constitute a cross-benchmark leaderboard.

## Minimum experiment record

Report the task/environment; exact injected or observed failure; agent and model version; the no-recovery and plain-retry baselines; number of runs; the success verifier; side effects; error-awareness measure; recovery latency/cost; and reproducibility details such as scripts, seeds, code commits and data licenses.

**A passing end-task score is not sufficient:** also inspect the trajectory for deleted files, fabricated success, duplicate writes, and unintended permissions.

## Suggested local scenarios

- **Implemented:** response timeout *after* committed write; blind retry versus reconciliation and idempotency in the [demo](../examples/ambiguous_write_demo.py).
- **Future work:** process crash at step boundary, partial batch success, a plausible-but-wrong tool result, and corrupted sandbox state.

Do not label future scenarios implemented before their tests exist.