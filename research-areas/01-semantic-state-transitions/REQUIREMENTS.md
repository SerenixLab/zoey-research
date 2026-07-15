# Semantic State And Transition Research Requirements

Status: `research requirements, not architecture`  
Reviewed: `2026-07-15`

These requirements translate the canonical state/control model into external-research acceptance questions. They do not prescribe a schema, database, event format, or module boundary.

| ID | Requirement | Evidence expected from external review or experiment |
| --- | --- | --- |
| `SST-R01` | Preserve semantic roles and lifecycle states without forcing them into one universal enum. | Mapping shows which distinctions are native, application-owned, or unsupported; impossible collapses are recorded. |
| `SST-R02` | Represent temporal meanings explicitly and only where applicable. | Occurrence, observation, validity/effectivity, decision, activation, recording, expiry, supersession, revocation, and reconciliation are not silently equated. |
| `SST-R03` | Support separate projections for current effective state, corrected history, and as-known-at-the-time history. | Query examples produce different answers after a late correction and name the time/basis used. |
| `SST-R04` | Correct without destructive overwrite, except through an explicit governed erasure path. | Earlier recorded state and transition basis remain queryable after ordinary correction; erasure has separate semantics and evidence. |
| `SST-R05` | Reject a consequential transition whose material basis is stale. | A concurrent correction, revocation, narrowing, or dependency change makes the old transition fail or re-enter evaluation instead of winning by last write. |
| `SST-R06` | Preserve source lineage and transition provenance separately. | The system can reconstruct underlying evidence plus actor, policy, configuration, and guard basis for the state change. Transaction correlation metadata alone is insufficient. |
| `SST-R07` | Keep extraction, inference, and contradiction detection on the candidate side of authority. | LLM, similarity, graph, or rule outputs cannot become authoritative state without the applicable Zoey-owned promotion control. |
| `SST-R08` | Keep semantic contracts storage-independent and replaceable. | Candidate-specific IDs, timestamps, snapshots, or actors remain behind owned contracts, with an export/migration story for authoritative state. |
| `SST-R09` | Distinguish correction, supersession, narrowing, retirement, revocation, forgetting, redaction, deletion, and erasure. | Each applicable action has different current-state, historical, lineage, and derived-artifact consequences. |
| `SST-R10` | Make conflict and non-convergence explicit. | Concurrent or cyclic bases do not self-validate and do not resolve through silent last-write-wins. |
| `SST-R11` | Preserve the selected-slice SUT/evaluation and state/projection boundaries. | Research mechanisms do not allow harness facts, oracle state, or derived inspection facts to become SUT semantic state. |
| `SST-R12` | Bind any behavioral evidence to exact effective configuration. | If the research becomes an evaluation record or comparison, the applicable `EVAL-004` metadata trigger is re-triaged before the claim. |

## Required adversarial cases

Any future controlled experiment must include at least:

- a correction received after the corrected fact became effective;
- a correction received after a dependent transition was proposed but before activation;
- two concurrent transitions from the same stale basis;
- narrowing that changes applicability without declaring the original source false;
- contradiction that remains unresolved rather than auto-selecting a winner;
- forgetting or deletion with surviving source, derived artifact, or backup implications;
- a transaction or graph history that exists but lacks sufficient semantic authority;
- replay under a different behavior configuration that must not masquerade as the original decision.

## Non-requirements

- Every semantic object does not need every timestamp.
- Every transition does not need heavyweight audit storage.
- A temporal database is not required.
- Event sourcing is not required.
- A graph model is not required.
- A statechart runtime is not required.
- Immutable application history does not authorize retention of data that must be erased.
