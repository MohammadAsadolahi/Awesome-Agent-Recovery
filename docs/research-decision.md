# Scope, Curation and Evidence Policy

_Reviewed 2026-10-28._

## Scope

A resource belongs here if it directly helps **detect, diagnose, choose an intervention for, recover from, or measure failure** in autonomous agent systems. Includes tool failures, runtime intervention, safe retries, state reconciliation, rollback, workspace restoration, durable execution, and multi-agent fault containment.

General agent framework lists, marketing catalogs and undemonstrated capabilities are out of scope.

## Evidence hierarchy

1. Original paper or official publisher record; label preprints accurately.
2. Maintainer code, dataset or benchmark release that can actually be inspected.
3. Official production runtime documentation, with caveats.
4. Reproducible, independently run experiments where available.
5. Secondary summaries only to locate primary sources.

Do not equate an arXiv abstract with peer review, a project page with released code, a workflow checkpoint with transaction rollback, or a paper's reported gain with replication.

## Verified anchor papers

The canonical abstracts of [ReInBench](https://arxiv.org/abs/2610.36471), [CUA-Recovery](https://arxiv.org/abs/2610.27645), [RegretBench](https://arxiv.org/abs/2610.28934), [Sentry](https://arxiv.org/abs/2610.02994), [Traverse](https://arxiv.org/abs/2609.17930), [AgentRewind](https://arxiv.org/abs/2608.14380), [ToolMaze](https://arxiv.org/abs/2606.05806), and [Crab](https://arxiv.org/abs/2604.28138) were checked against the respective primary arXiv pages on 2026-10-28. Broader entries are curated links, not claims of independent reproduction.

## How this differs from existing lists

Broader collections on [agent reliability](https://github.com/swarmproof/awesome-agent-reliability), [agent trajectories](https://github.com/YintongHuo/awesome-agent-trajectory) and [agent harnesses](https://github.com/Gloriaameng/Awesome-Agent-Harness) overlap with the field. This collection prioritizes **failure mode → evidence → recovery action → independent verification**.

The value should come from traceable sources, useful decision aids, and tested examples—not inflating the paper count.