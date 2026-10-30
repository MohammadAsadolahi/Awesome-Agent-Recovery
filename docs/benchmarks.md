# Benchmarks and Evaluation Protocol

_Updated 2026-10-30. Numbers below are as reported by authors, not independently reproduced._

## Recovery-specific benchmarks

**Compare only matched failure phases and denominators.** A diagnosis score does not imply a safe retry; nominal task success does not imply recovery from injected faults.

| Benchmark | Paper | Target failure | Caution |
| --- | --- | --- | --- |
| MCP-Injector | [Realistic MCP Faults](https://arxiv.org/abs/2610.32555) | Incident-derived protocol fault persistence across tested model/stacks | Two tested model sizes; no general scale conclusion |
| RITE | [Silent Tool Errors](https://arxiv.org/abs/2610.27777) | 501 paired correct/explicit/silent-condition instances | E-commerce workflows and frozen tools |
| Async-RBench | [Asynchronous Task Execution](https://arxiv.org/abs/2610.32429) | 200 executable tasks in eight subagent-result scenarios | Replanning score not equivalent to task success |
| AndroidFlux | [Mobile Agent Error Recovery](https://arxiv.org/abs/2610.34384) | Checkpoint-aligned AndroidWorld recovery and action ranking | Controlled device state and rollout setting |
| SSCBench | [Evidential Validity](https://arxiv.org/abs/2610.11514) | 1,191 faulted runs; counterevidence before first faulty reliance | Exposure validity is not repair success |
| RetryRealistic | [When Tools Fail, Agents Fabricate](https://openreview.net/forum?id=HLCpv21u07) | 30 tasks, nine fault types, file/SQLite/HTTP ground truth | Honest failure vs fabricated answer; workshop per authors |
| LIMBO | [Where Does Exactly-Once Live?](https://arxiv.org/abs/2609.29095) | 25,930 author-reported episodes across service contracts, late commits and duplicate delivery | Tracks real effect ledger in sandbox; does not establish generic exactly-once |
| UndoBench | [Separating Task Competence from Recovery](https://arxiv.org/abs/2610.05622) | 2,880 paired lost-ACK trials in the authors' frozen study; pre/during/post-mutation scenarios | Report conditional recovery and duplicate effects separately from nominal task completion |
| GUI-RobustEval | [Recovering Policy-Induced Errors](https://proceedings.mlr.press/v306/bu26b.html) | 1,216 executable GUI recovery cases | Controlled GUI environment; not remote transaction reversal |
| ToolMisuseBench | [Offline Deterministic Tool Misuse and Recovery](https://aclanthology.org/2026.realm-1.28/) | 1,200 public-test cases in seed-42 release | Frozen offline faults and tool contracts |
| ParaRecover | [Parallel Tool-Use Recovery](https://aclanthology.org/2026.emnlp-main.975/) | 10,626 process-level instances and 14 error types | Error localization and replanning, not distributed atomicity |
| BENCH2ROBUST | [Retry, Switch, or Abstain?](https://arxiv.org/abs/2608.11977) | Scenario-controlled solvability and recovery policy | Synthetic tool faults; explicitly include safe stop |
| Recovery-Bench | [Evaluating Agentic Recovery from Mistakes](https://openreview.net/forum?id=8FZRnDgDxq) | Recovery from polluted context and inherited failure trajectories | OpenReview submission; publication/acceptance status not verified |
| EpiSEM-Bench | [Evidence Recovery under Missing Evidence](https://arxiv.org/abs/2610.31650) | 300 matched unsafe/safe task pairs, author-reported | Safety evidence acquisition, not external state restore |
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

## Side-effect correctness and the recovery denominator

In addition to ordinary completion, record **whether the same task would succeed without the injected fault**. [UndoBench](https://arxiv.org/abs/2610.05622) formalizes conditional recovery success among paired nominally capable cases. Report duplicate-effect rate, missing-effect rate and authoritative postconditions as separate columns.

Failure phase matters: `PRE_MUTATION`, `DURING_MUTATION`, and `POST_MUTATION_PRE_ACK` can have different recovery possibilities. Include delayed in-flight commits, response loss, redelivery and partial batch commits where the tool contract permits controlled injection.

[LIMBO](https://arxiv.org/abs/2609.29095) shows that an empty immediate read-back does not prove an earlier timed-out call cannot still commit. Use stable operation keys, conditional writes or a terminal-status contract when the downstream API offers them; otherwise account for unresolved uncertainty and safe stop.

[Same Winners, Different Success Rates](https://arxiv.org/abs/2609.34215) demonstrates that high checkpoint action-ranking agreement can coexist with near-zero absolute success. Report agreement, all-zero fraction, held-out success and pooled success together when evaluating checkpoint policies.

## New evaluation threats: executor mismatch and missing evidence

- [Repairs for Whom?](https://arxiv.org/abs/2610.38610) shows that a repair scored with a stronger evaluator can be less valuable when the deployed agent executes it. Record **both evaluator and executor models**, and validate selected fixes on the actual executor.
- [SSCBench](https://arxiv.org/abs/2610.11514) distinguishes counterevidence that could be observed **before first faulty use** from counterevidence arriving later. Record injection, first visibility, first consumption and first incorrect reliance.
- [Async-RBench](https://arxiv.org/abs/2610.32429) separates the response contract (what to change/preserve/reverify) from final task success. Track result order, duplicate notifications, stale dependencies and prohibited effects.
- [Failure-Transparent Agents](https://arxiv.org/abs/2609.35732) and [RetryRealistic](https://openreview.net/forum?id=HLCpv21u07) separate honest failure, unsupported success claims and verified recovery. A false-success reduction **does not** by itself mean tool effects were repaired.
- [Permission to Retry](https://arxiv.org/abs/2610.31916) requires checking authorization at replay and reconciliation, not only at initial dispatch.

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

An improved diagnosis score does **not** imply improved safe recovery. Report the **denominator** for recovery (failed cases vs all tasks), whether the restart point is human-labeled or predicted, and whether the environment is resettable. See the [30 October evidence review](research-update-2026-10-30.md), [transactional recovery review](research-update-2026-10-29-transactional.md) and [earlier diagnostics review](research-update-2026-10-29.md) for paper-specific caveats.
