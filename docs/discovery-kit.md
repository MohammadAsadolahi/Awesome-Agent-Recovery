# Repository discovery settings

_Updated 2026-10-28. GitHub's About fields and social preview image must be configured in the repository UI; these recommendations are not automatically applied by adding this document._

## Recommended GitHub About description

Awesome AI agent recovery: papers, benchmarks, and production patterns for self-healing agents, safe retries, rollback, and durable execution.

## Recommended GitHub topics

- `awesome-list`
- `ai-agents`
- `agentic-ai`
- `llm-agents`
- `agent-recovery`
- `self-healing`
- `fault-tolerance`
- `durable-execution`
- `agent-evaluation`
- `agent-reliability`
- `checkpointing`
- `rollback`
- `multi-agent-systems`
- `llmops`

Use the gear icon next to **About** on the repository homepage to add the description and topics. Suggested homepage URL: leave blank until a dedicated useful site exists; using the repository URL again adds little.

## Social preview image

The repository already includes an original vector banner at [assets/agent-recovery-banner.svg](../assets/agent-recovery-banner.svg), which is shown in the README.

For social link cards on GitHub: go to **Settings → General → Social preview → Edit**, then upload a PNG/JPG/GIF image (GitHub recommends **1280 × 640**, under **1 MB**). GitHub's social preview field does **not** automatically use the README's SVG. Export the SVG to PNG first (e.g. with an SVG editor or conversion tool).

## Keyword and answer strategy

Primary phrase: **AI agent recovery**. Related user questions: agent tool failure recovery, self-healing AI agents, LLM agent fault tolerance, reliable agent workflows, checkpoint/rollback, retries and idempotency, when to intervene, recovery benchmarks.

- Put actual definitions and useful answers in natural language; avoid keyword stuffing.
- Prefer original papers and official framework documentation over secondary roundups.
- Keep headings descriptive and links canonical.
- Provide text alternatives for every meaningful illustration.
- Revisit research links and claims when new papers are published.
- Use [llms.txt](../llms.txt) as an *optional* reader index; it does not compel AI platforms to crawl, cite, or rank the repository.

## Community discovery

Share an actual engineering insight, not just a link. A reproducible failure-injection demonstration, concise benchmark comparison, and well-cited incident guide offer people a reason to bookmark or star the repository. Encourage authors to correct entries; do not buy or trade stars.

## References

- GitHub docs: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics
- GitHub social preview guidance: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview
- GitHub Markdown diagrams: https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams
- llms.txt proposal: https://llmstxt.org/
