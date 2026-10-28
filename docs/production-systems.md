# Production Systems: Recovery Boundaries

_Reviewed 2026-10-28. These are documentation-based descriptions, not independent benchmarks._

| System | Documented recovery primitive | What to verify yourself |
| --- | --- | --- |
| [Temporal](https://docs.temporal.io/ai) | Durable workflows, activities, retries, long waits; see [AI cookbook](https://docs.temporal.io/ai/cookbook) | Idempotency, replay boundaries, and compensation for remote writes |
| [Inngest](https://www.inngest.com/docs/durable-execution/durable-agents) | Dynamic durable steps, waits, retry and replay | Step granularity and remote side-effect deduplication |
| [DBOS](https://docs.dbos.dev/python/examples/hacker-news-agent) | Database-backed durable agent workflows | Database transactions vs third-party API effects |
| [Restate](https://github.com/restatedev/restate) | Durable execution journal and service operations | External system behavior and licensing |
| [LangGraph](https://github.com/langchain-ai/docs/blob/main/src/oss/langgraph/persistence.mdx) | Graph/thread persistence, checkpointing, interrupts, time travel | Workspaces and remote actions outside graph state |
| [Pydantic AI](https://pydantic.dev/docs/ai/capabilities/durable_execution/overview/) | Integration with durable execution backends | Backend-specific guarantees and limits |
| [OpenAI Agents SDK Sessions](https://openai.github.io/openai-agents-python/sessions/) | Persistent conversation/session history | Does not provide arbitrary transaction rollback |

## Three different forms of persistence

1. **Conversation persistence** saves what the agent knows.
2. **Durable workflow execution** saves what steps completed and can continue after a worker dies.
3. **Environment snapshots** restore a controlled filesystem/process state.

None alone universally undoes a payment, message, booking, deletion, permission change, or other external write. Reconciliation and compensating actions must match the external service's actual semantics.

## Production review questions

- What is journaled and replayed, and what is executed again?
- Can the service survive process restart, redeploy, and multi-day human approval?
- How are operation IDs propagated across tools and retries?
- Which mutations can be verified, de-duplicated, compensated or safely stopped?
- What happens when compensation itself fails?
- How are state retention, logs, sensitive traces, and operational costs managed?

See the [field guide](field-guide.md) for concrete decisions.