# Zoey Capability And Evidence Landscape

Status: `initial research map; Area 1 corrected implementation frontier revalidated`

Reviewed: `2026-07-18`
Research method: [`METHOD.md`](METHOD.md)

## Scope and authority

This map prioritizes research. It is not a final architecture, product roadmap, migration inventory, or replacement for Zoey's canonical documents and accepted ADRs.

Baselines used for this revision:

- `meta/SYSTEM_THESIS.md` `V0.3.1`;
- `meta/STATE_AND_CONTROL_MODEL.md` `V0.4.1`;
- `meta/OPEN_QUESTIONS.md` `V0.2.20`;
- accepted ADRs through `ADR-009 R4`;
- `workbenches/scn001-selected-slice/README.md` current frontier;
- initial, non-exhaustive inspection of Iris at `legacy/Specialized-LLM/` and Yuki at `legacy/Yuki/`.

Both legacy lineages are locally available. This removes the access blocker for capability-bounded legacy audits, but no complete `LEG-001` migration inventory is claimed. Capability area 1 now has an initial reviewed legacy audit; legacy entries in every other area remain signals to inspect, not reuse decisions.

## Current project position

The active SCN-001 workbench has implemented the selected-slice engineering chain through direct current-session correction realization, delayed-correction candidate formation and activation, later-use applicability, bounded later behavior disposition, mandatory drill-opt-in non-applicability, matched realization, intervention-conditioned outcome with explicit uncertainty, and a grounded explanation with typed retained support. A broader review invalidated the prior current-frontier acceptance; exact corrective range through `6e57840` then passed fresh independent review, with governance closure recorded at `f3c4129`. Formal evaluation and scoring remain unimplemented.

The next selected-slice phase is intentionally blocked until `EVAL-004` and `EVAL-005` receive accepted decisions for formal record/configuration identity and scoreability. External research may proceed only within its own bounded triggers; it cannot resolve those owner-governed decisions, change the workbench boundary, or be presented as milestone evidence. `REPO-001` remains authoritative for any extraction proposal.

## Priority A: strengthen the active engineering and evidence system

| Area | Zoey need | Governing anchors | Current Zoey evidence | Initial legacy signals | External evidence needed |
| --- | --- | --- | --- | --- | --- |
| **1. Semantic state and transitions** | Preserve assertions, observations, hypotheses, candidates, active trials, outcomes, corrections, narrowing, and retirement as distinct states. | SCM; `ADR-003`, `ADR-006` | Selected-slice state is implemented through direct correction, delayed candidate and activation, later-use applicability, bounded disposition, counterfactual non-applicability, realization, bounded outcome/uncertainty, and grounded explanation support; corrected baseline `6e57840` passed fresh independent review. | **Initially reviewed:** Iris implements fail-closed memory-candidate transitions, source binding, and review promotion; Yuki implements current playbook loading/inspection but not correction history. | The corrective cycle exposed no concrete external-mechanism gap, and that mechanism conclusion is unchanged. Broader research remains dormant and trigger-bound. XTDB is `source-reviewed` as `EXT-STATE-001`; no mechanism or experiment is adopted. |
| **2. Provenance and dependency lineage** | Reconstruct the exact evidence, effective state, actor, relation, and order used by a transition. | SCM; `ADR-006`, `ADR-007` | Stable scoped references, typed relations, source-binding checks, and passive inspection implemented for the slice. | Iris provenance/citation, artifact registry, and replay designs; Yuki retrieval traces and evidence artifacts. | Data-lineage and causal-provenance systems, historical dependency reconstruction, cycle/non-convergence handling. |
| **3. Agent and behavioral evaluation** | Replayable scenarios, counterfactuals, nondeterministic campaigns, hard invariants, and oracle separation. | `ADR-002`, `ADR-004`, `ADR-005`, `ADR-009`; `EVAL-004/005` | Harness, simulator, fixtures, boundary tests, and engineering gates exist; no formal evaluation record or scoring contract exists. | Iris evaluation suite and replay specifications; Yuki evidence schemas and baseline soak plans. | Agent-evaluation harnesses, simulation environments, adversarial campaigns, formal evidence packaging, judge-calibration methods. |
| **4. Behavior-configuration identity** | Bind behavior evidence to exact model, prompt, runtime, policy, context, and dependency configuration. | `ADR-007`; `EVAL-004`; `GROW-003/004` | Selected-slice dependency identity exists; formal behavior-configuration record is deferred. | Iris artifact/config registries and versioning rules; Yuki config snapshots and checkpoint manifests. | Experiment tracking, immutable configuration fingerprints, run comparison, replacement/continuity evidence. |
| **5. Architecture and governance enforcement** | Mechanically prevent forbidden dependency direction, answer leakage, stale governance, and unsupported claims. | Engineering Standard; `ADR-008`, `ADR-009`; `REPO-001` | Governance projection, dependency boundary, closed ingress, quality gates, and conformance ledger are active. | Iris policy/control-plane and documentation validation patterns; Yuki layered verification. | Policy-as-code, architecture tests, supply-chain controls, invariant checking, evidence-aware CI patterns. |

These areas should be researched first because they can strengthen the present workbench and later extraction without deciding final memory, model, voice, or product architecture.

## Priority B: future cognition and continuity

| Area | Zoey need | Governing anchors | Current Zoey evidence | Initial legacy signals | External evidence needed |
| --- | --- | --- | --- | --- | --- |
| **6. Personal memory and retention** | Preserve different memory meanings, retention bases, permitted uses, sensitivity, correction, forgetting, and deletion. | SCM; `MEM-001..005`; `CONT-002` | Real personal-memory custody is excluded from the current slice. | Iris hybrid authoritative memory and candidate lifecycle; Yuki flat Chroma runtime plus unimplemented L0/L1/L2 design. | Local-first memory lifecycle, temporal stores, user correction/deletion, consolidation, backup-aware erasure. |
| **7. Retrieval and context assembly** | Select useful context while preserving provenance, trust, sensitivity, epistemic status, and budgets. | Thesis/SCM; `MEM-002/003`; `TRUST-001`; later `EVAL` triggers | Harness injects curated context; production retrieval is explicitly excluded. | Iris context assembly and hostile-input quarantine; Yuki flat turn retrieval and traces. | Hybrid/temporal retrieval, authority-aware RAG, context planning, privacy-aware ranking, evaluation datasets. |
| **8. Behavioral adaptation and drift** | Support scoped trials and durable adaptation without sycophancy, overgeneralization, or uncontrolled identity drift. | Thesis; `GROW-001..005`; `MEM-004` | Trial candidate, activation, focused behavior, and short-term outcome semantics are partly implemented; durable adaptation is excluded. | Yuki continual-learning/drift research and playbook; Iris preference governance and evaluation lifecycle. | Online adaptation, longitudinal evaluation, rollback, drift detection, intervention-aware learning, human review. |
| **9. Hybrid inference and trust boundaries** | Route among local and hosted mechanisms without creating competing identities, authorities, or sole external custody. | Thesis; SCM; `TRUST-001`; `GROW-003/004` | No final inference topology selected. | Iris hybrid specialist runtime and model containment; Yuki local Ollama/STT/TTS pipeline. | Privacy-aware routing, provider isolation, capability degradation, local/cloud fallback, destination-use enforcement. |
| **10. Continuity, recovery, and migration** | Preserve or honestly degrade continuity across crash, restore, migration, state loss, and model replacement. | Thesis; SCM; `CONT-001/002`; `GROW-003/004`; `DEP-003` | Run isolation exists; durable continuity and recovery claims are excluded. | Iris checkpoint/restore and degraded-mode designs; Yuki checkpoint manifests and reliability plans. | Local-first sync, event-log recovery, migration frameworks, restore-gap representation, reconciliation and degraded continuity. |

Research here should precede durable repository creation under `projects/`, but it should not activate these deferred questions until their registered capability triggers occur.

## Priority C: agency and operations

| Area | Zoey need | Governing anchors | Current Zoey evidence | Initial legacy signals | External evidence needed |
| --- | --- | --- | --- | --- | --- |
| **11. Governed external operations** | Separate proposal, actor assurance, authorization, execution, uncertain outcome, reconciliation, revocation, and audit. | SCM; SCN-002; `AUTH-001..006` | Scenario and state/control semantics exist; no real operation path is implemented. | Iris capability tokens, risk tiers, human review, job lifecycle, and autonomy designs. | Durable workflows, idempotency, approval protocols, compensation, external-source reconciliation, audit systems. |
| **12. Initiative and attention management** | Allow useful proactivity without hidden objectives, attention capture, or interruption overload. | Thesis; `INIT-001/002`; `TIME-001`; `PROD-001` | Proactivity is outside the selected slice. | Iris notification policy and progressive autonomy; Yuki reactive-first plans and later modular-ability ideas. | Notification arbitration, priority/candidate queues, interruption-cost models, batching, quiet-time and revocation controls. |

Workflow, authorization, and notification infrastructure may provide stronger references than autonomy-maximizing agent frameworks.

## Priority D: surfaces and embodied interaction

| Area | Zoey need | Governing anchors | Current Zoey evidence | Initial legacy signals | External evidence needed |
| --- | --- | --- | --- | --- | --- |
| **13. Conversational voice stack** | STT, endpointing, incremental generation, streaming TTS, playback, barge-in, cancellation, recovery, turn-taking, and prosody. | `SURF-001/002`; `PROD-003`; `TRUST-001`; `MEM-004` | No real voice stack in Zoey; Qwen3-TTS is watchlisted as `EXT-VOICE-001`. | Yuki has an implemented phrase voice loop; GPT-SoVITS is present as legacy source. | Full-duplex stacks, endpoint detection, real streaming and cancellation, local runtime comparison, multilingual benchmarks. |
| **14. Avatar and presence systems** | Coordinate expression, lip-sync, gaze, motion, and presence without creating another identity. | Thesis; `SURF-001`; `PROD-003` | No embodiment implementation or accepted surface contract. | Yuki avatar plans distinguish automatic expression from deliberate gestures. | Avatar state machines, visemes, motion scheduling, synchronization, accessibility and privacy-aware presence. |
| **15. Cross-surface continuity** | Preserve one Zoey across text, voice, console, and future surfaces while varying presentation and disclosure appropriately. | Thesis; SCM; `SURF-001/002`; `PROD-003` | Surface invariants are canonical; no second real surface exists. | Iris gateway/client boundaries; Yuki voice, dashboard, desktop, and text surfaces. | Session handoff, shared-state contracts, modality-specific presentation, audience/privacy boundaries, failure recovery. |
| **16. User-facing control interfaces** | Let the user inspect and correct memory, adaptations, permissions, provenance, and operational history. | `MEM-005`; `GROW-005`; `PROD-001/002`; `AUTH-005` | Passive engineering inspection exists; no user-facing control product is selected. | Iris memory inbox, review workflows, and client governance display; Yuki read-only dashboard foundation. | Consent and permission UX, audit timelines, provenance explanation, state editors, deletion/revocation flows, usability evidence. |

Qwen3-TTS belongs inside area 13. Its quality does not answer the wider voice-surface, cross-surface, privacy, or continuity questions.

## Cross-cutting gates

Every capability search must assess:

- **security and privacy:** custody, encryption, secret isolation, sandboxing, outbound-data policy, sensitive artifacts, deletion and recovery;
- **observability and inspectability:** structured traces, attributable transitions, configuration fingerprints, replay, failures, and user-readable explanations;
- **modularity and replaceability:** narrow contracts, explicit lifecycle ownership, dependency inversion, migration, and continuity across replacement.

## Next research sequence

1. Keep [`01-semantic-state-transitions`](research-areas/01-semantic-state-transitions/RESEARCH_BRIEF.md) externally dormant while the owned implementation is revalidated; activate external research only when later-lifecycle pressure creates a concrete unanswered mechanism question.
2. Perform capability-bounded Iris/Yuki audits before each Priority B–D external search.
3. Research one family at a time and register only reviewed candidates in `CANDIDATE_REGISTER.md`.
4. Create a comparative extraction record before proposing any controlled experiment.
5. Require a concrete empirical question and applicable governance re-triage before creating a candidate workbench.
