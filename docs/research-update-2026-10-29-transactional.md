# Research update: transactional recovery, fault injection and safe resumption

**Curated:** 29 October 2026 · **Added:** 22 distinct research papers · **Catalog:** 44 → 66 resources

This second research pass prioritizes failure modes that are invisible in clean-run success rates: ambiguous acknowledgments, late commits, redelivery, partial effects, unsafe downstream actions, and recovery after corrupted environment state. It also extends GUI, parallel-tool, security and multi-agent recovery coverage.

> These are primary-source citations and **authors' claims**, not independent reproduction. A preprint, an OpenReview submission and a peer-reviewed proceedings paper are labeled differently. The proposed techniques rely on specific tool contracts or controlled evaluation conditions; none is a general certification of exactly-once execution.

## What is new and why it belongs

### A. External effect correctness and transactional boundaries (7)

| Source | Key contribution | Important limit |
| --- | --- | --- |
| [LIMBO / Where Does Exactly-Once Live?](https://arxiv.org/abs/2609.29095) (2026 preprint) | Twelve service-boundary faults, effect-ledger verification, 25,930 author-reported episodes. Late commits and redelivery expose cases where reading state before retrying is insufficient. | The testbed is deterministic; paper notes code/data release upon publication and does not prove application-wide exactly-once. |
| [Atomix](https://arxiv.org/abs/2602.14849) (2026 preprint) | Progress-aware commit frontiers distinguish buffered, reversible and irreversible tool effects. | Requires compatible adapters and orchestrator progress signals; no claimed full distributed crash-safe guarantee. |
| [SagaLLM](https://doi.org/10.14778/3750601.3750611) (PVLDB 2025) · [code](https://github.com/genglongling/SagaLLM) | Multi-agent planning with Saga-based compensation and independent validation. | Saga compensation is not ACID rollback. |
| [Robust Agent Compensation / RAC](https://arxiv.org/abs/2605.03409) (2026 preprint) | Log-based compensation architecture for correcting agent side effects. | Framework/testbed dependent; compensation handler correctness must be evaluated. |
| [DelAct](https://doi.org/10.1109/IWQoS70441.2026.11661202) (IWQoS 2026) | Separates control, actuation and event logging; replay and compensation under injected faults. | Results use a selected ticket/invoice workflow. |
| [EffectMatch](https://arxiv.org/abs/2609.31301) (2026 preprint) | Compares authorized changes to observed persistent outcome before admitting commits and downstream actions. | Depends on controlled side-effect observation. |
| [Verified Tool Calls](https://arxiv.org/abs/2608.02645) (2026 preprint) | Postconditions, verify-before-retry and idempotency wrappers under non-atomic faults. | Simulated faults; not proof that read-back is always sufficient. |

**Adjacent recovery boundary:** [MemTX](https://arxiv.org/abs/2607.23929) (2026 preprint) applies transactional admission to shared agent beliefs and attempts typed cascading repairs when beliefs are retracted. It is not a substitute for remote-service compensation.

### B. Benchmarks that separate recovery from nominal competence (8)

| Source | What it measures | Interpret carefully |
| --- | --- | --- |
| [UndoBench](https://arxiv.org/abs/2610.05622) · [code](https://github.com/tradertanmay/undobench) (2026 preprint) | 36 workflows / 36 fault scenarios across eight domains; 2,880 paired lost-ACK trials. Reports 83.54% nominal competence vs 46.72% conditional recovery success in the frozen study. | Author-reported, paired simulation; distinguish fault timing and external effects. |
| [GUI-RobustEval / RoTS](https://proceedings.mlr.press/v306/bu26b.html) · [code](https://github.com/AlibabaResearch/RoTS) (ICML 2026) | 1,216 executable GUI recovery cases and trajectory synthesis. | Resettable GUI tasks are not necessarily remote service recovery. |
| [ToolMisuseBench](https://aclanthology.org/2026.realm-1.28/) (REALM 2026) | Deterministic tool errors, typed recoverability, output-grounded scoring, 1,200 public tests. | Workshop and offline fault plans. |
| [ParaRecover](https://aclanthology.org/2026.emnlp-main.975/) · [code](https://github.com/gbw206/ParaRecover) (EMNLP 2026) | 10,626 examples with 14 error types for cascading parallel-tool faults. | Diagnostic/replanning quality, not global atomicity. |
| [Recovery-Bench](https://openreview.net/forum?id=8FZRnDgDxq) (OpenReview submission associated with NeurIPS 2025) | Continuing from failed trajectories, contaminated environment and context. | Acceptance status unverified; check paper version before claiming peer review. |
| [Same Winners, Different Success Rates](https://arxiv.org/abs/2609.34215) (2026 preprint) | Shows checkpoint action-ranking agreement can be high even with very poor absolute success. | Theory and controlled benchmark interpretation; report absolute metrics. |
| [EpiSEM-Bench](https://arxiv.org/abs/2610.31650) (2026 preprint) | 300 matched unsafe/safe pairs for obtaining missing safety evidence. | Obtaining evidence is not restoring previously applied effects. |
| [Oracle-State Intervention](https://aclanthology.org/2026.realm-1.6/) (REALM 2026) | Replacing context post-failure repairs under 10% of failed runs in specified WebArena conditions. | Negative result is specific to models, environments and intervention timing. |

### C. Selecting corrective actions and containing propagation (6)

| Source | Contribution | Boundary |
| --- | --- | --- |
| [BENCH2ROBUST](https://arxiv.org/abs/2608.11977) (2026 preprint) | Retry/switch/abstain policies learned and evaluated under controlled fault solvability. | Controlled tasks, not arbitrary service state. |
| [RESKILL](https://aclanthology.org/2026.emnlp-main.2024/) (EMNLP 2026) | Hypothesis-driven skill patches with successive retests and failure feedback. | ALFWorld/TextCraft and fixed repair budgets. |
| [RecoverAgent](https://aclanthology.org/2026.findings-emnlp.830/) (EMNLP Findings 2026) | Preserves authorized user intent after indirect prompt injection by rewriting unsafe intermediate inputs. | Security benchmarks, not all tool side effects. |
| [DoCtOR](https://aclanthology.org/2026.emnlp-main.335/) (EMNLP 2026) | Corrects and reflects on decisive erroneous agent and step in a collaborating team. | Does not establish distributed compensation guarantees. |
| [Safety Must Survive Self-Improvement](https://arxiv.org/abs/2610.01073) (2026 preprint) | Revalidation and rollback of unsafe executable edits across self-improvement generations. | Controlled authorization tasks. |
| [AIR](https://proceedings.mlr.press/v306/xiao26n.html) (ICML 2026) | Detects incidents, executes bounded containment/remediation, and synthesizes prevention rules. | Tested agent types and evaluation environment only. |

The seventh cross-cutting item is **MemTX** in section A.

## Comparing to existing repository coverage

- **LIMBO / UndoBench vs the ambiguous-write demo:** the demo proves an intuitive case, while the new papers consider late in-flight commits, redelivery, partial effects, conditional recovery and effect-ledger scoring.
- **Atomix, SagaLLM, RAC, DelAct and EffectMatch vs durable workflow systems:** research prototypes address effect semantics, boundaries and compensation; Temporal, Inngest and DBOS document durable execution. None alone grants an external API the missing contract.
- **ToolMisuseBench / BENCH2ROBUST vs ToolMaze:** these add typed recoverability, deterministic offline faults and explicit retry/switch/abstain policies.
- **ParaRecover vs existing sequential fault tests:** dependency branches introduce error propagation and partial branch completion.
- **GUI-RobustEval vs CUA-Recovery:** controlled errors made by an agent policy and synthesized repair trajectories complement inherited persistent desktop errors.
- **RESKILL / DoCtOR vs Sentry / DoVer:** tested skill patches and decisive-agent targeting complement lesson retrieval and hypothesis intervention.
- **Oracle-State Intervention vs context checkpointing:** available context is not the same as plan competence or repaired state.
- **RecoverAgent / AIR / EpiSEM / self-improvement safety:** containment and safe continuation after security-relevant events, not general prompt-injection catalogs.

## How to evaluate a recovery claim

1. **State the contract:** read-only/idempotent/compensatable/irreversible tool, operation key, conditional writes, terminal-status support and consistency delay.
2. **Name the fault phase:** before mutation, during partial effect, committed before acknowledgment, late commit, transport redelivery or no fault.
3. **Keep control and faulted trials paired:** identify the subset that could finish normally before computing conditional recovery.
4. **Separate detection, diagnosis, repair, and effect correctness:** success requires authoritative postcondition and side-effect ledger checks. Record duplicates, missing writes, residual effects and safe abstentions.
5. **Report limits:** simulator vs live system, whether the environment resets, required code release, intervention budget, model version, reproducibility and statistical uncertainty.

The comparison is **not** a leaderboard. Authors' reported dataset sizes, scores and scope differ substantially.

## Curation notes

The latest pass started from the prior [44-resource catalog](../data/resources.csv) and excluded duplicate versions of already-curated papers. Priority went to primary ACL, PMLR, PVLDB and IEEE records when available, otherwise canonical arXiv/OpenReview records. Publisher venues are named only when verified. No claim is made that every linked project is runnable, that a preprint is peer-reviewed, or that this pass is an exhaustive systematic literature review.

For the practical recovery decision procedure, see [the field guide](field-guide.md). For benchmark details, see [benchmarks](benchmarks.md). For production orchestration, see [production systems](production-systems.md).
