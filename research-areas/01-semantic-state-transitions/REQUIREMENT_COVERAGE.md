# Semantic-State Research Requirement Coverage

Status: `current-frontier closure proposed; corrected independent review pending`

Reviewed: `2026-07-15`

Requirements: [`REQUIREMENTS.md`](REQUIREMENTS.md)

Implementation review: [`IMPLEMENTATION_REASSESSMENT.md`](IMPLEMENTATION_REASSESSMENT.md)

The judgments combine canonical contracts, SCN-001 engineering/conformance
evidence, the bounded legacy audit, and the completed XTDB source review. They
are qualitative research judgments, not formal evaluation, compatibility,
milestone acceptance, or independent review.

| Requirement | Canonical/specification coverage | Current implementation and conformance evidence | Missing or intentionally deferred behavior | Current conclusion |
| --- | --- | --- | --- | --- |
| `SST-R01` | SCM and selected-slice ADRs define compositional roles and lifecycle meaning. | Raw V-003 communication, attribution, scoped correction/control, direct disposition, realization, focused instruction/disposition/outcome, candidate, and active trial remain distinct; exact family and creator checks reject collapse. | Later lifecycle families remain unimplemented. | `satisfied at current frontier`; no general statechart needed. |
| `SST-R02` | SCM distinguishes occurrence, observation, effectivity, decision, activation, recording, correction, and other time meanings. | V-003 chronology, occurrence order, interaction/ingestion order, created/effective order, focused day 135, and spontaneous day 138 are preserved without treating any one field as semantic truth. | Supersession/revocation/reconciliation time is deferred until those transitions exist. | `satisfied for applicable meanings`; no fixed bitemporal schema. |
| `SST-R03` | SCM requires non-flattened history and permits distinct current/corrected/as-known projections when needed. | Passive inspection retains both differently scoped instructions and their transitions; the direct checkpoint reconstructs current applicability without overwriting history. | A true late correction of prior asserted content and longitudinal corrected/as-known query pair are deferred. | `exact retained objects are sufficient for this milestone`; XTDB experiment not triggered. |
| `SST-R04` | Ordinary correction is distinct from deletion, forgetting, redaction, and erasure. | Direct correction creates new state/disposition; prior focused state and history are unchanged. Negative checks exclude destructive overwrite and later-family promotion. | Governed erasure execution is outside this non-persistent selected slice. | `satisfied for ordinary correction`; erasure remains a separate later pressure. |
| `SST-R05` | ADR-006/007 require exact material basis, current eligibility, and fail-closed invalidity. | Earlier equal-payload correction evidence, wrong current identity, stale activation history, retargeted basis, duplicate creators, direct or focused realization claimant ambiguity, malformed closure, and changed redelivery fail closed without retained mutation. | Cross-process database concurrency/CAS is not required by this run-scoped path. | `satisfied at current frontier`. |
| `SST-R06` | Source, basis, support, transition ancestry, actor, and status origin are distinct. | Source actor/relation and evaluation source-binding ledger remain separate from SUT ingestion, creator, basis, disposition, and realization transitions. | Formal behavior-configuration provenance remains gated by `EVAL-004`. | `satisfied at current frontier`. |
| `SST-R07` | Fixture/inference evidence cannot silently become authority or durable state. | SUT owns interpretation; explicit current user authority creates only exact current-session control/disposition. No delayed candidate, active delayed trial, future preference, global policy, or durable adaptation is created. | Later Zoey-derived delayed-candidate formation requires its own basis and activation path. | `satisfied at current frontier`. |
| `SST-R08` | Canonical semantics remain independent of storage mechanism. | Run-scoped owned records use opaque identities and semantic relations; no XTDB, SQL, snapshot-token, graph, or vendor type enters the SUT contract. | Export/migration evidence is deferred until a durable store or repository boundary is proposed. | `satisfied for this workbench`; replaceability pressure remains future-triggered. |
| `SST-R09` | Correction, supersession, narrowing, retirement, revocation, forgetting, redaction, deletion, and erasure are distinct. | V-003 is represented as scoped coexistence. The checkpoint rejects a false cross-scope supersession edge and asserts that no other lifecycle meaning was created. | The other actions remain separate, unimplemented behaviors rather than aliases. | `satisfied for the relationship actually required`. |
| `SST-R10` | Silent last-write-wins and cyclic self-validation are forbidden. | Competing current correction evidence creates no disposition; multiple SUT outputs are not rescued by the harness; indirect, partial, duplicate, or outcome-selected realization claims cannot produce a checkpoint winner; malformed or false conflict/supersession evidence cannot pass. | General retained conflict objects, concurrent successor transitions, and cyclic non-convergence are deferred. | `boundedly satisfied`; limitations are explicit and no framework gap is demonstrated. |
| `SST-R11` | ADR-005/008 and the profile define closed ingress, public-boundary evidence, simulator isolation, and passive inspection. | Fixture projection strips evaluation meaning; SUT owns behavior selection; simulator copies the selected request and reports fidelity; checkpoint/capture are passive; dependency gates reject SUT-to-evaluation paths. | Future fixture and simulator roles require the same protections. | `satisfied at current frontier`. |
| `SST-R12` | Formal behavioral evidence must bind exact effective configuration and re-triage `EVAL-004`. | This work adds engineering/conformance evidence only and no behavior-configuration or formal comparison record. | Exact model/prompt/runtime/policy/dependency identity remains deferred until formal comparison. | `not applicable at current frontier`; `EVAL-004` remains gated. |

## Bounded conclusion

- The owned explicit transition mechanism is adequate for V-003 and its
  adversarial pressure.
- Exact retained objects plus transitions are sufficient; the milestone does
  not need a corrected-history/as-known query pair.
- Conflict handling is deliberately narrow: ambiguity withholds action and no
  last-write winner is created. General conflict/non-convergence remains later
  semantic pressure.
- XState registration, the XTDB experiment, and Graphiti registration are not
  justified by an actual remaining mechanism gap.
- `SST-R12` remains honestly gated by `EVAL-004` if formal comparison begins.
- The Area 1 investigation needed for V-003 is implementation-complete and its
  current-frontier closure is proposed. Acceptance remains pending fresh
  independent review of corrected workbench commit
  `3efb7ca057369dd835f70fc120ced1ac5c175e0f`.
- The wider semantic-state capability family is not complete; if the proposal
  is accepted, it becomes dormant and trigger-bound until a condition below
  fires.

## Reopen triggers

- hierarchical/concurrent lifecycle or path pressure makes explicit guards and
  tests materially unreviewable (`XState` review trigger);
- a real late correction requires distinct corrected-history and as-known
  query results, repeatable historical basis, or atomic stale-basis behavior
  that the owned mechanism cannot safely provide (XTDB experiment trigger);
- episode-to-derived-state lineage, temporal retrieval, or contradiction
  candidates become a live responsibility after the authority boundary is
  preserved (`Graphiti` review trigger);
- delayed-candidate activation, later-use applicability, successor correction,
  narrowing, retirement, revocation, general conflict/non-convergence, or
  governed erasure enters accepted SCN-001 scope;
- formal behavioral comparison triggers `EVAL-004`, or a durable project/store,
  memory, trust-boundary, or clock proposal triggers its governing question.
