# Agent Recovery: Research FAQ

**This collection is about failed tool-using LLM agents and verified corrections**, not generic prompting or framework catalogs.

### What counts as AI agent recovery?

A controlled intervention after failure that improves the task's actual state or outcome: bounded tool retry, replanning, local repair, checkpoint restoration, compensation, or safe stopping. A recovery benchmark must measure one of those outcomes, not just detect that an error occurred.

### Why are there only 57 papers now?

The [comprehensive curation audit](curation-audit-2026-11-04.md) screens the prior 131 resources and explains 74 removals. It favors directly measured recovery and distinctive methodological contributions over sheer volume. Companion software and broad frameworks are no longer separate entries.

### Does diagnosing the root cause mean the task is fixed?

No. The [credit-assignment-to-repair study](https://aclanthology.org/2026.realm-1.15/) explicitly probes that gap. [CUADebug](https://aclanthology.org/2026.findings-emnlp.530/) separately measures fault localization and corrected reruns.

### When is an agent's tool call safe to retry?

Only when the operation and provider's contract make it safe. A timed-out effectful write may already be committed **or still in flight**. [LIMBO](https://arxiv.org/abs/2609.29095) studies this and the importance of idempotency keys, status and commit semantics.

### Can a checkpoint roll back the real world?

A checkpoint can restore controlled agent/workspace state, not arbitrary external effects. [AgentRewind](https://arxiv.org/abs/2608.14380) and [Crab](https://arxiv.org/abs/2604.28138) have explicit restoration boundaries. [SagaLLM](https://doi.org/10.14778/3750601.3750611) addresses compensation separately.

### How do I benchmark recovery fairly?

Use matched failed states, a no-recovery baseline, a declared intervention budget, and independently verified outcomes. Separate **clean-run competence**, **conditional recovery**, **duplicate effects**, **false-alarm interventions**, and **cost**. See the [benchmark protocol](benchmarks.md).

### Can a negative-result paper belong?

Yes, if it directly tests a proposed corrective action and explains when that intervention fails. For example, [Oracle-State Intervention](https://aclanthology.org/2026.realm-1.6/) or [From Credit Assignment to Repair](https://aclanthology.org/2026.realm-1.15/).

### Why are some important LLM papers absent?

Being influential or peer-reviewed is not enough. General agent reasoning, agent infrastructure, broad reliability and diagnosis-only studies are valid research **outside this narrow bibliography**. Read the [scope policy](research-decision.md).

### How can I propose a paper?

Read [CONTRIBUTING.md](../CONTRIBUTING.md), identify the precise agent failure and recovery outcome, compare against the existing 57 entries, and provide a canonical scholarly source with limitations.
