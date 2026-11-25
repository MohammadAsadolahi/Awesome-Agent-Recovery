# Research update — 25 November 2026

**Scope:** original publications about recovery of failed tool-using LLM agents, following the unchanged [evidence policy](research-decision.md). Baseline: 57 papers after the [4 November audit](curation-audit-2026-11-04.md). This incremental search focused on November 5–25, with searches for tool fault injection, checkpoint restoration, safe retries and reconciliation, failure-conditioned repair, agent benchmarks and November ACL proceedings. It is not a systematic review.

## Included (7 new papers; 64 total)

| Paper | Why it qualifies | Evidence limits |
| --- | --- | --- |
| [Which Failure Does an Intervention Repair? When Agent Interventions Help, and Where Self-Evolving Skills Stall](https://arxiv.org/abs/2611.29290) (2026-11-22) | Uses matched changes to agent harnesses, skills, models and budgets to distinguish failure-conditioned rescue from aggregate accuracy gains. | Preprint; roughly 0.9 million trajectories across nine benchmarks. Matched comparisons show configuration dependence; not proof of live recovery or external-effect integrity. |
| [When Tools Fail, Agents Fabricate: Silent Failure and Verification-First Oversight in Tool-Using LLM Agents](https://arxiv.org/abs/2611.28341) (2026-11-20) | RetryRealistic injects persistent or transient tool faults in executable environments and tests a verification-first monitor that directs corrective actions. | Preprint; 2,100 faulted runs across four agents. Author-reported monitor improves correct recovery from 45.6% to 56.3%; bounded sandbox, not production verification. |
| [Exercised, Rarely Recovered: What Public Reports Say About Recovery in 50 AI Agent Harnesses and Runtimes](https://arxiv.org/abs/2611.27090) (2026-11-20) | Codes observed outcomes of recovery mechanisms in public reports and contrasts practical restoration evidence with research-runtime guarantees. | Preprint; original observational study of 50 systems and 128 real-use reports. Only 19 reports describe full recovery; selection and reporting bias preclude a population recovery rate. |
| [Idempotency Is Not Recovery: A Fault-Injection Study of Language-Model Agent Tool Actions](https://arxiv.org/abs/2611.23353) (2026-11-17) | Separates duplicate-effect suppression from recovery of ambiguous outcomes using fault injection, independent target-state checks, reconciliation and ledger ablations. | Preprint; 7,513 trials per OS, captured model responses and single-host faults. Reconciliation ablation leaves 100/100 post-effect outcomes ambiguous; not distributed exactly-once assurance. |
| [AgentFaultBench: State-Verified Evaluation of Tool-Fault Recovery](https://arxiv.org/abs/2611.20711) (2026-11-16) | Tests recovery advice against neutral feedback under injected faults using independent checks of GitLab state, required verification and final responses. | Preprint; isolated GitLab, LangGraph and CrewAI, 1,944 planned primary runs plus a 624-run study. Primary advice effects mixed or inconclusive; no human validation. |
| [Recovery Gone Too Far: Understanding and Repairing Risky Fallback in LLM Agents](https://arxiv.org/abs/2611.19886) (2026-11-15) | Studies action-boundary violations during recovery by substitute tools and evaluates a calibrated monitor that returns risky fallback decisions to the agent. | Preprint; 304 scenarios across eight domains, four models and two production coding agents. Reduced violations do not establish universal safety; normal success can decline. |
| [Same Error, Different Recovery: How Delivery Changes LLM Agent Behavior](https://arxiv.org/abs/2611.11581) (2026-11-08) | Controls feedback placement, retained history and conversational turns to isolate their effects on retry, correction and stopping after tool failures. | Preprint; 13 open models, deterministic reruns and ToolMaze evaluation. Explicit-error gains do not generalize to the Loud/Quiet tasks; source record inspected via arXiv mirror. |

## Excluded or deferred

| Candidate | Decision and reason |
| --- | --- |
| [ProbeAgent](https://arxiv.org/abs/2611.26897) | Exclude: tests recurrence of diagnosed failures rather than repairing the failed execution. |
| [Improving Repair Agents with Cause-Chain Diagnoses](https://arxiv.org/abs/2611.30574) | Exclude: diagnoses defects in software that agents are asked to fix, rather than failures of the agents themselves. |
| [When AI Agents Should Repair, Replan, or Abandon](https://arxiv.org/abs/2611.19663) | Defer: useful theoretical planning model, but the primary contribution is general plan commitment; no direct tool-using LLM recovery experiments established here. |
| [TRIAGE](https://aclanthology.org/2026.aacl-short.27/) | Defer: failure-attribution focus; corrective task outcomes not verified in this pass. |
| [SecondChance](https://arxiv.org/abs/2611.31586) | High-priority follow-up: abstract indexed by multiple secondary sources, but primary record could not be retrieved in this pass. Do not add until canonical source is accessible. |
| Log Analysis for LLM-Based Agents | Exclude: survey rather than original recovery experiment. |
| Agent Error Simulator | Defer: inspect full publication and compare its narrow numerical-workflow setting against the retained tool-fault benchmarks before admission. |

Primary arXiv records were inspected for six included papers. For Same Error, Different Recovery, an [arXiv record mirror](https://arxiv.cnoctave.top/abs/2611.11581) and independent indexed metadata were inspected because the canonical page could not be retrieved by the search service; the catalog retains its canonical arXiv identifier. RetryRealistic's companion repository was linked from the paper and inspected. Other code fields are blank unless confirmed. All new entries are explicitly labeled preprints. Results are author-reported; no experiments were independently reproduced. No prior paper was removed, and the earlier audit remains historical.

## Reproducibility

The canonical CSV and generated JSON use identical records; the README lists each paper once within the curated sections. Existing admission gates and validation scripts remain unchanged.
