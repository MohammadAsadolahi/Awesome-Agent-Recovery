# Agent Recovery: Field Guide

_Updated 2026-10-29. Engineering synthesis; not a production-safety certification._

## Recovery starts with external truth

A language model can recover its conversation while the actual state of a filesystem, database, browser, or remote API remains corrupted. Determine **what state is authoritative**, **whether a side effect committed**, and **which effects are reversible** before retrying.

| Layer | Failure | Recover with | Limitation |
| --- | --- | --- | --- |
| Context | Lost task history | Session persistence, reconstruction | Does not restore the world |
| Agent loop | Invalid tool response, stuck plan | Validation, bounded retries, replanning | Retrying effectful calls may duplicate writes |
| Workflow | Worker crash, deployment | Durable journal and step replay | External writes still need safeguards |
| Controlled workspace | Files or OS state modified | Aligned snapshot and restore | Only covers the controlled sandbox |
| External service | Partial update, billing, deletion | Authoritative reconciliation, idempotency key, compensation | Compensation may be impossible |
| Multi-agent | Bad output spreads between agents | Quarantine, provenance, replay, revalidation | Shared artifacts may already be tainted |

## Decision procedure

1. **Observe:** record intended action, operation ID, tool inputs, outputs, status, and independent evidence.
2. **Detect:** flag explicit errors, broken invariants, semantic mistakes, drift or lack of progress.
3. **Reconcile:** query authoritative state to determine whether an ambiguous action already committed.
4. **Classify:** read-only, idempotent, compensatable, or irreversible/high-impact operation.
5. **Decide:** retry with a stable key, choose another tool, restore aligned checkpoints, compensate, ask a human, or stop.
6. **Verify:** inspect actual state, duplicates, collateral effects, and task success before continuing.
7. **Resume or stop safely:** enforce retry and intervention budgets; log why recovery was chosen.

## Example: lost response after committed write

An agent creates an invoice. The remote API commits it, but the network drops the response. Retrying the same create call might create a second invoice.

**Safer design:** assign a stable business-operation identifier before the request, query the remote service by that identifier after a timeout, and retry only if the API supports the required idempotency/absence guarantees. Stop and escalate if the outcome is unknowable. **A workflow engine does not by itself make an arbitrary external effect exactly once.**

Try the [offline example](../examples/ambiguous_write_demo.py).

## Recovery metrics

- **First-error detection:** percentage of actual first mistakes correctly localized.
- **Verified recovery rate:** recovered episodes divided by failure-exposed episodes, with explicit success criteria.
- **Intervention precision:** necessary versus unnecessary interventions; agents sometimes self-recover.
- **Latency and cost:** additional steps, elapsed time, tokens, tool calls, and infra costs.
- **Duplicate side effects:** repeated remote mutations, ideally zero.
- **Collateral damage:** irreversible or unintended changes even in runs marked successful.
- **Safe stop:** appropriate human escalation/abstention on high-risk ambiguous actions.

## Diagnosis is not recovery

Methods such as [AgentRx](https://aclanthology.org/2026.findings-emnlp.598/) and [TRAJDEBUG](https://aclanthology.org/2026.findings-emnlp.437/) can identify a likely critical fault, but this alone does not repair real state. [AgentDebugX](https://aclanthology.org/2026.emnlp-demos.52/), [CUADebug](https://aclanthology.org/2026.findings-emnlp.530/) and [PROBE](https://arxiv.org/abs/2605.08717) investigate how grounded diagnosis informs a controlled second attempt. Before any rerun: preserve an operation key, determine which effects already committed, choose a valid checkpoint, constrain the next action and independently verify its effects. If these conditions cannot be met, escalate.

## Failure-injection checklist

| Fault | Expected recovery |
| --- | --- |
| Rate limit or transient outage | Backoff and capped retry |
| Silent incorrect tool result | Independent verification |
| Timeout after remote commit | Reconcile before retry |
| Partial batch success | Resume missing items only |
| Worker crash | Replay without duplicating effects |
| Lost task context | Rehydrate goal and real environment state |
| Overwritten files | Restore snapshot, run checks |
| Irreversible uncertain effect | Stop or escalate |

See [benchmarks](benchmarks.md) and [production systems](production-systems.md).