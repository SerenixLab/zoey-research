# Area 1 SCN-001 Implementation Reassessment

Status: `current-frontier closure accepted after independent review`

Reviewed: `2026-07-15`

Reviewed workbench evidence baseline: `adf756a6765e433047574acec1d40e8da74005f4` on local `main`

This reassessment compares the implemented `DP-DIRECT-CORRECTION` trajectory
with `SST-R01` through `SST-R12`. It includes the accompanying checkpoint
hardening and checkpoint-parity correction that revalidate the complete
retained focused-drill and V-003 attribution closures. The evidence is
engineering and conformance evidence only. It is not a formal evaluation,
compatibility result, milestone determination, or independent review.

The initial implementation commit is
`1cab3e1eeb9cc30e8dd2b8d7d8d75ffa38ae1f5e`. Independent review of the combined
stack through `11789d80c34ef2b2b9a03baae5e94770d1798a00` was blocking because
the evaluation checkpoint did not completely reconstruct the focused
instruction/disposition lineage or the current attributed assertion. Commit
`99772a8343c4fb01ba85618fbace6b0c8f20b263` corrected those defects, but its
subsequent independent review was also blocking: evaluation still ignored
direct realization claims owned indirectly through `payload.requestedRef` and
trusted the focused outcome-selected realization transition without proving it
was the unique focused claimant. Commit `3efb7ca057369dd835f70fc120ced1ac5c175e0f`
corrected those defects, but fresh review found that evaluation could accept a
coherently extended direct simulator-ingestion participant set rejected by the
SUT. The evidence baseline above closes that final predicate-parity defect and
received a fresh passing independent review.

## Implemented pressure

The public-boundary trajectory retains these distinct objects and transitions:

```text
raw V-003 user communication
    -> SUT attribution
    -> scoped current spontaneous-session correction/control
    -> direct current-session turn-completion disposition
    -> SUT-selected output
    -> simulator realization fact
    -> SUT realization-recording transition
```

The direct state has exact current-session scope, explicit-user authority,
`turn_completion_correction`, and `not_established` future/global meaning. It
reuses exact retained control facts, but it does not mutate or supersede the
earlier focused-drill immediate-correction instruction, disposition,
realization, outcome, active trial, or their lineage.

The evaluation checkpoint reconstructs the exact direct closure, exact V-003
attribution, and complete retained focused-drill prefix. It independently
checks D-001/D-002 source and ingestion identity, focused instruction and
disposition creators and relations, focused realization/outcome closure, and
the current assertion creator, source, communication basis, status, and order.
It now enumerates direct realization facts, relations, and recording
transitions using the SUT's direct and `payload.requestedRef` ownership paths,
and requires the focused outcome's fact and transition to be the unique
claimants for that disposition. It rejects malformed predecessor state, false
cross-scope lifecycle relations, source or target substitution, duplicate or
partial realization ownership, bad order, missing basis, fidelity mismatch,
and later-family state. Exact replay is idempotent and independent runs share
no semantic identity.

## Explicit mechanism decisions

1. **Are semantic roles sufficiently distinct without a general statechart?**
   Yes for the current frontier. Raw communication, interpretation, scoped
   control, behavior disposition, realization, focused behavior, trial state,
   and outcome are separate families with owned transition evidence.
2. **Can illegal and stale transitions be expressed and tested cleanly?** Yes.
   Exact closure validation, first-ingestion identity, retained basis refs, and
   fail-closed processing cover current stale/substituted/ambiguous cases
   without first/latest selection or a second mutable owner.
3. **Does this milestone need separate current, corrected-history, and as-known
   projections?** No. V-003 changes behavior for a new exact context; it does
   not revise the truth of the earlier focused-drill instruction.
4. **Are exact retained objects plus transition evidence sufficient?** Yes for
   this milestone. They preserve both differently scoped instructions and the
   material order/basis needed to reconstruct current applicability.
5. **Is conflict/non-convergence adequate for the current path?** Yes, narrowly.
   Competing current correction evidence withholds a disposition, multiple
   outputs are not arbitrated, and a false cross-scope conflict or supersession
   cannot satisfy the checkpoint. General conflict objects and cyclic
   non-convergence remain later pressure.
6. **Is source lineage distinct from transition provenance?** Yes. Semantic
   source relations and source-binding evidence are separate from SUT creator,
   basis, interaction, ingestion, and realization transitions.
7. **Register XState?** No. There is no demonstrated hierarchy, concurrency,
   guard-composition, path-explosion, or illegal-state defect that the owned
   explicit mechanism cannot review and test cleanly.
8. **Activate the XTDB experiment?** No. The current path does not require a
   corrected-history/as-known query pair, vendor snapshot basis, or database
   atomicity beyond the run-scoped owned transition mechanism.
9. **Register and review Graphiti?** No. Episode extraction, temporal retrieval,
   and LLM-produced contradiction candidates are not responsibilities of this
   trajectory, and its lineage is reconstructable.
10. **Can Area 1 close without another candidate?** Yes at the V-003 frontier.
    No concrete unanswered mechanism question requires another candidate, and
    fresh independent review accepted the corrected workbench baseline.
11. **What remains deferred to later SCN-001 pressure?** Successor correction,
    narrowing, retirement, revocation, general conflict/non-convergence,
    delayed-candidate formation and activation, later-use applicability,
    longitudinal corrected/as-known queries, and governed erasure behavior.
    These are not missing mechanisms for V-003.
12. **Are open-question triggers activated?** No. This work introduces no formal
    comparison (`EVAL-004`), durable project boundary (`REPO-001`), persistent
    personal memory, new trust boundary, production store, or general governed
    clock. Existing triggers remain intact.

## Adversarial evidence reviewed

- missing fragments and rewritten fixture meaning do not create a disposition;
- wrong actor, context, session, task mode, scope, target, chronology, source
  binding, first ingestion, or realization target fail closed;
- equal-payload earlier evidence cannot substitute for current V-003 evidence;
- duplicate creators, competing instructions, multiple outputs, malformed
  relations, and post-hoc closure repair do not silently select a winner;
- simulator mismatch is retained as supplied evidence but cannot pass the
  checkpoint;
- indirect `payload.requestedRef` realization claims, extra claiming facts,
  partial relations/transitions, duplicate evidence, combined ambiguity, and a
  focused outcome pointer selecting one of two claimants cannot pass;
- a coherently extended direct simulator interaction, ingestion, and basis set
  cannot pass when the SUT requires the exact singleton realization fact;
- changed redelivery is rejected atomically; exact redelivery is idempotent;
- passive inspection does not allocate order or repair semantic state;
- prior focused-drill state remains exact, differently scoped, and
  non-superseded after direct realization;
- no delayed candidate, active delayed trial, global policy, future preference,
  durable adaptation, formal record, or scoring artifact is produced;
- independent runs cannot resolve one another's direct-correction identities.

## Stopping point

`CP-DIRECT-CORRECTION-REALIZED` is sufficient to accept this Area 1 conclusion because
the successful path and its attacks establish the applicable role, identity,
scope, authority, history, stale-basis, provenance, boundary, and
non-promotion properties. Implementing the delayed-correction family would add
new SCN-001 behavior, not answer a remaining mechanism question from this
trajectory. Independent review accepted this evidence. The V-003 investigation
is dormant and trigger-bound; it should reopen when one of the deferred
pressures becomes an accepted frontier or evidence trigger.

## Verification basis

- `npm run check`: all local workbench gates passed after the realization-
  ingestion parity correction, including 245 tests.
- `npm run check:boundary`: all 152 boundary tests passed after the correction.
- `python3 tools/check_research.py`: research conformance passed on the final
  research tree with 2 candidates, 1 family, and 19 Markdown files.

Fresh independent review passed exact corrected workbench commit
`adf756a6765e433047574acec1d40e8da74005f4`. That review is engineering and
conformance evidence only; it does not establish formal evaluation,
compatibility, scoreability, milestone completion, or production readiness.
