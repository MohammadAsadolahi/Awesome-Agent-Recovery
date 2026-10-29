# Benchmarks and Evaluation Protocol

_Updated 2026-10-29. Numbers below are as reported by authors, not independently reproduced._

## Recovery-specific benchmarks

| Benchmark | Paper | Target failure | Caution |
| --- | --- | --- | --- |
| AgentChaosBench | [When Agentic Executions Fail](https://arxiv.org/abs/2608.14680) | 275 sanitized traces; 10 types of MCP/A2A/guardrail faults and no-fault controls | Fault-type and location detection, **not** completed recovery |
| Agent Error Simulator | [Fault Injection for Testing Recovery](https://grc.iit.edu/publications/bateman-2026-agent-error-simulator-3c7d/) | Declarative format, logic and tool-call faults in hierarchical workflows | Domain-specific jobs and HPC setup; not a universal leaderboard |
| TrajErrBench | [TRAJDEBUG](https://aclanthology.org/2026.findings-emnlp.437/) | 486 annotated failed trajectories; error lifecycle | Attribution is not state restoration |
| AgentRx Benchmark | [AgentRx](https://aclanthology.org/2026.findings-emnlp.598/) | 170 annotated failed trajectories in final ACL publication | Earlier project summaries describe an earlier 115-case release |
| CUAErrorBench | [CUADebug](https://aclanthology.org/2026.findings-emnlp.530/) | 204 annotated computer-use failures; evaluates root cause and rerolls | Rerollout requires controlled restart/evaluation conditions |
| Agent Error Dataset | [AED / AET](https://arxiv.org/abs/2609.40111) | 50,228 diagnoses; subset of 3,062 matched replay pairs | Replay feasibility varies; results not external exactly-once correctness |
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
## Evaluation taxonomy: do not collapse distinct success measures

| Level | Metric | Necessary evidence |
| --- | --- | --- |
| 1. Detect | Recall / false alarms on injected or observed faults | Fault labels and clean controls |
| 2. Localize | First-critical-step, fault-type and location accuracy | Human or injected causal reference; distinguish resolved errors |
| 3. Propose | Actionability and policy compliance of recovery plan | Evidence link and guardrail checks |
| 4. Execute | Successful rerun after recovery attempt | Controlled restart and no-recovery baseline |
| 5. Verify | Correct external state, no duplicate/irreversible collateral effects | Independent authoritative checks and side-effect ledger |

An improved diagnosis score does **not** imply improved safe recovery. Report the **denominator** for recovery (failed cases vs all tasks), whether the restart point is human-labeled or predicted, and whether the environment is resettable. See the [research review](research-update-2026-10-29.md) for paper-specific caveats.
