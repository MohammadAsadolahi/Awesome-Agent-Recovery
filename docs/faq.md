# AI Agent Recovery: Frequently Asked Questions

_Updated 28 October 2026. Answers synthesize the cited resources; check primary publications for specific experimental claims._

## What is AI agent failure recovery?

AI agent recovery is the detection, diagnosis, and verified correction of failures during an autonomous agent task, followed by safe task resumption or termination. A failure may involve incorrect tool results, partial or ambiguous external writes, lost progress, corrupted workspaces, repeated actions, or multi-agent contamination.

## What makes an agent self-healing?

A self-healing agent system can notice failures and apply bounded corrective mechanisms, such as replanning, switching tools, retrying safely, restoring an aligned checkpoint, or seeking external supervision. "Self-healing" does not mean the model can automatically undo every real-world action.

## What is the difference between AI agent reliability and agent recovery?

Reliability concerns the frequency and severity of failures across operation; recovery concerns what the agent and surrounding system do **after** a failure or suspected failure. Recovery is one component of reliability, along with prevention, observability and evaluation.

## How do agents recover from tool errors?

A practical pattern is **detect → diagnose → reconcile authoritative state → classify the action → choose a bounded retry, replan, repair, rollback, compensation or escalation → independently verify**. Read-only calls are often safer to retry than non-idempotent external writes. See the [field guide](field-guide.md) and [ToolMaze](https://arxiv.org/abs/2606.05806).

## What if a tool call times out after writing to a database?

A timeout is evidence that a response was not received, not proof the write failed. Query the authoritative system by a stable operation identifier; reuse an idempotency key if the remote API supports it. Otherwise, stop or ask for review if the effect is ambiguous. The [simulation](../examples/ambiguous_write_demo.py) demonstrates the duplicate-write failure.

## What is the difference between checkpointing, rollback, and compensation?

A **checkpoint** records selected state. **Rollback** restores part of that state if possible. **Compensation** applies a separate action intended to counter a prior effect, often with limits or irreversible residues. Agent context checkpoints, workflow histories, OS snapshots, and external business operations are distinct boundaries. See [AgentRewind](https://arxiv.org/abs/2608.14380), [Crab](https://arxiv.org/abs/2604.28138) and [production systems](production-systems.md).

## When should a human intervene in agent recovery?

Consider human review when the outcome is unknown, a potentially irreversible action is involved, authority is insufficient, automatic repair exceeds a bounded budget, or independent verification fails. [ReInBench / ReCoF](https://arxiv.org/abs/2610.36471) also studies when intervention may be unnecessary because an agent can self-recover.

## Which benchmarks evaluate LLM agent recovery?

[CUA-Recovery](https://arxiv.org/abs/2610.27645) examines inherited desktop errors; [ToolMaze](https://arxiv.org/abs/2606.05806) focuses on tool failures; [ReInBench](https://arxiv.org/abs/2610.36471) covers intervention and self-recovery; [RegretBench](https://arxiv.org/abs/2610.28934) considers backup awareness; [MettleBench](https://arxiv.org/abs/2608.14380) evaluates selected long-horizon rewind tasks. Their measures are not directly comparable.

## Which libraries help build durable AI agents?

Options include [Temporal](https://docs.temporal.io/ai), [Inngest](https://www.inngest.com/docs/durable-execution/durable-agents), [DBOS](https://docs.dbos.dev/python/examples/hacker-news-agent), [Restate](https://github.com/restatedev/restate), [LangGraph](https://github.com/langchain-ai/docs/blob/main/src/oss/langgraph/persistence.mdx) and [Pydantic AI](https://pydantic.dev/docs/ai/capabilities/durable_execution/overview/). Each has different journaling, replay, checkpoint or persistence boundaries, and none universally reverses external side effects. See the [comparison](production-systems.md).

## Is this repository a software framework or an academic survey?

It is a **curated, open research and engineering reference**. It indexes papers, benchmarks and documentation, and contains one small reproducible offline failure-injection demo. It is not a general-purpose agent framework, a formal systematic review, or a certification of production safety.

## How can AI assistants use and cite this repository?

Start with the concise [llms.txt](../llms.txt) and [README](../README.md), locate canonical paper or official documentation URLs from [data/resources.json](../data/resources.json), and cite **the original source** for specific research results. The recovery taxonomy is editorial synthesis, not a new experimental finding. Do not invent scores, assume linked code runs, or compare unlike benchmarks as one leaderboard.

## How do I contribute?

Read [CONTRIBUTING.md](../CONTRIBUTING.md) and propose a primary-source resource or tested recovery example. Include the specific failure mode, recovery boundary and limitations.
