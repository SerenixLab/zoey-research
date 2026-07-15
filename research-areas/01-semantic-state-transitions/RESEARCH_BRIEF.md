# Semantic State, Correction, And Temporal Transition Research Brief

Status: `V-003 closure proposed; corrected independent review pending`

Reviewed: `2026-07-15`

Capability area: `1` Semantic state and transitions

Current engineering adjacency: `SCN-001` direct current-session correction

## Decision

Propose closure of the Area 1 investigation required for the implemented V-003 engineering frontier. If fresh independent review accepts the corrected evidence baseline, retain the wider capability family as dormant and trigger-bound. Do not adopt the proposed multi-framework composition as architecture, choose a storage engine, create another workbench, or broaden the current SCN-001 milestone from this research alone.

The implementation question was narrower than a general memory architecture:

> Can Zoey preserve semantic distinctions, differently scoped history, temporal meaning, exact transition basis, and inspectable current applicability through direct current-session correction with its owned mechanism?

The corrected implementation supports a yes answer for the current frontier, subject to fresh independent review. The evidence and limits are recorded in [`IMPLEMENTATION_REASSESSMENT.md`](IMPLEMENTATION_REASSESSMENT.md) and [`REQUIREMENT_COVERAGE.md`](REQUIREMENT_COVERAGE.md). Exact retained objects and transitions are sufficient for V-003; general corrected/as-known queries, successor lifecycle actions, and general conflict/non-convergence remain trigger-bound later pressure.

## Feedback assessment

The external feedback identified the right family and a strong first candidate. It also needs seven corrections before it can govern repository work.

1. **Zoey already owns the semantics.** The research is not deciding what belief, authority, correction, retirement, or continuity mean. It is looking for mechanisms and tests that preserve the existing canonical distinctions.
2. **Time is not a fixed five-column schema.** Occurrence, observation, claimed validity, effective interval, expiry, refresh, supersession, revocation, reconciliation, decision, activation, and recording time are state-dependent meanings. Each record should carry only the applicable typed meanings; XTDB's two database timelines do not replace the rest.
3. **“Belief” is too broad for acceptance criteria.** Research must distinguish current accepted state, current applicable state, corrected history, as-known-at-the-time history, attributed assertions, inferences, authority, and external projections.
4. **History preservation has a governed erasure exception.** Correction, supersession, retirement, forgetting, revocation, redaction, and deletion remain distinct. Audit preservation cannot override privacy or deletion obligations, and an erasure mechanism cannot be reported as ordinary correction.
5. **The proposed composition is a responsibility/source map, not an architecture.** [`XState`](https://github.com/statelyai/xstate)-like guards, [`XTDB`](https://github.com/xtdb/xtdb)-like bitemporality, event-store concurrency, [`Graphiti`](https://github.com/getzep/graphiti)-like episode lineage, and [`TerminusDB`](https://github.com/terminusdb/terminusdb)-like diffs may be useful independently. There is no basis to combine or adopt all of them.
6. **The candidate workflow must follow the register.** Raw repository names remain in this working shortlist. A candidate is registered when it enters source-bounded review and always before cloning, a workbench, or an adoption proposal. XTDB is registered as `EXT-STATE-001`; the other names are not yet registered candidates.
7. **A fixed monthly watch is premature.** Reviewed dates, exact source locks, and candidate-specific watch topics are sufficient now. Refresh before an experiment or decision, after a material upstream release/license change, or when an assessment has become too old for the claim being made. Do not create five comparison records or recurring monitoring merely to make the shortlist look active.

## In scope

- lifecycle and semantic distinction across assertions, observations, hypotheses, candidates, proposals, assessments, trials, dispositions, outcomes, corrections, conflicts, narrowing, supersession, retirement, and deletion;
- typed time meanings and bitemporal projection patterns;
- current, corrected-history, and as-known-at-the-time projections;
- correction without silent overwrite;
- transition guards and stale-basis rejection;
- source lineage and transition provenance;
- concurrency behavior, non-convergence, and explicit conflict;
- privacy-aware interaction between immutable history and governed erasure;
- tests that can strengthen the current scenario-provisional workbench without changing its accepted boundary.

## Out of scope

- final production memory schema or storage engine;
- durable personal-state retention or user-facing memory controls;
- a general Zoey event store, graph, state-machine framework, or workflow engine;
- automatic LLM promotion of extracted facts or contradictions;
- a durable repository under `projects/`;
- formal SCN-001 evaluation, scoring, or compatibility claims;
- treating SCN-001-derived abstractions as general Zoey architecture before SCN-002 counter-pressure.

## Completed sequence

1. The capability-bounded Iris/Yuki audit is preserved in [`LEGACY_AUDIT.md`](LEGACY_AUDIT.md).
2. The pinned [`XTDB`](https://github.com/xtdb/xtdb) review in [`../../external-capabilities/xtdb/ASSESSMENT.md`](../../external-capabilities/xtdb/ASSESSMENT.md) is source-review complete.
3. The extracted patterns pressured the implemented SCN-001 direct current-session correction and adversarial tests.
4. [`IMPLEMENTATION_REASSESSMENT.md`](IMPLEMENTATION_REASSESSMENT.md) reassesses every `SST-R01`–`SST-R12` requirement.
5. No concrete gap justifies registering [`XState`](https://github.com/statelyai/xstate), activating the XTDB experiment, or registering [`Graphiti`](https://github.com/getzep/graphiti).
6. [`TerminusDB`](https://github.com/terminusdb/terminusdb), [`KurrentDB`](https://github.com/kurrent-io/KurrentDB), and the WorldDB paper remain unregistered references because no narrower unsatisfied responsibility requires them.

## Proposed closure and reopening

Current evidence supports closure of the V-003 investigation because the corrected implementation demonstrates the applicable semantic distinctions, exact retained history, stale/substituted-basis rejection, realization-ownership ambiguity rejection, lineage/provenance separation, boundary preservation, narrow conflict behavior, and non-promotion limits without leaving a concrete mechanism uncertainty. Independent review of workbench commit `99772a8` was blocking because direct and focused realization claimant enumeration remained incomplete. The proposal is not accepted until corrected workbench commit `3efb7ca057369dd835f70fc120ced1ac5c175e0f` receives a fresh passing independent review.

Acceptance would not mean that every lifecycle action is implemented or that the whole semantic-state problem is complete. It would make this family dormant and trigger-bound. Reopen it when a trigger in [`REQUIREMENT_COVERAGE.md`](REQUIREMENT_COVERAGE.md) fires. Any future experiment still requires a concrete empirical question, minimal Zoey-owned contract, explicit non-goals, negative cases, predeclared invariants, applicable question re-triage, and a governed disposable boundary.
