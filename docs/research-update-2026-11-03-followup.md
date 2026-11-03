# Research Review — 3 November 2026 (follow-up)

**Decision:** accept **14 new papers** into the previously **102**-resource index (**116 resources; 98 research papers**). Only scholarly publications/preprints were added. This batch adds distinct contributions on counterfactual repair outcomes, restart choice under cost constraints, GUI restoration, contract-permitted retry, secure checkpoint continuation, and real-world effect integrity.

**Evidence and boundaries:** Original arXiv and ACL Anthology metadata/abstracts and accessible methods were checked on 3 November 2026. A few arXiv landing pages were inaccessible directly during this pass and their metadata was corroborated through scholarly indexing, so those records should not be mistaken for independent full-text replication. Every arXiv-only source below is a *preprint*. All findings are **author-reported**, not independently reproduced. The stated guarantees depend on each paper's testbed, contract and fault assumptions.

## Admission rule

Accept only an original research publication whose main contribution studies **a failure of an AI agent or its execution environment**, and whose work is failure-specific diagnosis linked to repair, targeted intervention, bounded restore/compensation, fault-specific evaluation, or independent effect verification. A generic accuracy gain, assistant repairing somebody else's codebase, and prevention-only advice do not qualify. Avoid duplicates of the current CSV under alternate titles and preprint/venue versions.

## Admitted research

### Transactional effects and recovery contracts

| Publication and original source | Distinct relevance and scope limit |
| --- | --- |
| [RetryBench: Separating Retry Permission from Recovery Outcomes in GPT Tool Use](https://arxiv.org/abs/2610.15884) (2026-10-11) | Separately measures unsupported dispatch after timed-out tool calls and eventual outcome to distinguish false retry permission from actual recovery. **Limit:** 2026 arXiv preprint revised October 22; four purposive tasks, model endpoint comparisons and one recovery decision; does not certify episode-level safety. |
| [Mnemosyne: Agentic Transaction Processing for Validating and Repairing AI-generated Workflows](https://arxiv.org/abs/2607.00269) (2026-06-30) | Uses deterministic admission, persistent transition logs, dependency-safe compensation and bounded reactive repair for proposed workflow changes. **Limit:** 2026 arXiv preprint revised August; stated correctness holds relative to specified executable constraints and adapters, not all external systems. |
| [Fault-Tolerant Budget Conservation in Distributed Multi-Agent Delegation](https://arxiv.org/abs/2610.00349) (2026-09-29) | Preserves delegated agent resource budgets under crash, duplicate delivery, partition and late commit through effect reservations and reconciled settlement. **Limit:** 2026 arXiv preprint; proofs and bounded TLA+ checks plus crash-injected SQLite tests require explicit mediation and gateway assumptions. |
| [When Tool Calls Succeed but Workflows Fail: Anomalies at the Agent-Tool Boundary](https://arxiv.org/abs/2609.15397) (2026-09-14) | Classifies external-effect anomalies that can survive tool success and derives reconciliation and transaction contract requirements at the agent-tool boundary. **Limit:** 2026 arXiv preprint; effect-history model and MCP annotation audit over 98,291 tools, not an implemented general recovery engine. |

### Causal diagnosis and repair validation

| Publication and original source | Distinct relevance and scope limit |
| --- | --- |
| [ReplayRCA: Measuring Post-hoc Diagnosis and Live Oversight of Agent Failures by Counterfactual Replay](https://arxiv.org/abs/2610.41025) (2026-10-29) | Restores failed LLM agent execution to the selected step and tests whether a proposed corrected action improves outcome against a placebo replay. **Limit:** 2026 arXiv preprint; deterministic OpsWorld evaluations and single-step intervention. Causal repair is measured against placebo, not external-world rollback. |
| [From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws](https://arxiv.org/abs/2606.06324) (2026-06-04) | Maps failed agent traces to faulty runtime-harness components and applies scoped patches with regression-aware validation. **Limit:** 2026 arXiv preprint revised July; repairs recurrent harness flaws across evaluated benchmarks, rather than restoring a specific external effect. |
| [EDGE: Error Dependency Graph-Guided Multi-Error Attribution in Multi-Agent LLM Systems](https://aclanthology.org/2026.findings-emnlp.387/) (2026-10) | Builds error-dependency graphs and validates causal subsets via counterfactual rollout for multi-error attribution in LLM multi-agent failures. **Limit:** Findings of EMNLP 2026; TRAIL and MAST attribution evaluations, not independently demonstrated end-to-end repair or external-state verification. |

### Runtime interventions and recovery strategy

| Publication and original source | Distinct relevance and scope limit |
| --- | --- |
| [Monitor Accuracy Isn't the Answer: A Decision-Value Framework for Evaluating AI Agent Restart Monitors](https://arxiv.org/abs/2610.36544) (2026-10-27) | Evaluates restart-versus-continue decisions based on replacement opportunity, remaining budget and certification rather than monitor accuracy alone. **Limit:** 2026 arXiv preprint; 194 model executions on 19 SymPy SWE-bench Verified issues, with no certified positive result in 103 reported live comparisons; simple independent restart assumptions. |
| [Failure Recovery via Belief Updates and World Modeling for Long-Horizon Agents](https://arxiv.org/abs/2610.18082) (2026-10-13) | BELIEFWEAVER retains evidence across failing attempts and checkpoints and uses belief updates plus prospective world modeling to guide repair. **Limit:** 2026 arXiv preprint; three terminal-agent benchmarks with author-reported gains; persistent reasoning state does not establish side-effect integrity. |
| [Self-Healing Agentic Orchestrators for Reliable Tool-Augmented Large Language Model Systems](https://arxiv.org/abs/2606.01416) (2026-05-31) | Classifies tool and orchestration failures, selects corrective actions under limited budgets and verifies reconstructed tool-using agent outcomes. **Limit:** 2026 arXiv preprint; controlled 100-task fault-injection evaluation and small model-in-loop tool study, not broadly reproduced production evidence. |

### Checkpointing and GUI restoration

| Publication and original source | Distinct relevance and scope limit |
| --- | --- |
| [Lost in Recovery: Demystifying Recovery Behavior of Computer-Use Agents via Goal-Oriented Action Replay](https://arxiv.org/abs/2610.27954) (2026-10-20) | Introduces ReTrace and transition-consistent recovery scoring for computer-use agents restoring GUI state after controlled mistakes. **Limit:** 2026 arXiv preprint; goal-oriented action replay and injected GUI errors, not proof of remote system transaction rollback. |
| [Safe to Resume? Breaking Execution Continuity of Agent Execution via Rollback](https://arxiv.org/abs/2608.29381) (2026-08-29) | Studies insecure checkpoint/rollback across agent frameworks including stale dependencies, nondeterministic replay, and unrecorded external effects. **Limit:** 2026 arXiv preprint; examined five framework designs and reported three end-to-end attack demonstrations; a security diagnosis study, not a general-purpose repair guarantee. |
| [How GUI Agents Fail: GraceBench for Execution Stability Diagnosis](https://arxiv.org/abs/2610.19900) (2026-10-14) | Measures recovery ability along with deviation, loops and stagnation in GUI-agent traces using graph-aligned UI transitions. **Limit:** 2026 arXiv preprint; 169 tasks in ten apps and trajectory stability scores; recovery ability is a metric, not automated environment repair. |

### Contextual safety and replay

| Publication and original source | Distinct relevance and scope limit |
| --- | --- |
| [TRAP: Tool-result Replay Attack for Probing Misbinding in LLM Agents](https://arxiv.org/abs/2610.16333) (2026-10-12) | Measures stale and cross-context replay of genuine tool results during agent recovery and evaluates contextual binding defenses. **Limit:** 2026 arXiv preprint; ReplayBench scenarios use controlled result replay and defenses, not claims of universal security. |

## Self-critique and overlap tests

- **ReplayRCA vs Traverse / REFLECT:** the former explicitly measures paired repair outcomes against a placebo continuation, while the latter papers primarily improve attribution. A single successful replay in a deterministic environment is not a proof of safe external rollback.
- **Restart decision value vs ReCoF / Sentry:** restart monitor classification accuracy does not itself show that an intervention helps. The new paper includes negative empirical findings and narrow clean-restart assumptions.
- **RetryBench vs Permission to Retry / LIMBO:** contract-supported authority to retry and successful final outcomes are different measurements. RetryBench tests one decision on limited tasks; LIMBO concerns tool effect ledgers and ambiguity.
- **Mnemosyne vs SagaLLM / Atomix / Cordon:** deterministic admission of untrusted generated proposals, transition journaling and bounded reactive repair provide a separate transaction formulation. Its safety claims apply only to specified constraints and execution boundaries.
- **ReTrace / GraceBench vs CUA-Recovery / CUADebug:** transition-consistent GUI restoration and trajectory instability metrics answer different questions from inherited-state recovery and earlier causal GUI error diagnosis.
- **Safe to Resume? vs ACRFence / AgentRewind:** incomplete restore, stale dependencies and nondeterministic replay broaden the checkpoint-boundary threat model. Security counterexamples do not constitute an automatic repair technique.
- **BELIEFWEAVER vs REVISE / Sentry:** preserved evidence and prospective planning guide recovery across attempted paths, not merely rerunning an unaffected workflow graph.
- **TRAP vs Async-RBench / RITE:** cross-context reuse of a valid but stale tool-result artifact differs from a tool returning incorrect data or a delayed subagent message.
- **Fault-tolerant budget conservation vs general agent compensation:** uncertain or late external effects consume exclusive delegation budget until proven settled; the analysis depends on the specified gateway and authenticated state.
- **HarnessFix vs AgentDebugX / PROBE:** failed agent traces repair the execution harness itself with patch validation rather than promising that a particular failed external task is restored.
- **Agent-tool boundary anomalies vs EffectMatch / LIMBO:** the effect-history taxonomy tests which provider contracts are expressible and which anomaly classes cannot be ruled out with black-box tool APIs alone; it is a *diagnostic/contract* study, not a recovery runtime.
- **EDGE vs DoCtOR / DoVer:** explicit dependency between multiple errors and intervention-supported attribution; its measured contribution is diagnosis, not completed recovery.

## Excluded or deferred after additional screening

| Candidate | Decision |
| --- | --- |
| [Bonded Recourse for Smart-Contract Settlement of Compensable Agent Side Effects](https://arxiv.org/abs/2609.01939) | **Exclude:** focuses on *financial/legal settlement* of residual harm after permitted actions. Useful adjacent effect accountability work, but not the agent's own operational recovery mechanism. |
| [Binding Drift in Multi-Step Tool-Augmented Agents](https://arxiv.org/abs/2607.18316) | **Defer:** measures prevention and re-verification of entity-binding drift, mostly before downstream failure, overlapping existing pre-action guards without a distinct post-failure restoration process. |
| [Auditing Automated Evaluation, Error Propagation, and Runtime Mitigation in Tool-Using Language Agents](https://arxiv.org/abs/2604.16706) | **Defer:** broad reliability evaluation with runtime interception; overlaps the catalog's existing fault propagation and fabricated-success benchmarks. May be revisited for a distinct recovery metric. |

## Interpretation guidance

Track fault phase, clean-task competency, permitted retries, recovery decisions, failed or duplicate external effects, verified postconditions, abstention and cost as *separate* measures. Never treat a successful retry as proof of justified permission, or a restored checkpoint as proof that remote writes were reversed.

The canonical source is [CSV](../data/resources.csv); [JSON](../data/resources.json) is generated from it. Offline validation and tests are performed through the GitHub quality workflow.
