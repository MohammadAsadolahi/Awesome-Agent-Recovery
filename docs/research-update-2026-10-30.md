# Research Review — 30 October 2026

**Decision:** accept **13 distinct papers** into the previously 66-resource index (**79 resources total**). This includes the 12-paper shortlist and the accompanying *When Tools Fail, Agents Fabricate / RetryRealistic* paper, which has its own experimental contribution. The code is recorded as an optional link within the paper row, **not a second duplicate resource**.

**Scope:** detection → causal diagnosis → safe corrective choice → execution → independently observed outcome. Publication metadata, abstracts and available release pages were checked against arXiv, author/repository material and other original sources on 30 October 2026. Figures below are **authors' reported results, not independently replicated**.

## Admission tests

A paper is included only if it has: (1) a canonical original source; (2) a failure-specific mechanism, benchmark or reproducible test method; (3) distinct coverage beyond the 66 existing entries; (4) a concrete operational or evaluation implication; and (5) an explicit limitation on what success means.

**Important boundaries:** An accepted paper does **not** automatically imply released working code, peer review, production readiness, external effect reversibility, or exactly-once semantics. An arXiv preprint is called a preprint. For workshop status, distinguish a research repository's metadata from independent verification of a proceedings record.

## Selected additions

| Paper and canonical source | Why this adds distinct value | Boundary, caveat and evidence |
| --- | --- | --- |
| [Repairs for Whom?](https://arxiv.org/abs/2610.38610) · 28 Oct | Holds candidate repairs fixed and tests whether stronger evaluators choose repairs that help the **deployed executor**. | 2026 preprint; on ALFWorld/WebShop, author-reported repair-choice losses depend on evaluator/executor pairing. Not a general ranking across models. |
| [Tool-Calling Agents Under Realistic MCP Faults / MCP-Injector](https://arxiv.org/abs/2610.32555) · 23 Oct | Protocol-aware persistent, transient and intermittent MCP fault injection calibrated using public ecosystem incident evidence. [Code/data](https://gitlab.com/uniluxembourg/snt/sedan/papers/mcp-injector). | 2026 preprint whose abstract reports NeurIPS poster acceptance; 57,240 mined issue/PR threads, 1,350 experimental cells, two tested gpt-oss sizes. No universal claim that scale cannot help. |
| [Permission to Retry](https://arxiv.org/abs/2610.31916) · 22 Oct | Separates checkpoint persistence, current **permission to dispatch**, external effect evidence, and permission to reconcile. | 2026 preprint; 336 finite execution histories across native LangGraph/Temporal host configurations; [ancillary outcome data](https://arxiv.org/abs/2610.31916) is available. A bounded conformance study, not a global authorization system. |
| [Async-RBench](https://arxiv.org/abs/2610.32429) · 23 Oct | Replays asynchronous subagent arrivals and checks required updates, invariants, prohibitions and re-verification independently of final task success. [Code](https://github.com/pope8zdt/Async-RBench). | 2026 preprint; 200 executable tasks, eight scenarios, nine tested agents; author-reported 26.0% async versus 29.7% batched task success. Controlled result delivery, not arbitrary external effects. |
| [AndroidFlux](https://arxiv.org/abs/2610.34384) · 25 Oct | Aligns mobile-device checkpoint state before/at/after the first recoverable error and scores downstream corrective actions. | 2026 preprint; AndroidWorld-based controlled environment and reward-modeling experiment; not live mobile app transaction rollback. |
| [RITE](https://arxiv.org/abs/2610.27777) · 20 Oct | Compares *silent semantic corruption* with explicit errors and clean values across matched tool-using episodes. | 2026 preprint; 167 matched units, 501 conditions across nine e-commerce workflows; real-world e-commerce tool semantics not established. |
| [REVISE](https://arxiv.org/abs/2609.00643) · 1 Sep | Dependency-sensitive partial recomputation after user/plan revisions while preserving still-valid progress. | 2026 preprint; structured DAG and tested revision/commit scenarios; an online-revision problem, not a blanket crash-recovery guarantee. |
| [When Messages Go Wrong](https://arxiv.org/abs/2610.15459) · 11 Oct | Compares message faults and evidence-preserving communication paths across multi-agent topologies. [Code/artifacts](https://github.com/SonGoKu21/mas_communication). | 2026 preprint; more than 29,000 reported executions, 100 tasks; recovery depends on independent evidence paths that survive the fault. |
| [Agent-Reflex](https://arxiv.org/abs/2610.17953) · 13 Oct | A *training* approach based on tool-feedback perturbations, matched success/failure pairs and explicit reflective skills. [Code, data, weights](https://github.com/RUC-NLPIR/Agent-Reflex). | 2026 **work-in-progress** preprint; training/benchmark improvement does not imply safe external state repair. Kept as a specialized self-recovery reference, not a recommended production control. |
| [SSCBench](https://arxiv.org/abs/2610.11514) · 8 Oct | Asks whether injected-error counterevidence could reach the agent **before the first faulty use**, rather than merely appearing eventually. | 2026 preprint; 1,191 faulted executions in two τ-bench environments. This is a validity check for experiments, not an agent recovery success measure. |
| [Failure-Transparent Agents](https://arxiv.org/abs/2609.35732) · 28 Sep | Holds failed-tool observations fixed and evaluates **unsupported success claims** versus an evidence-structured status contract. | 2026 preprint; author-reported 3,600 annotated responses, false-success 22.8% baseline vs 0.8% under a bundled contract in blocked-task cases. Accuracy of reporting ≠ repaired task. |
| [Loud Failures, Quiet Failures](https://arxiv.org/abs/2610.10062) · 7 Oct | Separates fault noticing, replanning, repeated calls and recovered outcomes; checks variation against clean-run stochasticity. | 2026 preprint; 1,920 trials over 24 tasks; one task outcome is not necessarily a fault-caused difference. |
| [When Tools Fail, Agents Fabricate / RetryRealistic](https://openreview.net/forum?id=HLCpv21u07) · Oct | Reproducible real filesystem, SQLite and local HTTP fault testing; reports correct answer, fabricated success and honest failure. [Released toolkit](https://github.com/Kingsford-Group/RetryRealistic). | Described by authors as a **NeurIPS 2026 workshop** paper; 30 tasks, nine fault types and controlled sandbox. Explicit-error-gated monitor misses faults that never raise an error. OpenReview may require authentication. |

## Selection logic and contrast with existing work

- **ToolMaze / AgentChaosBench → MCP-Injector, RITE, Loud/Quiet, RetryRealistic:** the new group adds incident-informed MCP persistence patterns, paired silent semantic faults and **honest-failure vs fabrication** scoring. Avoid calling all four a single homogeneous tool-failure benchmark.
- **ParaRecover / distributed recovery → Async-RBench, REVISE:** the new pair covers late/stale subagent results and validity-preserving *online revisions*, respectively; neither proves third-party atomic transactions.
- **AgentRewind / CUA-Recovery / GUI-RobustEval → AndroidFlux:** extends aligned recovery evaluation to **mobile UI state** and explicitly separates clean-task competence from checkpoint recovery.
- **Sentry / RESKILL → Agent-Reflex:** the latter trains reflective behavior with released artifacts; it is not an intervention layer or runtime effect verifier.
- **LIMBO / UndoBench → Permission to Retry:** moves beyond effect observability and idempotency to permission changes between dispatch, crash recovery and reconciliation.
- **Traverse / same-winners benchmark caution → Repairs for Whom?, SSCBench:** tests **executor-specific repair value** and **timely counterevidence exposure**; both constrain how results should be interpreted.
- **EffectMatch / existing independent verification → Failure-Transparent Agents, RetryRealistic:** distinguish *real-world postconditions* from whether a final response is justified by observed evidence.

## Suggested benchmark reporting additions

For every evaluated recovery attempt, record the **deployed executor model**, repair-selection evaluator, fault-exposure time, counterevidence-first-visible time, counterevidence-first-used time, main/subagent result-delivery order, and permissions at original dispatch versus retry. Report **actual external effect ledger**, verified task success, conditional recovery among clean-run-capable tasks, unsupported success/fabrication, and safe abstention as different columns.

A small but critical example: "tool call completed" is not proof that its observation is correct; "no result found" is not proof a prior write cannot still commit; and "I completed the task" is not evidence of completion. Do not collapse these into a single recovery rate.

## Deferred after review

- A broad extension into **generic reflective training** and prompt engineering was deferred. [Agent-Reflex](https://arxiv.org/abs/2610.17953) is admitted only for its targeted tool-noise and user-correction studies; its larger model-training ecosystem is not separately indexed.
- [HSC-Bench](https://arxiv.org/abs/2610.36523) is a plausible next addition, but inherited handoff context overlaps CUA-Recovery/Async-RBench until distinctive recovery metrics and artifact release are more clearly checked.
- [Returning to Development States](https://arxiv.org/abs/2610.13841) overlaps AgentRewind/Crab; revisit if it demonstrates an otherwise missing restoration guarantee.
- [Self-Evolving Agents Can Repair Failures but Struggle to Generalize](https://arxiv.org/abs/2610.22984) is related to transfer/generalization; add only when there is a distinct, failure-specific recovery protocol.
- [Understanding Communication Failures in Multi-Agent LLM Systems](https://arxiv.org/abs/2610.32060) overlaps the larger causal communication-fault and intervention study above; not needed for the present selective update.

No claim is made that this is an exhaustive systematic literature search or that any experimental result was independently reproduced. The [catalog](../data/resources.csv) is the editable source of truth; [JSON](../data/resources.json) is synchronized from it. Run `python scripts/validate.py --sync-json` and the unit tests before publishing.
