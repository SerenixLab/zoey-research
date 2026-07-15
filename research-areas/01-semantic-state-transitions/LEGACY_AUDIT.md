# Capability-Bounded Iris And Yuki Audit

Status: `initial reviewed audit`  
Reviewed: `2026-07-15`  
Capability: semantic state, correction, and temporal transitions

## Inspection boundary

The local Iris checkout was inspected at `84bea3fbaca81198603885a086b72b5978bab55e`; the local Yuki checkout was inspected at `55f464d28cb06073d78fda20ec32b702aee3dac5`.

Both worktrees had unrelated local changes. Conclusions below use files unchanged from the stated commits. This is a capability-bounded audit, not a complete `LEG-001` migration inventory or a reuse decision.

## Iris / Specialized-LLM

### Implemented evidence

Iris has implemented, tested lifecycle discipline around owner-alpha memory candidates:

- an explicit allowed-transition table in `kernel/state_transitions.py`;
- fail-closed rejection of illegal transitions;
- candidate records with source refs, hashes, scope, expiry, state, metadata, and audit refs;
- tested transitions from review states to approval, denial, deletion, source revocation, or expiry;
- separate managed-memory and derived-index responsibilities around promotion and revocation;
- UI/review flows that do not treat provenance viewing as approval.

Classification: `implemented candidate` for transition-table discipline, fail-closed mutation, source binding, and approval-bound promotion.

### Specification-only or mismatched evidence

The lifecycle design document is broader than the implemented candidate state machine. The specification names `captured`, `sandbox_active`, `review_pending`, `review_only`, `approved`, `denied`, `expired`, `deleted`, `blocked_similar`, `superseded`, and `conflict`; the inspected implementation supports a smaller set centered on review and terminal dispositions. That gap is useful evidence but cannot be reported as implemented coverage.

Iris stores current candidate state and audit-oriented metadata in SQLite. The inspected capability does not establish:

- bitemporal corrected-history and as-known projections;
- typed occurrence, observation, decision, activation, and recording timelines;
- general stale-basis comparison across dependent semantic objects;
- correction of an approved state through a non-destructive successor lifecycle;
- a general conflict/non-convergence model.

Classification: `adapt with rewrite` for Zoey's selected-slice semantics; `pattern/reference only` for the broader memory design.

## Yuki

### Implemented evidence

Yuki's runtime loads a versioned JSON playbook into prompt assembly, and its dashboard exposes the current playbook metadata. The current playbook schema includes `interaction_state.recent_corrections`, active topics, and a provenance section.

This is evidence that a correction-bearing runtime configuration surface and passive inspection path exist. It is not evidence that correction transitions populate, supersede, validate, or historically project those fields.

Classification: `implemented candidate` only for loading and passively exposing the current playbook snapshot.

### Planned and archived evidence

Yuki planning material discusses correction logging, human review before durable changes, playbook versioning, rollback, decision provenance, and memory evolution. The inspected runtime search did not show an implemented correction lifecycle or bitemporal/as-known reconstruction for `recent_corrections`.

Classification: `pattern/reference only` for the planned human gate and versioned playbook; `archive only` for broader correction and evolutionary-memory claims.

## Comparative extraction

| Requirement | Best legacy evidence | Reuse posture | Remaining gap |
| --- | --- | --- | --- |
| Explicit lifecycle and illegal-transition rejection | Iris transition registry and tests | Adapt with rewrite | Zoey semantic roles are broader and compositional. |
| Source-backed promotion | Iris candidate records and review gate | Pattern plus selected implementation ideas | Needs selected-slice dependency identity and activation-basis semantics. |
| Current correction-bearing configuration | Yuki playbook snapshot | Pattern/reference only | No implemented mutation lifecycle or historical projection. |
| Corrected vs as-known history | None found | Missing | External temporal pattern review justified. |
| Stale-basis rejection across dependencies | Partial source-revocation invalidation in Iris | Adapt with rewrite | General material-basis check remains missing. |
| Typed multi-time semantics | Expiry clocks and timestamps in Iris; snapshot version in Yuki | Pattern/reference only | No explicit temporal contract matching Zoey's model. |

## Audit conclusion

External research is justified, but it should extend rather than ignore legacy evidence. Iris is the stronger lifecycle and provenance reference; Yuki is a useful negative lesson about a correction-shaped field without an implemented correction history. Neither removes the need to examine bitemporal projections and stale-basis mechanics.
