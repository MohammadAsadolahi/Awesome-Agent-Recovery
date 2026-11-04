# Comprehensive curation audit — 4 November 2026

**Decision:** Reduce the active catalog from **131 mixed entries to 57 research publications**. Remove **74** entries: 56 research papers that no longer meet the stricter directness/uniqueness bar, and 18 non-paper catalog entries. This is an **editorial selection**, not a claim that excluded research is invalid or of low scholarly quality.

The former entries and earlier research reviews remain recoverable in Git history. **The active index is strictly original research publications**, not tools, tutorials, broad reliability collections, general framework docs, or companion code entries.

## Purpose and scope

**Awesome Agent Recovery** catalogs original research into **failures of tool-using language-model agents and methods for restoring useful, verified task progress**. It includes bounded retry and intervention, controlled rollback or compensation, recovery-specific evaluation, and a small number of exceptionally informative failure-attribution foundations. It does **not** attempt to be a complete bibliography for LLM agents, prompt engineering, agent safety, general reliability, AIOps, or robotics.

### Explicit screening protocol

Each of the 131 records was independently considered against the repository's purpose and the other entries.

1. **Publication gate:** original research paper/preprint with an inspectable primary source; code and framework documentation belong in the paper's optional supporting `code` link.
2. **Directness gate:** does the study investigate a *failed agent* and a corrective action, a recoverability-specific benchmark, a measured recovery outcome, or a necessary recovery boundary (for example whether a remote write was safely applied)? Generic task success is not sufficient.
3. **Evidence gate:** reported controlled failures, paired comparisons, reproducible environments, causal interventions, independent effect checks, or an unusually rigorous field/benchmark study. Venue is useful evidence, **not** a guarantee of impact; 2026 preprints are not presumed peer-reviewed.
4. **Distinctiveness gate:** if multiple papers cover substantially the same benchmark/fault, keep the work with the strongest distinct methodology, evaluation, or operational implications rather than all variants.
5. **Honest boundary:** distinguish diagnosis, recovery proposal, controlled rerun, verified external state and safe refusal. Papers with a negative recovery result may be **high-priority keeps** when they actually test the intervention.

**Narrow exception:** [MAST](https://papers.nips.cc/paper_files/paper/2025/hash/b1041e52d3be19f0a9bc491657488e4a-Abstract-Datasets_and_Benchmarks_Track.html) is retained as one directly agent-failure-specific taxonomy and benchmark anchor because its annotated multi-agent fault classes help define recoverable failure states. It is **not** described as a demonstrated recovery method.

## Results

| Metric | Before | After |
| --- | ---: | ---: |
| Total active catalog records | 131 | 57 |
| Original research papers | 113 | 57 |
| Non-paper records (survey, code, runtime docs, lists) | 18 | 0 |
| Resources removed | — | 74 |
| Companion code counted separately | Some | None |

### Reason counts (exclusive editorial buckets)

| Removal reason | Entries |
| --- | ---: |
| Non-publication / duplicate companion entry | 17 |
| Survey or general agent foundation | 3 |
| Diagnosis / detection without a sufficiently distinct recovery outcome | 14 |
| Robustness, security, prevention, or reporting rather than demonstrated task recovery | 13 |
| Peripheral domain / general training rather than current failed-task recovery | 9 |
| Redundant or lower distinctive evidence versus retained recovery works | 18 |

A source may fail several tests; it is assigned **one primary removal reason** below so every removal is auditable.

## Kept: 57 directly relevant papers

| ID | Research contribution that merits retention |
| --- | --- |
| `dittany-contribution-repair` | [Dittany: Contribution-Guided Repair Framework for MAS Applications](https://arxiv.org/abs/2610.42144) — Locates unmet multi-agent task conditions and repairs actions or graph dependencies while retaining previously validated contributions. |
| `evidence-guided-recovery` | [Evidence-Guided Recovery for AI Agents with Ambiguous Tool Outcomes and Partial Execution](https://arxiv.org/abs/2610.41453) — Plans safe continuation after ambiguous tool outcomes using publicly supported effect states, provider contracts and independent replay certificates. |
| `verify-backtrack-loop` | [Verify--Backtrack Loop: Structured Precondition Recovery for Long-Horizon Language Agents](https://arxiv.org/abs/2610.41564) — Uses goal-stack verification and typed failure attribution to trigger explicit retry, subgoal updates or backtracking after unmet prerequisites. |
| `agentheal-access-recovery` | [AgentHeal: Evaluating Goal-Preserving Resource Recovery of Web Agents under Access Barriers](https://arxiv.org/abs/2610.39234) — Benchmarks web-agent recovery from blocked links, authorization walls and rate limits while preserving the original authorized goal. |
| `replayrca-causal-repair` | [ReplayRCA: Measuring Post-hoc Diagnosis and Live Oversight of Agent Failures by Counterfactual Replay](https://arxiv.org/abs/2610.41025) — Restores failed LLM agent execution to the selected step and tests whether a proposed corrected action improves outcome against a placebo replay. |
| `evaluator-executor-mismatch` | [Repairs for Whom? Evaluator-Executor Mismatch in Selecting Repairs for Failed LLM Agents](https://arxiv.org/abs/2610.38610) — Tests whether candidate repairs selected by a different evaluator improve the deployed agent's own rollouts. |
| `recof` | [When to Intervene? An Empirical Study of Errors and Self-Recovery in LLM Agents](https://arxiv.org/abs/2610.36471) — Analyzes natural self-recovery and predicts when external intervention is necessary. |
| `permission-to-retry` | [Permission to Retry: A Study of Authorization and Recovery in AI Agent Workflows](https://arxiv.org/abs/2610.31916) — Examines whether recovering workflows still have authority to dispatch reconcile or retry an uncertain external effect. |
| `cua-recovery` | [CUA-Recovery: Benchmarking Error Recovery in Long-Horizon Computer-Use Agents](https://arxiv.org/abs/2610.27645) — Benchmarks recognition and repair of inherited desktop errors over persistent workflows. |
| `retrace-cua-recovery` | [Lost in Recovery: Demystifying Recovery Behavior of Computer-Use Agents via Goal-Oriented Action Replay](https://arxiv.org/abs/2610.27954) — Introduces ReTrace and transition-consistent recovery scoring for computer-use agents restoring GUI state after controlled mistakes. |
| `rite-silent-errors` | [RITE: Evaluating End-to-End Resilience to Silent Tool Errors in E-Commerce Agentic Systems](https://arxiv.org/abs/2610.27777) — Contrasts plausible incorrect tool values with correct values and explicit failures to measure recognition verification and end-task recovery. |
| `aria-runtime-amendment` | [ARIA: Runtime Inspection and Amendment for Multi-Agent Systems](https://arxiv.org/abs/2610.20780) — Learns when and how to amend in-progress multi-agent trajectories from execution-verified correction pairs. |
| `beliefweaver-failure-recovery` | [Failure Recovery via Belief Updates and World Modeling for Long-Horizon Agents](https://arxiv.org/abs/2610.18082) — BELIEFWEAVER retains evidence across failing attempts and checkpoints and uses belief updates plus prospective world modeling to guide repair. |
| `undobench` | [UndoBench: Separating Task Competence from Recovery Capability in Tool-Using AI Agents](https://arxiv.org/abs/2610.05622) — Measures conditional recovery separately from nominal task competence under phased enterprise write failures. |
| `sentry` | [Sentry: Learning to Recover from LLM Agent Failures at Test Time](https://arxiv.org/abs/2610.02994) — Conditionally retrieves failure lessons and verifies repaired execution. |
| `agentdebugx` | [AgentDebugX: An Open-Source Toolkit for Failure Observability, Attribution, and Recovery in LLM Agents](https://aclanthology.org/2026.emnlp-demos.52/) — Links evidence-grounded failure diagnosis to bounded recovery proposals and controlled reruns. |
| `credit-assignment-to-repair` | [From Credit Assignment to Repair: A Leakage-Controlled Diagnostic Study of Tool-Using Agents](https://aclanthology.org/2026.realm-1.15/) — Tests whether failure localization causes useful selective tool-agent repair and reports a reproducible negative result for its selected intervention gate. |
| `cuadebug` | [CUADebug: Diagnosing and Repairing Computer-Use Agent Failures](https://aclanthology.org/2026.findings-emnlp.530/) — Inspects paired screenshots and actions for causal GUI errors and conditions re-execution on structured diagnosis. |
| `doctor` | [Finding Where the Buck Stops: An Automated Failure Attribution-Based Reflection Framework for Multi-Agent Collaboration](https://aclanthology.org/2026.emnlp-main.335/) — DoCtOR targets reflection and correction at the decisive error agent and step instead of the entire team. |
| `oracle-state` | [Causal Decomposition of LLM Agent Failure via Oracle-State Intervention](https://aclanthology.org/2026.realm-1.6/) — Tests whether replacing polluted context with oracle state actually rescues failed long-horizon agents. |
| `pararecover` | [ParaRecover: A Process-Level Benchmark for Error Localization and Recovery in Parallel Tool-Use Agents](https://aclanthology.org/2026.emnlp-main.975/) — Evaluates cascading failure diagnosis and replanning across dependent parallel tool-call branches. |
| `prfc-tool-recovery` | [PRFC: Learning Progressive Recovery from Function Calling Errors for Tool-Using LLMs](https://aclanthology.org/2026.findings-emnlp.1762/) — Trains successive corrective tool calls with progress-aware rewards after observed function-calling failures. |
| `recoveragent` | [RecoverAgent: Intent-Preserving Recovery from Indirect Prompt Injection in Tool-using LLM Agents](https://aclanthology.org/2026.findings-emnlp.830/) — Rewrites unsafe injected intermediate responses to resume permitted user goals after threat detection. |
| `reskill` | [RESKILL: Explicit Failure Attribution and Structured Repair for Interactive Language Agents](https://aclanthology.org/2026.emnlp-main.2024/) — Keeps structured failure hypotheses and retest feedback to choose and revise agent skill repairs. |
| `toolmisusebench` | [ToolMisuseBench: An Offline Deterministic Benchmark for Tool Misuse and Recovery in Agentic Systems](https://aclanthology.org/2026.realm-1.28/) — Measures deterministic fault-conditioned recovery with typed recoverability and output-grounded scoring. |
| `agent-error-dataset` | [Agent Error Dataset: Scaling 50,000 Error--Diagnosis Pairs for Failure Analysis and Error-Aware Post-Training](https://arxiv.org/abs/2609.40111) — Pairs error diagnoses with candidate corrections and matched replay from common checkpoints when available. |
| `limbo` | [Where Does Exactly-Once Live? Model, Harness, and Tool-Contract Effects on Duplicate Side Effects in LLM Agents](https://arxiv.org/abs/2609.29095) — LIMBO injects late commits, duplicate delivery and partial batches; effect ledgers expose unsafe retries. |
| `rir-rollback-reflection` | [Rollback the World, Keep the Reflection: Rollback-Induced Reflection for Long-Horizon LLM Agents](https://arxiv.org/abs/2609.18304) — Couples controlled environment rollback with retained knowledge from the failed trajectory to guide subsequent agent execution. |
| `traverse` | [Locating Hidden Failures Makes Long-Horizon Agents More Reliable](https://arxiv.org/abs/2609.17930) — Traverse labels mistakes and Scout predicts first-error locations. |
| `agent-tool-boundary-anomalies` | [When Tool Calls Succeed but Workflows Fail: Anomalies at the Agent-Tool Boundary](https://arxiv.org/abs/2609.15397) — Classifies external-effect anomalies that can survive tool success and derives reconciliation and transaction contract requirements at the agent-tool boundary. |
| `agentrewind` | [AgentRewind: Recoverable Execution for Long-Horizon LLM Agents](https://arxiv.org/abs/2608.14380) — Aligns agent-context and environment-state checkpoints for resumable execution. |
| `bench2robust` | [Retry, Switch, or Abstain? Learning Strategy-Aware Tool-Use Policies via Controlled Error Injection](https://arxiv.org/abs/2608.11977) — BENCH2ROBUST distinguishes retry switching tools and safe stopping under controlled failure solvability. |
| `dependency-memory-rollback` | [From Faulty Memories to Corrected Actions: Dependency-Guided Rollback Repair for Memory-Augmented Agents](https://arxiv.org/abs/2608.10502) — Tracks faulty memories through dependent actions, repairs affected persistent state and selectively replays work while preserving unaffected records. |
| `failfast-restartsmart` | [Fail-Fast, Restart-Smart: Early Failure Prediction and Restart for SWE Agentic Tasks](https://arxiv.org/abs/2608.03222) — Uses prefix-only early-failure monitoring and a fresh same-policy restart that can selectively reuse the interrupted code diff. |
| `real-time-repair` | [Real-Time Detection and Repair of LLM Agent Failures](https://arxiv.org/abs/2608.02464) — Combines step telemetry and deterministic verification with repair experiments. |
| `memtx` | [MemTX: Transactional Belief Commit for Stateful Agent Memory](https://arxiv.org/abs/2607.23929) — Stages evidence-backed shared-memory writes and triggers cascading repair after a belief is retracted. |
| `agentcheck-mcp-workbench` | [AgentCheck: A Reproduce-Intervene-Mitigate Workbench for LLM Agents over MCP](https://arxiv.org/abs/2607.11098) — Reproduces MCP tool faults and reruns agents under matched failures to test whether specific mitigations actually recover outcomes. |
| `air` | [AIR: Improving Agent Safety through Incident Response](https://proceedings.mlr.press/v306/xiao26n.html) — Introduces incident detection containment recovery and future guardrail synthesis inside agent execution. |
| `fission-grpo-tool-recovery` | [Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors](https://aclanthology.org/2026.acl-long.1880/) — Turns execution errors into on-policy training examples and resampled correction rollouts for multi-turn tool-call recovery. |
| `gui-robusteval` | [Recovering Policy-Induced Errors: Benchmarking and Trajectory Synthesis for Robust GUI Agents](https://proceedings.mlr.press/v306/bu26b.html) — Introduces GUI-RobustEval with executable wrong-action recovery cases and RoTS recovery-trajectory synthesis. |
| `structured-reflection-tool-errors` | [Failure makes the agent stronger: Enhancing Accuracy through Structured Reflection for Reliable Tool Interactions](https://aclanthology.org/2026.findings-acl.618/) — Benchmarks and trains explicit error diagnosis followed by an executable corrected tool call in failed multi-turn tool use. |
| `mnemosyne-agentic-transactions` | [Mnemosyne: Agentic Transaction Processing for Validating and Repairing AI-generated Workflows](https://arxiv.org/abs/2607.00269) — Uses deterministic admission, persistent transition logs, dependency-safe compensation and bounded reactive repair for proposed workflow changes. |
| `cordon-semantic-transactions` | [Cordon: Semantic Transactions for Tool-Using LLM Agents](https://arxiv.org/abs/2606.17573) — Stages agent tool effects in task-scoped semantic transactions with reversible shadow state, validation and recovery metadata. |
| `harnessfix-failure-repair` | [From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws](https://arxiv.org/abs/2606.06324) — Maps failed agent traces to faulty runtime-harness components and applies scoped patches with regression-aware validation. |
| `toolmaze` | [When Tools Fail: Benchmarking Dynamic Replanning and Anomaly Recovery in LLM Agents](https://arxiv.org/abs/2606.05806) — ToolMaze tests explicit or implicit transient or permanent tool perturbations. |
| `delact` | [DelAct: A Replayable Boundary Runtime for Auditable and Governed LLM Agent Workflows](https://doi.org/10.1109/IWQoS70441.2026.11661202) — Separates deliberation actuation and append-only logging for replay idempotent execution and compensation. |
| `tracefix` | [TraceFix: Repairing Agent Coordination Protocols with TLA+ Counterexamples](https://doi.org/10.1145/3786335.3813159) — Repairs LLM-generated multi-agent coordination protocols using TLA+ counterexamples and enforces topology conformance at runtime. |
| `probe-structured-recovery` | [Debugging the Debuggers: Failure-Anchored Structured Recovery for Software Engineering Agents](https://arxiv.org/abs/2605.08717) — PROBE gates recovery guidance on structured telemetry and grounded diagnosis for subsequent repair attempts. |
| `rac` | [Robust Agent Compensation (RAC): Teaching AI Agents to Compensate](https://arxiv.org/abs/2605.03409) — Studies log-based compensation layers that track agent effects and support corrective execution. |
| `crab` | [Crab: A Semantics-Aware Checkpoint/Restore Runtime for Agent Sandboxes](https://arxiv.org/abs/2604.28138) — Uses OS-effect inspection to make agent sandbox checkpointing more selective. |
| `acrfence-semantic-rollback` | [ACRFence: Preventing Semantic Rollback Attacks in Agent Checkpoint-Restore](https://arxiv.org/abs/2603.20625) — Addresses semantically different tool requests after checkpoint restoration that can replay effects or resurrect expired authority. |
| `wink-agent-misbehaviors` | [Wink: Recovering from Misbehaviors in Coding Agents](https://arxiv.org/abs/2602.17037) — Monitors coding-agent drift, loops and tool failures and applies targeted runtime course-correction interventions. |
| `atomix` | [Atomix: Timely, Transactional Tool Use for Reliable Agentic Workflows](https://arxiv.org/abs/2602.14849) — Uses progress-aware resource frontiers to gate commits and distinguish bufferable reversible and irreversible effects. |
| `mast-failure-taxonomy` | [Why Do Multi-Agent LLM Systems Fail?](https://papers.nips.cc/paper_files/paper/2025/hash/b1041e52d3be19f0a9bc491657488e4a-Abstract-Datasets_and_Benchmarks_Track.html) — Introduces MAST taxonomy and MAST-Data of 1600-plus annotated multi-agent traces to distinguish design misalignment and verification failures. |
| `agentdebug-original` | [Where LLM Agents Fail and How They can Learn From Failures](https://arxiv.org/abs/2509.25370) — Introduces AgentErrorTaxonomy and AgentErrorBench with root-cause targeted debugging feedback and iterative reruns. |
| `sagallm` | [SagaLLM: Context Management, Validation, and Transaction Guarantees for Multi-Agent LLM Planning](https://doi.org/10.14778/3750601.3750611) — Applies saga-style compensation persistent context and independent validation to multi-agent planning. |
| `recovery-bench` | [Recovery-Bench: Evaluating Agentic Recovery from Mistakes](https://openreview.net/forum?id=8FZRnDgDxq) — Evaluates agent recovery from prior failed trajectories and polluted context rather than clean starts. |

**Retained negative/diagnosis-to-intervention evidence:** [Oracle-State Intervention](https://aclanthology.org/2026.realm-1.6/), [From Credit Assignment to Repair](https://aclanthology.org/2026.realm-1.15/), [ReplayRCA](https://arxiv.org/abs/2610.41025), and [Repairs for Whom?](https://arxiv.org/abs/2610.38610) are relevant because they experimentally test when a plausible corrective action helps or fails. They should not be confused with mere error labeling.

## Removed: all 74 entries and the primary curation reason

| ID | Excluded work | Editorial reason |
| --- | --- | --- |
| `monitor-decision-value` | Monitor Accuracy Isn't the Answer: A Decision-Value Framework for Evaluating AI Agent Restart Monitors | Redundant or lower distinctive evidence versus retained recovery works |
| `androidflux` | AndroidFlux: Evaluating and Reward Modeling Failure Recovery Capabilities in Mobile Use Multimodal Agents | Peripheral domain / general training rather than current failed-task recovery |
| `async-rbench` | Async-RBench: Benchmarking Asynchronous Task Execution in LLM Agents | Peripheral domain / general training rather than current failed-task recovery |
| `mcp-injector` | Tool-Calling LLM Agents Under Realistic MCP Faults: Scale Does Not Purchase Fault Tolerance | Redundant or lower distinctive evidence versus retained recovery works |
| `episem` | EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence | Robustness, security, prevention, or reporting rather than demonstrated task recovery |
| `self-direction` | Don't Forget What You Just Learned: Self-Directed Repair Turns Agent Mistakes Into Lasting Lessons | Peripheral domain / general training rather than current failed-task recovery |
| `backupper` | Back Up Before You Regret: Measuring Backup Awareness and Automating Backup in Coding Agents | Robustness, security, prevention, or reporting rather than demonstrated task recovery |
| `gracebench-gui-diagnosis` | How GUI Agents Fail: GraceBench for Execution Stability Diagnosis | Diagnosis / detection without a sufficiently distinct recovery outcome |
| `agent-reflex-training` | Agent-Reflex: Teaching Language Agents to Act Reflectively | Peripheral domain / general training rather than current failed-task recovery |
| `trap-tool-result-replay` | TRAP: Tool-result Replay Attack for Probing Misbinding in LLM Agents | Robustness, security, prevention, or reporting rather than demonstrated task recovery |
| `messages-go-wrong` | When Messages Go Wrong: Understanding Communication Faults in LLM-Based Multi-Agent Systems | Robustness, security, prevention, or reporting rather than demonstrated task recovery |
| `retrybench-permission` | RetryBench: Separating Retry Permission from Recovery Outcomes in GPT Tool Use | Redundant or lower distinctive evidence versus retained recovery works |
| `hardware-agent-faults` | How Do Hardware Faults Manifest Differently in LLM Agents? | Robustness, security, prevention, or reporting rather than demonstrated task recovery |
| `sscbench` | SSCBench: Evaluating the Evidential Validity of Fault-Injection Tests for Tool-Using LLM Agents | Diagnosis / detection without a sufficiently distinct recovery outcome |
| `loud-quiet-failures` | Loud Failures, Quiet Failures: Fault Detection and Recovery in Tool-Using Language Model Agents | Redundant or lower distinctive evidence versus retained recovery works |
| `statewise-operational-repair` | StateWise: Diagnosing and Repairing Persistent Operational State Before Agent Actions | Redundant or lower distinctive evidence versus retained recovery works |
| `defa` | DeFA: Dependency-Guided Failure Attribution for LLM Agents | Diagnosis / detection without a sufficiently distinct recovery outcome |
| `recova` | Recova: Agent-Guided Failure Recovery for Autonomous Robotic Manipulation | Peripheral domain / general training rather than current failed-task recovery |
| `safety-self-improvement` | Safety Must Survive Self-Improvement: Why Failures Persist and How Agents Recover | Robustness, security, prevention, or reporting rather than demonstrated task recovery |
| `agentrx` | AgentRx: Diagnosing AI Agent Failures from Execution Trajectories | Diagnosis / detection without a sufficiently distinct recovery outcome |
| `edge-multi-error-attribution` | EDGE: Error Dependency Graph-Guided Multi-Error Attribution in Multi-Agent LLM Systems | Diagnosis / detection without a sufficiently distinct recovery outcome |
| `hiplr-local-recovery` | HiP-LR: Hierarchical Planning with Localized Failure Recovery for Long-Horizon Multi-Robot Tasks | Peripheral domain / general training rather than current failed-task recovery |
| `lastcq` | What Drives Recovery in Agentic Text-to-Cypher? LAST-CQ: An LLM Agent Self-Refinement Framework | Peripheral domain / general training rather than current failed-task recovery |
| `retryrealistic-fabrication` | When Tools Fail, Agents Fabricate: Silent Failure and Verification-First Oversight in Tool-Using LLM Agents | Robustness, security, prevention, or reporting rather than demonstrated task recovery |
| `trajdebug` | TRAJDEBUG: Tracing Error Lifecycle to Identify Critical Failures in Long-Horizon Agent Trajectories | Diagnosis / detection without a sufficiently distinct recovery outcome |
| `causal-harness-recovery` | When Harnesses Lose the Signal: Causal Evaluation of Recovery in LLM Agents | Redundant or lower distinctive evidence versus retained recovery works |
| `fault-tolerant-budget-conservation` | Fault-Tolerant Budget Conservation in Distributed Multi-Agent Delegation | Redundant or lower distinctive evidence versus retained recovery works |
| `failure-transparent-agents` | Failure-Transparent Agents: Benchmarking Post-Failure Reporting in Tool-Using Language Models | Robustness, security, prevention, or reporting rather than demonstrated task recovery |
| `same-winners` | Same Winners, Different Success Rates: Evaluating How LLM Agents Recover from Failures | Redundant or lower distinctive evidence versus retained recovery works |
| `effectmatch` | Beyond Approved Actions: Runtime Validation of Persistent Outcomes in Agent Workflows | Robustness, security, prevention, or reporting rather than demonstrated task recovery |
| `meshheal` | MeshHeal: Two-Timescale Self-Healing for Gray Failures in Decentralized LLM Agent Networks | Redundant or lower distinctive evidence versus retained recovery works |
| `self-healing-harness` | Self-Healing Harness for Runtime Oversight of Agent Self-Modification | Robustness, security, prevention, or reporting rather than demonstrated task recovery |
| `collective-control` | Collective Loss of Control in LLM Agent Systems: An Epidemic Account of Mutation, Contagion, and Recovery | Robustness, security, prevention, or reporting rather than demonstrated task recovery |
| `vp-control-commit-gates` | Engineering Reliable Commit Gates for Agentic AI: Cost-Aware Verification Portfolios under Common-Mode Data Failures | Robustness, security, prevention, or reporting rather than demonstrated task recovery |
| `revise-online-workflows` | REVISE: Validity-Guided Recovery for Online Revisions in Agent Workflows | Peripheral domain / general training rather than current failed-task recovery |
| `agent-error-simulator` | Agent Error Simulator: Fault Injection for Testing Recovery in Agentic Workflows | Redundant or lower distinctive evidence versus retained recovery works |
| `emergent-repair` | Localizing Emergent Failures in Agentic AI: Recovering Minimal Repair Families via Counterfactual Replay | Redundant or lower distinctive evidence versus retained recovery works |
| `safe-to-resume-rollback` | Safe to Resume? Breaking Execution Continuity of Agent Execution via Rollback | Redundant or lower distinctive evidence versus retained recovery works |
| `darc-selective-recovery` | Diagnosis Before Recovery: Turning Agent Failures into Selective Self-Correction | Redundant or lower distinctive evidence versus retained recovery works |
| `agentchaosbench` | When Agentic Executions Fail: Detecting and Localizing Runtime Faults from Telemetry | Diagnosis / detection without a sufficiently distinct recovery outcome |
| `verified-tool-calls` | Verified Tool Calls Improve LLM Agent Reliability Under Non-Atomic Failures | Redundant or lower distinctive evidence versus retained recovery works |
| `recore-planning-graph` | Repair the Core, Not the Symptom: Planning-Graph Repair for Long-Horizon Agents | Redundant or lower distinctive evidence versus retained recovery works |
| `traceelephant` | Seeing the Whole Elephant: A Benchmark for Failure Attribution in LLM-based Multi-Agent Systems | Diagnosis / detection without a sufficiently distinct recovery outcome |
| `toolbenchx-unreliable-tools` | Beyond Function Calling: Benchmarking Tool-Using Agents under Tool-Environment Unreliability | Redundant or lower distinctive evidence versus retained recovery works |
| `src` | Speculative Rollback Correction for Quality-Diverse Web Agent Imitation | Peripheral domain / general training rather than current failed-task recovery |
| `reflect-intervention-attribution` | REFLECT: Intervention-Supported Error Attribution for Silent Failures in LLM Agent Traces | Diagnosis / detection without a sufficiently distinct recovery outcome |
| `selfhealing-orchestrators` | Self-Healing Agentic Orchestrators for Reliable Tool-Augmented Large Language Model Systems | Redundant or lower distinctive evidence versus retained recovery works |
| `verifymas` | VerifyMAS: Hypothesis Verification for Failure Attribution in LLM Multi-Agent Systems | Diagnosis / detection without a sufficiently distinct recovery outcome |
| `agentforesight` | AgentForesight: Online Auditing for Early Failure Prediction in Multi-Agent Systems | Diagnosis / detection without a sufficiently distinct recovery outcome |
| `mpbench` | Rethinking Failure Attribution in Multi-Agent Systems: A Multi-Perspective Benchmark and Evaluation | Diagnosis / detection without a sufficiently distinct recovery outcome |
| `agenttrace-causal` | AgentTrace: Causal Graph Tracing for Root Cause Analysis in Deployed Multi-Agent Systems | Diagnosis / detection without a sufficiently distinct recovery outcome |
| `reliabilitybench` | ReliabilityBench: Evaluating LLM Agent Reliability Under Production-Like Stress Conditions | Robustness, security, prevention, or reporting rather than demonstrated task recovery |
| `dover` | DoVer: Intervention-Driven Auto Debugging for LLM Multi-Agent Systems | Redundant or lower distinctive evidence versus retained recovery works |
| `agentfail` | Diagnosing Failure Root Causes in Platform-Orchestrated Agentic Systems: Dataset, Taxonomy, and Benchmark | Diagnosis / detection without a sufficiently distinct recovery outcome |
| `reflexion` | Reflexion: Language Agents with Verbal Reinforcement Learning | Survey or general agent foundation |
| `react` | ReAct: Synergizing Reasoning and Acting in Language Models | Survey or general agent foundation |
| `trajectory-survey` | A Survey for LLM Agent Trajectory Analysis: From Failure Attribution to Enhancement | Survey or general agent foundation |
| `cua-code` | CUA-Recovery reference repository | Non-publication / duplicate companion entry |
| `toolmaze-code` | ToolMaze reference code | Non-publication / duplicate companion entry |
| `sentry-code` | Sentry research repository | Non-publication / duplicate companion entry |
| `temporal` | Temporal Durable AI | Non-publication / duplicate companion entry |
| `inngest` | Inngest Durable Agents | Non-publication / duplicate companion entry |
| `dbos` | DBOS Hacker News Research Agent | Non-publication / duplicate companion entry |
| `restate` | Restate | Non-publication / duplicate companion entry |
| `langgraph` | LangGraph Persistence | Non-publication / duplicate companion entry |
| `temporal-cookbook` | Temporal AI Cookbook | Non-publication / duplicate companion entry |
| `pydantic` | Pydantic AI Durable Execution | Non-publication / duplicate companion entry |
| `openai-sessions` | OpenAI Agents SDK Sessions | Non-publication / duplicate companion entry |
| `openai-tracing` | OpenAI Agents API Tracing | Non-publication / duplicate companion entry |
| `related-reliability` | Awesome Agent Reliability | Non-publication / duplicate companion entry |
| `related-trajectory` | Awesome Agent Trajectory | Non-publication / duplicate companion entry |
| `related-agentops` | Awesome AgentOps | Non-publication / duplicate companion entry |
| `related-harness` | Awesome Agent Harness | Non-publication / duplicate companion entry |
| `related-trajectory-analysis` | Awesome LLM Agent Trajectory Analysis | Non-publication / duplicate companion entry |

## Difficult calls and safeguards against over-pruning

- **MAST vs other diagnosis taxonomies:** Keep one strongly grounded 1,600+-trace NeurIPS taxonomy anchor for selecting actual agent fault classes. Drop diagnosis-only variants whose evaluation ends at attribution without a stronger tested recovery path.
- **ReTrace vs adjacent GUI benchmarks:** Keep [CUA-Recovery](https://arxiv.org/abs/2610.27645), [ReTrace](https://arxiv.org/abs/2610.27954), [CUADebug](https://aclanthology.org/2026.findings-emnlp.530/) and [GUI-RobustEval](https://proceedings.mlr.press/v306/bu26b.html) for **different** things: inherited bad states; transition-consistent restoration; causal repair-guided reruns; and executable policy-error correction.
- **LIMBO vs simpler verify-before-retry studies:** Keep [LIMBO](https://arxiv.org/abs/2609.29095) because it explicitly tests *late in-flight commits* and when read-back alone cannot guarantee exactly-once; the simpler wrapper tests are instructive but add less unique coverage.
- **Controlled transaction proposals:** Retain [Atomix](https://arxiv.org/abs/2602.14849), [SagaLLM](https://doi.org/10.14778/3750601.3750611), [RAC](https://doi.org/10.1145/3786335.3813141), [Cordon](https://arxiv.org/abs/2606.17573), [DelAct](https://doi.org/10.1109/IWQoS70441.2026.11661202), and [Mnemosyne](https://arxiv.org/abs/2607.00269) because their effect boundaries (compensation, shadow state, commit, durable records) **differ**. None guarantees universal rollback.
- **High-impact but off-scope works:** [ReAct](https://arxiv.org/abs/2210.03629), [Reflexion](https://arxiv.org/abs/2303.11366), the agent-trajectory survey and general framework documentation are excluded despite being useful elsewhere. Venue, historical importance, or popularity alone is insufficient.
- **Embodied, mobile and narrow application works:** Valid robot-specific, mobile-only and text-to-Cypher recovery publications were omitted for **domain concentration**, not because their methods are invalid. The repository now centers tool-using LLM and multi-agent *software* workflows.
- **Security/safety work:** The retained [AIR](https://proceedings.mlr.press/v306/xiao26n.html), [RecoverAgent](https://aclanthology.org/2026.findings-emnlp.830/) and [ACRFence](https://arxiv.org/abs/2603.20625) each implement or explicitly test recovery/mitigation **after an agent execution incident**. Broad prevention-only or mere false-success reporting papers were removed.

## Source integrity

Primary research records were compared with original publisher/arXiv abstracts, and key disputed overlaps were checked more deeply. No independent reproduction of 57 papers is claimed. The audit is a **selective expert curation**, not a formal systematic meta-analysis, and recent citation counts are too unstable to serve as an impact threshold.

For new PRs, [CONTRIBUTING.md](../CONTRIBUTING.md) now enforces the above criteria. The **single active catalog** is [resources.csv](../data/resources.csv); [JSON](../data/resources.json) is its derived mirror. Prior rejected items can be revisited if they supply new recovery-specific evidence.
