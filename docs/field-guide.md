# Recovery Field Guide

**Scope:** tool-using language-model agents that have failed or entered an uncertain execution state. This is an engineering synthesis of selected research, **not** a production-safety certification.

## Identify what failed

| Layer | Example | Research-guided response |
| --- | --- | --- |
| Tool response | Timeout, semantic corruption, broken endpoint | Classify retryability; check authoritative observations; capped retry, fallback or abstention ([ToolMaze](https://arxiv.org/abs/2606.05806), [RITE](https://arxiv.org/abs/2610.27777)) |
| Long-horizon planning | Wrong precondition, stale context or self-reinforcing error | Locate the causal mistake and attempt a bounded correction, not a generic fresh prompt ([Sentry](https://arxiv.org/abs/2610.02994), [ReplayRCA](https://arxiv.org/abs/2610.41025)) |
| Workspace or GUI | Damaged files, inherited GUI error | Restore a **supported** snapshot/goal state, then confirm task continuation ([AgentRewind](https://arxiv.org/abs/2608.14380), [CUA-Recovery](https://arxiv.org/abs/2610.27645)) |
| External write | A write might have committed before the error was returned | Reconcile in-flight status and committed effects; use tool idempotency/conditional contracts; stop when uncertainty cannot be resolved ([LIMBO](https://arxiv.org/abs/2609.29095)) |
| Multi-agent workflow | Wrong teammate output or failed dependency branch | Keep valid contributions, correct affected dependencies, verify before downstream reuse ([Dittany](https://arxiv.org/abs/2610.42144), [TraceFix](https://doi.org/10.1145/3786335.3813159)) |
| Security incident | Injection redirects a legitimate goal or compromised tool output | Contain the incident, preserve the authorized user intent and verify safe continuation ([AIR](https://proceedings.mlr.press/v306/xiao26n.html), [RecoverAgent](https://aclanthology.org/2026.findings-emnlp.830/)) |

## Safe retry is conditional, not automatic

1. Record a stable business-operation identity, intended postcondition, and known tool contract.
2. Query authoritative state **and** consider in-flight requests; an empty read-back cannot exclude a delayed commit.
3. Retry only if the provider promises the necessary idempotency, conditional-write or terminal-status semantics; apply bounds and backoff.
4. If a previously committed effect must be corrected, use a documented compensation or controlled restore. Compensation is a **new action**, not a magical rewind.
5. Verify end state independently; keep duplicate/missing-effect evidence; stop/escalate if correct state cannot be established.

[LIMBO](https://arxiv.org/abs/2609.29095) tests contract impossibility boundaries; [Permission to Retry](https://arxiv.org/abs/2610.31916) adds the requirement to re-check **authorization** before reconciliation and replay. [SagaLLM](https://doi.org/10.14778/3750601.3750611) and [RAC](https://doi.org/10.1145/3786335.3813141) investigate compensation with different assumptions.

## Measure the result, not the narrative

A failure was not recovered merely because an agent found a likely cause, produced a revised plan, restarted from a checkpoint, or stated that work was complete. Distinguish **detected**, **localized**, **proposed**, **executed**, **verified**, and **safe abstention**.

A particularly useful negative result is that [oracle-state substitution](https://aclanthology.org/2026.realm-1.6/) rescues relatively few failures in its reported WebArena setting. Another is that [diagnostic attribution](https://aclanthology.org/2026.realm-1.15/) can be accurate without improving a recovery action. The missing step is an **independently observed corrected continuation**.

## Local demonstration

Run the dependency-free simulator illustrating an acknowledged-lost committed write and the danger of blind retry:

```bash
python examples/ambiguous_write_demo.py
```

This only exercises a synthetic state machine with stated operation-key behavior; it does not prove exactly-once results for external services.

For deeper methodology see [benchmarks](benchmarks.md) and the [57 curated research publications](../README.md#curated-papers).
