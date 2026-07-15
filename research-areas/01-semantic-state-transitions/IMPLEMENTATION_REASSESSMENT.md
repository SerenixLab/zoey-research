# Area 1 SCN-001 Implementation Reassessment

Status: `outcome and explanation trigger reassessed after independent review`

Reviewed: `2026-07-15`

Reviewed workbench evidence baselines: direct realization `adf756a6765e433047574acec1d40e8da74005f4`; delayed candidate `1784bfe`; delayed activation `a355962`; later use and realization `6f0cb02`; outcome and explanation `b94dfdaaed3b55e94c4972480db73c7430d56eb3` on local `main`

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
11. **What remains deferred to later semantic pressure?** Successor correction,
    narrowing, retirement, revocation, general conflict/non-convergence, longitudinal
    corrected/as-known queries, and governed erasure behavior. These are not
    missing mechanisms for V-003 or the reviewed later-use frontier.
12. **Are open-question triggers activated?** No. This work introduces no formal
    comparison (`EVAL-004`), durable project boundary (`REPO-001`), persistent
    personal memory, new trust boundary, production store, or general governed
    clock. Existing triggers remain intact.

## Delayed-candidate addendum

The delayed-candidate formation trigger subsequently entered accepted SCN-001
scope. The implementation forms one `formed_non_active` candidate only after
the exact direct realization, retained focused-drill closure, active production
trial, bounded policy, current spontaneous context, and retained user-governed
controls are present. It keeps candidate formation distinct from activation,
prohibits behavior influence before activation, and creates no user preference,
global policy, durable adaptation, later-use disposition, or output.

The candidate's 15 consumed creator inputs each have an explicit `basis`
relation. Six epistemically favoring participants additionally have `support`,
and the direct disposition has separate `transition_ancestry`. Exact replay is
idempotent, changed or incomplete prefixes fail closed, and independent runs
cannot share candidate identity. Fresh independent review passed the exact
workbench stack through `1784bfe`; `d9d76df` records its governance closure.

At that checkpoint, the bounded trigger was re-triaged without starting external
research: the owned mechanism remained adequate, while activation and every
later behavior still required separate assessment.

## Delayed-activation addendum

The activation trigger subsequently entered scope. The corrected implementation
retains three distinct identities: the unchanged non-active candidate, a separate
nine-check assessment, and a separate active delayed trial. Exact basis includes
the candidate, correction and realization lineage, current context/chronology,
bounded policy, retained production trial, and selected controls. No user-response
fact is activation basis, and no later behavior is created.

Independent review of `d9d76df..4cf6af5` was blocking because the checkpoint
accepted a competing retention-basis record rejected by the SUT. Commit
`a355962` closed that singleton-parity gap; fresh review then passed the complete
stack. The owned mechanism remains sufficient, and later-use applicability now
constitutes the next separate pressure.

## Later-use and realization addendum

The next trigger subsequently entered scope. Canonical spontaneous production
now rechecks the exact same-run active delayed trial, creates a bounded later
behavior disposition, and records matched simulator realization without
changing trial state. Focused-drill opt-in independently rechecks its own
same-run trial, records `not_applicable`, and creates no disposition,
realization, narrowing, supersession, retirement, or erasure.

Independent review of `6728a9d..8285c83` was blocking because the raw state
reference lacked an ADR-007 lineage-preserving projection and typed
`projection_of` relation, while the SUT could accept a drill assertion whose
creator pointer did not equal its unique actual creator. Commit `6f0cb02`
closed both gaps with a separate exact projection record and SUT/evaluation
creator parity; fresh review then passed `6728a9d..6f0cb02`. The owned mechanism
remained sufficient. Outcome interpretation and explanation provenance then
formed the next separate pressure.

## Outcome and explanation addendum

The last bounded semantic trigger subsequently entered scope. The corrected
implementation creates a separate intervention-conditioned outcome and
uncertainty record only after exact later realization, and creates a separate
grounded explanation plus typed support and limitation records only after the
outcome closes. `L-005` records only that Zoey received no visible
co-intervention and is explicitly non-exhaustive for private or unobserved
causes. The explanation retains relevant stale history while excluding an
unrelated stale distractor, checks semantic causal limits rather than exact
wording, and retains no hidden chain-of-thought.

Independent review of `ae0eba57..f4422fa` was blocking because evaluator-owned
canonical-premise meaning crossed into the SUT and temporal result multiplicity
was asymmetric. Review through `18365f6` found a remaining evaluator gap for a
duplicated co-created distractor. Corrected stack `ae0eba57..b94dfda` keeps the
premise verdict private and closes global shared-result and uncertainty-relation
parity. Fresh independent review passed. The owned mechanism remains sufficient;
formal record/configuration identity and scoreability are separate governance
decisions under `EVAL-004` and `EVAL-005`, not an Area 1 mechanism gap.

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
- later-use projection rule/view/effective state, creator identity, typed
  `projection_of`/`basis` relations, applicability, disposition, and realization
  fail closed under missing, retargeted, backdated, duplicated, or substituted
  evidence;
- the canonical later path creates no global policy, future preference, durable
  adaptation, formal record, or scoring artifact, while drill opt-in remains
  explicitly inapplicable and creates no outcome or invented lifecycle change;
- outcome creation rejects evaluator-premise leakage, unmatched behavior,
  causal promotion, exhaustive co-intervention claims, undeclared uncertainty
  relations, and incomplete or substituted raw basis;
- explanation validation rejects missing relevant stale history, duplicated
  selected or co-created assessment results, unrelated-history promotion,
  lineage substitution, causal prose, hidden-reasoning claims, and limitation
  rewrites without mutating retained state;
- independent runs cannot resolve one another's direct-correction identities.

## Stopping point

The selected engineering chain through `DP-EXPLAIN` is sufficient to accept the
current Area 1 conclusion because the successful path and its attacks establish
the applicable role, identity, scope, authority, history, stale-basis,
provenance, uncertainty, explanation-support, boundary, and non-promotion
properties. Independent review accepted this evidence. The wider capability
family is dormant and trigger-bound; it should reopen only when a deferred
semantic pressure creates a concrete mechanism question.

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

Fresh independent review also passed corrected later-use stack
`6728a9d..6f0cb02` after 36 focused checks, 100 SUT state tests, 207 boundary
tests, and all 307 aggregate tests passed. Governance closure is `ae0eba5`.

Fresh independent review passed corrected outcome/explanation stack
`ae0eba57..b94dfda` after 38 focused checks, 105 SUT state tests, 240 boundary
tests, and all 345 aggregate tests passed. Governance closure is `4376bcc`.
