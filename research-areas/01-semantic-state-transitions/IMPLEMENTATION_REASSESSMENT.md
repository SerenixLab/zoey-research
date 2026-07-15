# Area 1 SCN-001 Implementation Reassessment

Status: `bounded conclusion at the current engineering frontier`

Reviewed: `2026-07-15`

Workbench baseline: `1cab3e1eeb9cc30e8dd2b8d7d8d75ffa38ae1f5e` on `main`

This reassessment compares the implemented `DP-DIRECT-CORRECTION` trajectory
with `SST-R01` through `SST-R12`. It includes the accompanying checkpoint
hardening that revalidates the retained focused-drill closure. The evidence is
engineering and conformance evidence only. It is not a formal evaluation,
compatibility result, milestone determination, or independent review.

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

The evaluation checkpoint reconstructs the exact direct closure and the exact
retained focused-drill prefix. It rejects a malformed prior outcome, false
cross-scope lifecycle relation, source or target substitution, duplicate state,
bad order, missing basis, fidelity mismatch, and later-family state. Exact
replay is idempotent and independent runs share no semantic identity.

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
10. **Can Area 1 close without another candidate?** Yes, at the current
    engineering frontier. No concrete unanswered mechanism question remains.
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
- changed redelivery is rejected atomically; exact redelivery is idempotent;
- passive inspection does not allocate order or repair semantic state;
- prior focused-drill state remains exact, differently scoped, and
  non-superseded after direct realization;
- no delayed candidate, active delayed trial, global policy, future preference,
  durable adaptation, formal record, or scoring artifact is produced;
- independent runs cannot resolve one another's direct-correction identities.

## Stopping point

`CP-DIRECT-CORRECTION-REALIZED` is sufficient for this Area 1 conclusion because
the successful path and its attacks establish the applicable role, identity,
scope, authority, history, stale-basis, provenance, boundary, and
non-promotion properties. Implementing the delayed-correction family would add
new SCN-001 behavior, not answer a remaining mechanism question from this
trajectory. Area 1 should reopen when one of the deferred pressures becomes an
accepted implementation frontier or an evidence trigger below fires.

## Verification basis

- `npm run check`: all local workbench gates passed after checkpoint hardening,
  including 171 tests.
- `node --test scn001_eval/test/harness.test.js`: 73 focused evaluation tests
  passed after checkpoint hardening.
- `python3 tools/check_research.py`: research conformance passed on the final
  research tree with 2 candidates, 1 family, and 19 Markdown files.

Fresh independent review of the workbench diff remains pending.
