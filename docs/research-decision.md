# Curation and Research Evidence Policy

**Updated: 4 November 2026** · [Full 131-item audit](curation-audit-2026-11-04.md)

## Purpose

Curate **original research on recovery of failing tool-using LLM agents**. The active catalog is a small, nonredundant reading list of papers that directly test or enable failure correction, verified recovery, bounded retries, controlled restoration, or recovery-specific evaluation.

**The core distinction:** diagnosing a cause or restarting a prompt is not equivalent to correcting a task or repairing the real environment.

## Hard admission gates

A new record must satisfy **every** gate:

1. **Scholarly original:** research paper, peer-reviewed proceedings publication, or explicitly labeled original preprint. The primary URL must point to a canonical scholarly record. Project READMEs, software products, surveys, generic frameworks, blogs, and tutorials are not catalog records.
2. **Direct recovery problem:** a central research question concerns an agent that has failed, could fail during a testable intervention, or must reconcile a faulty tool/environment. The work must report a corrective method, recovery-specific experiment, or a necessary formal/runtime boundary for safe recovery.
3. **Evidence:** a specified failure model and measurable or formal evidence (for example, fault injection with clean controls, paired reruns, controlled effects, correct state verifiers, or explicit impossibility assumptions). Broad aggregate task accuracy alone does not qualify.
4. **Distinct contribution:** meaningful differentiation from already retained papers in mechanism, failure domain, verifiability, or measured outcome. Reworded retry/reflection approaches without a stronger distinct test are generally excluded.
5. **Faithful limits:** venue/preprint status accurately stated; no assertion of production safety, independently replicated claims, guaranteed external rollback, or code release without supporting evidence.

**One narrowly scoped exception:** [MAST](https://papers.nips.cc/paper_files/paper/2025/hash/b1041e52d3be19f0a9bc491657488e4a-Abstract-Datasets_and_Benchmarks_Track.html), a high-quality, original failure-mode dataset/taxonomy whose fault classification directly informs which recovery mechanisms are needed. Its entry says explicitly that it does **not** measure recovered task execution. The exception is not permission to add other diagnosis-only papers.

## Strength of evidence

Prioritize:

- Peer-reviewed original experiments and substantive reproducible benchmarks **about recovery**, not venue prestige by itself.
- Corrected continuations compared with the same failed initial state and a clean/no-recovery control.
- Independent task and state postconditions; committed-effect ledgers for effectful tools; declared simulator/reset assumptions.
- Clear recovery denominators: all tasks vs initially failed cases vs nominally solvable paired cases.
- Causal ablations and negative results that demonstrate when the proposed intervention does not help.
- Meaningful novelty over existing core papers.

Recent preprints may still be valuable but should carry proportionate uncertainty. Bibliometric "impact" is not mature enough for many 2026 manuscripts; **relevance, evidence and novelty** are the operational editorial standards.

## Explicit exclusions

- General agent frameworks, workflow/orchestration product documentation, and code-only links (list companion code in the paper's `code` field).
- Generic reasoning, prompting, memory, self-improvement or accuracy work without failure-conditioned repair.
- Diagnosis-only benchmarks, monitoring-only metrics and broad fault taxonomies that do not test a recovery outcome (except the specified MAST anchor).
- Generic safety/prevention/prompt-injection studies without measured recovery/continuation.
- Mere "honest failure" or false-success reporting with no attempted repair.
- Narrow robotics, mobile-only and database-query case studies when a more representative, more general recovery paper already covers the mechanism.
- Duplicate preprint/venue records and interchangeable methods with weak incremental evidence.

## Catalog and checks

Edit only [`data/resources.csv`](../data/resources.csv), then run:

```bash
python scripts/validate.py --sync-json
python scripts/validate.py
python -m unittest discover -s tests -v
```

The validator rejects non-paper kinds and nonscholarly primary-source hosts. It cannot automatically judge semantic relevance or paper quality; reviewers must apply these criteria. [`data/resources.json`](../data/resources.json) is generated, not edited independently.

## Transparency and revision

The [4 November audit](curation-audit-2026-11-04.md) records all **57 keeps** and **74 removals**, including cases where excluded works remain valid research. Historical versions are available in Git history rather than the active curated reading path.

A removed paper may return if new evidence demonstrates direct recovery relevance or distinct value. Do not re-add a paper merely to grow the count.
