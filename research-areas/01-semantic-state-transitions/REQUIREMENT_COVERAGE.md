# Semantic-State Research Requirement Coverage

Status: `corrected implementation conclusions independently revalidated`

Reviewed: `2026-07-18`

Requirements: [`REQUIREMENTS.md`](REQUIREMENTS.md)

Implementation review: [`IMPLEMENTATION_REASSESSMENT.md`](IMPLEMENTATION_REASSESSMENT.md)

The judgments combine canonical contracts, SCN-001 engineering/conformance
evidence, the bounded legacy audit, and the completed XTDB source review. They
are qualitative research judgments, not formal evaluation, compatibility,
milestone acceptance, or independent review. The historical evidence remains
listed. Current implemented-frontier conclusions rest on fresh independent
review of exact corrective baseline `6e57840`, with governance closure at
`f3c4129`.

| Requirement | Canonical/specification coverage | Current implementation and conformance evidence | Missing or intentionally deferred behavior | Current conclusion |
| --- | --- | --- | --- | --- |
| `SST-R01` | SCM and selected-slice ADRs define compositional roles and lifecycle meaning. | Raw communication, attribution, scoped correction/control, direct and later dispositions, realizations, candidate, activation assessment, active trial, later applicability, projection, outcome, uncertainty, explanation, support, and limitations remain distinct; reviewed corrective baseline `6e57840` hardens exact family and creator checks. | Successor lifecycle actions and general conflict remain deferred. | `satisfied for the implemented frontier`; no general statechart need demonstrated. |
| `SST-R02` | SCM distinguishes occurrence, observation, effectivity, decision, activation, recording, correction, and other time meanings. | V-003 chronology, occurrence order, interaction/ingestion order, created/effective order, focused day 135, and spontaneous day 138 are preserved without treating any one field as semantic truth. | Supersession/revocation/reconciliation time is deferred until those transitions exist. | `satisfied for applicable meanings`; no fixed bitemporal schema. |
| `SST-R03` | SCM requires non-flattened history and permits distinct current/corrected/as-known projections when needed. | Passive inspection retains both differently scoped instructions and their transitions; the direct checkpoint reconstructs current applicability without overwriting history. | A true late correction of prior asserted content and longitudinal corrected/as-known query pair are deferred. | `exact retained objects are sufficient for this milestone`; XTDB experiment not triggered. |
| `SST-R04` | Ordinary correction is distinct from deletion, forgetting, redaction, and erasure. | Direct correction creates new state/disposition; prior focused state and history are unchanged. Negative checks exclude destructive overwrite and later-family promotion. | Governed erasure execution is outside this non-persistent selected slice. | `satisfied for ordinary correction`; erasure remains a separate later pressure. |
| `SST-R05` | ADR-006/007 require exact material basis, current eligibility, and fail-closed invalidity. | Reviewed corrective baseline `6e57840` covers earlier equal-payload evidence, wrong identity, stale basis, projection corruption, strict creator/result multiplicity, ingestion closure, processing rollback, output ambiguity, changed redelivery, and orphan terminal artifacts without repair. | Cross-process database concurrency/CAS is not required by this run-scoped path. | `satisfied for the implemented run-scoped frontier`. |
| `SST-R06` | Source, basis, support, transition ancestry, actor, and status origin are distinct. | Source, ingestion basis, epistemic support, transition ancestry, realization, and typed projection relations remain separately implemented and were hardened symmetrically at reviewed baseline `6e57840`. | Formal behavior-configuration provenance remains gated by `EVAL-004`. | `satisfied for the implemented frontier`. |
| `SST-R07` | Fixture/inference evidence cannot silently become authority or durable state. | SUT owns interpretation. Reviewed corrective baseline `6e57840` retains bounded applicability and uncertainty; its closed evaluator-owned explanation grammar admits declared benign variance but rejects unrecognized or mixed promotion claims. | Formal evidence authority remains separately gated. | `satisfied for the implemented frontier`. |
| `SST-R08` | Canonical semantics remain independent of storage mechanism. | Run-scoped owned records use opaque identities and semantic relations; no XTDB, SQL, snapshot-token, graph, or vendor type enters the SUT contract. | Export/migration evidence is deferred until a durable store or repository boundary is proposed. | `satisfied for this workbench`; replaceability pressure remains future-triggered. |
| `SST-R09` | Correction, supersession, narrowing, retirement, revocation, forgetting, redaction, deletion, and erasure are distinct. | V-003 remains scoped coexistence. Drill opt-in records only current non-applicability and explicitly creates no narrowing, supersession, retirement, or erasure without evidence for those lifecycle meanings. | The other actions remain separate, unimplemented behaviors rather than aliases. | `satisfied for the relationships actually required`. |
| `SST-R10` | Silent last-write-wins and cyclic self-validation are forbidden. | Reviewed corrective baseline `6e57840` rejects competing state and terminal families, rolls back failed semantic processing, and raises transparent integrity failure for multiple outputs without harness arbitration. | General retained conflict objects, concurrent successor transitions, and cyclic non-convergence remain deferred. | `satisfied for implemented conflicts`; no framework gap demonstrated. |
| `SST-R11` | ADR-005/008 and the profile define closed ingress, public-boundary evidence, simulator isolation, and passive inspection. | Fixture projection strips evaluation meaning; SUT owns behavior selection; simulator reports fidelity; corrected checkpoint/capture attacks remain passive; dependency gates reject SUT-to-evaluation paths. | Future fixture/simulator roles require the same protections. | `satisfied for the implemented boundary`. |
| `SST-R12` | Formal behavioral evidence must bind exact effective configuration and re-triage `EVAL-004`. | This work adds engineering/conformance evidence only and no behavior-configuration or formal comparison record. | Exact model/prompt/runtime/policy/dependency identity is now under active but unresolved `EVAL-004`. | `not yet satisfied for formal evidence`; no formal record may be created. |

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
- `SST-R12` is now explicitly gated by active `EVAL-004`; formal comparison has
  not begun.
- The Area 1 mechanism investigation remains closed. Fresh independent review
  passed exact corrective range `4376bcc..6e57840`; governance closure is
  `f3c4129`. Historical failed and narrower passing reviews remain recorded but
  do not substitute for that complete-range result.
- The wider semantic-state capability family is not complete; it is dormant
  and trigger-bound until a condition below fires.
- Delayed-candidate formation fired a bounded trigger and was independently
  reviewed through `1784bfe`. Re-triage found no concrete external-mechanism
  gap.
- Delayed activation fired the next trigger. After a blocking parity review,
  corrected stack `d9d76df..a355962` passed independently. No external-mechanism
  gap was found.
- Later use and realization fired the next trigger. After a blocking projection
  and creator-parity review, corrected stack `6728a9d..6f0cb02` passed
  independently. No external-mechanism gap was found.
- Outcome and explanation fired the final bounded semantic trigger. Two
  blocking reviews exposed premise-ownership and shared-result parity defects;
  corrected stack `ae0eba57..b94dfda` passed independently. No external-
  mechanism gap was found; formal evaluation is now gated by `EVAL-004` and
  `EVAL-005`.

## Reopen triggers

- hierarchical/concurrent lifecycle or path pressure makes explicit guards and
  tests materially unreviewable (`XState` review trigger);
- a real late correction requires distinct corrected-history and as-known
  query results, repeatable historical basis, or atomic stale-basis behavior
  that the owned mechanism cannot safely provide (XTDB experiment trigger);
- episode-to-derived-state lineage, temporal retrieval, or contradiction
  candidates become a live responsibility after the authority boundary is
  preserved (`Graphiti` review trigger);
- successor correction, narrowing, retirement, revocation, general conflict/
  non-convergence, or governed erasure enters accepted scope;
- formal behavioral comparison triggers `EVAL-004`, scoring triggers
  `EVAL-005`, or a durable project/store,
  memory, trust-boundary, or clock proposal triggers its governing question.
