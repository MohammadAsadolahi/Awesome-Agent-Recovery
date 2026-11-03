# Research Review — 3 November 2026

**Decision:** admit **23 distinct research publications** to the previous 79-resource catalog (**102 resources total; 84 papers**). This review adds **only papers**, not tools, guides or duplicate code entries. Original arXiv and ACL Anthology records were checked against the existing CSV catalog and repository scope on 3 November 2026. All performance statements remain **author-reported**, not independently reproduced.

## Admission tests and scope

Every admitted work (1) has an identifiable original paper/preprint or proceedings record; (2) studies a failure *of an AI agent* (rather than a software bug an agent happens to fix); (3) offers failure diagnosis tied to intervention, a concrete recovery/restore mechanism, or a failure-specific recovery benchmark; (4) adds a distinguishable mechanism or evaluation test beyond the existing collection; and (5) states what the experiments do **not** establish. An arXiv entry is a **preprint**, not verified peer review. A controlled replay or checkpoint never proves arbitrary third-party exactly-once side effects.

## Admitted publications

### Transactional recovery and external effects

| Original publication | Distinct contribution and limitations |
| --- | --- |
| [Evidence-Guided Recovery for AI Agents with Ambiguous Tool Outcomes and Partial Execution](https://arxiv.org/abs/2610.41453) (2026-10-30) | Plans safe continuation after ambiguous tool outcomes using publicly supported effect states, provider contracts and independent replay certificates. **Limit:** 2026 preprint; finite assignments and local-model comparisons. Certificates depend on declared provider capabilities; no general exactly-once guarantee. |
| [Cordon: Semantic Transactions for Tool-Using LLM Agents](https://arxiv.org/abs/2606.17573) (2026-06-16) | Stages agent tool effects in task-scoped semantic transactions with reversible shadow state, validation and recovery metadata. **Limit:** 2026 preprint; staged effects and adapter boundaries only, not universal atomicity for all external systems. |
| [Engineering Reliable Commit Gates for Agentic AI: Cost-Aware Verification Portfolios under Common-Mode Data Failures](https://arxiv.org/abs/2609.10969) (2026-09-10) | Tests independent evidence, commit guards, concurrent writes and lost responses to distinguish verification from effect safety. **Limit:** 2026 preprint; controlled faults plus bounded HTTP/SQLite study. Generalization across unseen fault families is limited. |

### Failure localization and evidence

| Original publication | Distinct contribution and limitations |
| --- | --- |
| [From Credit Assignment to Repair: A Leakage-Controlled Diagnostic Study of Tool-Using Agents](https://aclanthology.org/2026.realm-1.15/) (2026-10) | Tests whether failure localization causes useful selective tool-agent repair and reports a reproducible negative result for its selected intervention gate. **Limit:** REALM 2026 workshop; on tested tau2-bench tasks interventions rarely changed trajectories and did not improve binary reward. Negative result, not a recovery solution. |
| [REFLECT: Intervention-Supported Error Attribution for Silent Failures in LLM Agent Traces](https://arxiv.org/abs/2606.09071) (2026-06-08) | Tests suspected silent agent errors with targeted patch-and-replay interventions before confirming causal attribution. **Limit:** 2026 preprint; measures localization quality rather than end-to-end task or external-state recovery. |

### Tool faults, intervention and self-recovery

| Original publication | Distinct contribution and limitations |
| --- | --- |
| [Verify--Backtrack Loop: Structured Precondition Recovery for Long-Horizon Language Agents](https://arxiv.org/abs/2610.41564) (2026-10-30) | Uses goal-stack verification and typed failure attribution to trigger explicit retry, subgoal updates or backtracking after unmet prerequisites. **Limit:** 2026 preprint; AppWorld, ALFWorld and ScienceWorld experiments. Backtracking is an agent planning-state operation, not arbitrary external rollback. |
| [AgentHeal: Evaluating Goal-Preserving Resource Recovery of Web Agents under Access Barriers](https://arxiv.org/abs/2610.39234) (2026-10-29) | Benchmarks web-agent recovery from blocked links, authorization walls and rate limits while preserving the original authorized goal. **Limit:** 2026 preprint; sandbox and real-website replay. Alternative resources must remain legitimate and policy-compliant; not generic transaction rollback. |
| [PRFC: Learning Progressive Recovery from Function Calling Errors for Tool-Using LLMs](https://aclanthology.org/2026.findings-emnlp.1762/) (2026-10) | Trains successive corrective tool calls with progress-aware rewards after observed function-calling failures. **Limit:** Findings of EMNLP 2026; multi-turn BFCL-v3 and three single-step tool tasks; improved call recovery does not certify external effects. |
| [When Harnesses Lose the Signal: Causal Evaluation of Recovery in LLM Agents](https://arxiv.org/abs/2610.00372) (2026-09-30) | Compares paired continuations with versus without a harness recovery operation to measure both rescued and harmed trajectories. **Limit:** 2026 preprint; ALFWorld and one tested model setting, not a cross-domain guarantee of intervention value. |
| [Diagnosis Before Recovery: Turning Agent Failures into Selective Self-Correction](https://arxiv.org/abs/2608.11772) (2026-08-12) | Profiles failure classes and selects admissible recovery interventions before test-time agent self-correction. **Limit:** 2026 preprint; task-family profiling and frozen recovery policies; validity beyond evaluated environments remains unproven. |
| [Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors](https://aclanthology.org/2026.acl-long.1880/) (2026-07) | Turns execution errors into on-policy training examples and resampled correction rollouts for multi-turn tool-call recovery. **Limit:** ACL 2026 long paper; recovery rates are benchmark-specific; training benefit is not transaction-safe live replay. |
| [Wink: Recovering from Misbehaviors in Coding Agents](https://arxiv.org/abs/2602.17037) (2026-02-19) | Monitors coding-agent drift, loops and tool failures and applies targeted runtime course-correction interventions. **Limit:** 2026 preprint; author-reported production trajectory and intervention study; not general environment rollback. |
| [AgentCheck: A Reproduce-Intervene-Mitigate Workbench for LLM Agents over MCP](https://arxiv.org/abs/2607.11098) (2026-07-13) | Reproduces MCP tool faults and reruns agents under matched failures to test whether specific mitigations actually recover outcomes. **Limit:** 2026 preprint; twelve injected fault types and five tested agents. Interpretive labels partly use LLM judgment; not broad production validation. |
| [Beyond Function Calling: Benchmarking Tool-Using Agents under Tool-Environment Unreliability](https://arxiv.org/abs/2606.25819) (2026-06-24) | Provides deterministic multi-step tasks with recoverable tool hazards and scores whether retry, fallback or verification succeeds. **Limit:** 2026 preprint; seeded benchmark with constructed recovery paths, not necessarily real-world provider fault contracts. |
| [Failure makes the agent stronger: Enhancing Accuracy through Structured Reflection for Reliable Tool Interactions](https://aclanthology.org/2026.findings-acl.618/) (2026-07) | Benchmarks and trains explicit error diagnosis followed by an executable corrected tool call in failed multi-turn tool use. **Limit:** Findings of ACL 2026; evaluated on BFCL v3 and Tool-Reflection-Bench; code release is not established by the proceedings text. |

### State restoration and selective replay

| Original publication | Distinct contribution and limitations |
| --- | --- |
| [StateWise: Diagnosing and Repairing Persistent Operational State Before Agent Actions](https://arxiv.org/abs/2610.05241) (2026-10-04) | Diagnoses invalid persistent agent records using counterfactual replanning and evidence checks, repairs records and verifies subsequent proposed actions. **Limit:** 2026 preprint; 150 executable coding-agent cases. Pre-action state repair is not proof of remote effect reversal. |
| [Rollback the World, Keep the Reflection: Rollback-Induced Reflection for Long-Horizon LLM Agents](https://arxiv.org/abs/2609.18304) (2026-09-16) | Couples controlled environment rollback with retained knowledge from the failed trajectory to guide subsequent agent execution. **Limit:** 2026 preprint; evaluated in resettable interactive environments, not arbitrary third-party irreversible effects. |
| [ACRFence: Preventing Semantic Rollback Attacks in Agent Checkpoint-Restore](https://arxiv.org/abs/2603.20625) (2026-03-21) | Addresses semantically different tool requests after checkpoint restoration that can replay effects or resurrect expired authority. **Limit:** 2026 preprint; proof-of-concept and proposed replay-or-fork mitigation; no blanket protection across external providers. |
| [From Faulty Memories to Corrected Actions: Dependency-Guided Rollback Repair for Memory-Augmented Agents](https://arxiv.org/abs/2608.10502) (2026-08-11) | Tracks faulty memories through dependent actions, repairs affected persistent state and selectively replays work while preserving unaffected records. **Limit:** 2026 preprint revised October; controlled and trajectory-derived tests; residual recurrence observed after selective replay. |
| [Repair the Core, Not the Symptom: Planning-Graph Repair for Long-Horizon Agents](https://arxiv.org/abs/2607.01767) (2026-07-02) | Repairs a causally implicated core of a failed agent planning graph instead of changing one symptom or rerunning the whole graph. **Limit:** 2026 preprint revised October; planning-graph study with evaluated controlled settings, not external-effect compensation. |

### Multi-agent fault containment

| Original publication | Distinct contribution and limitations |
| --- | --- |
| [Dittany: Contribution-Guided Repair Framework for MAS Applications](https://arxiv.org/abs/2610.42144) (2026-10-30) | Locates unmet multi-agent task conditions and repairs actions or graph dependencies while retaining previously validated contributions. **Limit:** 2026 preprint; evaluated across 30 applications and six MAS frameworks. Reported task accuracy is not external transaction integrity. |
| [ARIA: Runtime Inspection and Amendment for Multi-Agent Systems](https://arxiv.org/abs/2610.20780) (2026-10-14) | Learns when and how to amend in-progress multi-agent trajectories from execution-verified correction pairs. **Limit:** 2026 preprint; author-reported repair results across selected frameworks and benchmarks, not independent external-effect verification. |
| [HiP-LR: Hierarchical Planning with Localized Failure Recovery for Long-Horizon Multi-Robot Tasks](https://aclanthology.org/2026.findings-emnlp.1835/) (2026-10) | Localizes replanning to affected groups after runtime faults so unaffected LLM-coordinated robot agents can continue. **Limit:** Findings of EMNLP 2026; RECAP-THOR failure-injection tests in a specialized multi-robot environment. |

## Duplicate/overlap review

- **LIMBO / UndoBench → Evidence-Guided Recovery and VP-CONTROL:** these additions introduce evidence-admissible completion certificates and independent-source commit-gate tests; neither replaces provider idempotency or authoritative effect ledgers.
- **Atomix / SagaLLM → Cordon and ACRFence:** Cordon stages effects before release; ACRFence addresses *semantically different* replay after restoration. They do not certify a universal rollback.
- **AgentRewind / Crab → RIR, StateWise, dependency-memory rollback and ReCore:** the new papers respectively carry forward reflection, repair operational records, track faulty memory descendants, and focus planning-graph causal cores; all have distinct state boundaries.
- **MCP-Injector / ToolMaze → AgentCheck, ToolBench-X and AgentHeal:** the additions respectively test matched intervention reruns, executable recoverable tool hazards, and legitimate alternate web-resource routing.
- **ReCoF / Sentry / RESKILL → VBL, DARC, causal harness evaluation and Wink:** compare goal-stack backtracking, diagnosis-selected interventions, rescue-vs-harm policy choice, and production coding-agent course correction.
- **DoCtOR / Async-RBench → Dittany, ARIA and HiP-LR:** contribution-graph repair, learned runtime amendment, and specialized dependency-localized multi-robot continuation.
- **Agent-Reflex → PRFC, Fission-GRPO, structured reflection:** all study explicit *tool execution error* repair; they differ in progressive rewards, on-policy error rollouts and error-to-corrected-call supervision.
- **Traverse / AgentRx → REFLECT and the REALM credit-assignment study:** patch-and-replay-supported causal localization versus a negative test of whether detection produces actual useful repair. Neither should be described as independent proof of recovered external state.

## Excluded or deferred candidates

| Publication | Screening reason |
| --- | --- |
| [SafeCommit](https://arxiv.org/abs/2608.04289) | A well-scoped **pre-action prevention/certification** mechanism in an idealized synthetic benchmark; no demonstrated recovery of a failed workflow or persistent effect. Useful adjacent reading, deferred from this exact-topic batch. |
| [Stale Does Not Mean Unsafe](https://arxiv.org/abs/2609.29522) | Commit guard precision under races is important, but chiefly preventive and overlaps existing commit-integrity papers without a distinct post-failure recovery pathway. |
| [Judged Useless, Queried Anyway](https://arxiv.org/abs/2610.06191) | Shows agents ignoring evidence to stop using failed tools, but primarily evaluates stopping behavior rather than validated recovery or state repair. |
| [ContinuityBench](https://openreview.net/forum?id=3N3BzvoLbG) | Interrupted-state continuity is relevant, but context/handoff recovery alone does not establish independently verified effects; primary forum metadata was not fully accessible in this review. |
| [Self-Evolving Agents Can Repair Failures but Struggle to Generalize](https://arxiv.org/abs/2610.22984) | Primarily addresses experience transfer/generalization, without a sufficiently distinct runtime recovery contract for this selective update. |
| [HSC-Bench](https://arxiv.org/abs/2610.36523) | Inherited-context benchmark overlaps existing checkpoint and handoff studies; distinct recovery guarantees still need closer evaluation. |
| [Recova](https://arxiv.org/abs/2510.03285) | Embodied robot-policy recovery is adjacent to this collection's main LLM tool-agent focus; separate domain review needed. |

## Reporting and implementation boundaries

For any claimed recovery rate report: initial failing condition; whether a clean execution could succeed; fault visibility; detection and error-localization accuracy; chosen recovery action; *verified* final task state; whether irreversible effects were duplicated; whether a retry could commit late; and the external contract that authorizes compensation or replay. Negative results (including no reward improvement under selective repair) should not be reframed as successful recovery.

The [CSV](../data/resources.csv) remains the source of truth; [JSON](../data/resources.json) is synchronized from it. Validation: `python scripts/validate.py --sync-json`, `python scripts/validate.py`, and `python -m unittest discover -s tests`.
