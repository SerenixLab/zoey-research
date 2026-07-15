# Semantic State, Correction, And Temporal Transition Research Brief

Status: `outcome and explanation trigger re-triaged; wider research dormant`

Reviewed: `2026-07-15`

Capability area: `1` Semantic state and transitions

Current engineering adjacency: `SCN-001` formal evaluation gate (`EVAL-004` / `EVAL-005`)

## Decision

Accept closure of the Area 1 investigation required for the implemented V-003 engineering frontier. Fresh independent review passed the corrected evidence baseline. Retain the wider capability family as dormant and trigger-bound. Do not adopt the proposed multi-framework composition as architecture, choose a storage engine, create another workbench, or broaden the current SCN-001 milestone from this research alone.

The implementation question was narrower than a general memory architecture:

> Can Zoey preserve semantic distinctions, differently scoped history, temporal meaning, exact transition basis, and inspectable current applicability through direct current-session correction with its owned mechanism?

The independently reviewed corrected implementation supports a yes answer for the current frontier. The evidence and limits are recorded in [`IMPLEMENTATION_REASSESSMENT.md`](IMPLEMENTATION_REASSESSMENT.md) and [`REQUIREMENT_COVERAGE.md`](REQUIREMENT_COVERAGE.md). Exact retained objects and transitions are sufficient for V-003; general corrected/as-known queries, successor lifecycle actions, and general conflict/non-convergence remain trigger-bound later pressure.

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

## Accepted closure and reopening

The V-003 investigation is accepted closed because the corrected implementation demonstrates the applicable semantic distinctions, exact retained history, stale/substituted-basis rejection, realization-ownership ambiguity rejection, exact realization-ingestion parity, lineage/provenance separation, boundary preservation, narrow conflict behavior, and non-promotion limits without leaving a concrete mechanism uncertainty. Independent review of workbench commit `99772a8` was blocking because direct and focused realization claimant enumeration remained incomplete. Review of `3efb7ca` was also blocking because evaluation accepted a coherently extended simulator-ingestion participant set that the SUT rejected. Exact corrective commit `adf756a6765e433047574acec1d40e8da74005f4` closed that parity defect and received a fresh passing independent review.

Acceptance does not mean that every lifecycle action is implemented or that the whole semantic-state problem is complete. This family is dormant and trigger-bound. Reopen it when a trigger in [`REQUIREMENT_COVERAGE.md`](REQUIREMENT_COVERAGE.md) fires. Any future experiment still requires a concrete empirical question, minimal Zoey-owned contract, explicit non-goals, negative cases, predeclared invariants, applicable question re-triage, and a governed disposable boundary.

## Delayed-candidate trigger reassessment

The accepted delayed-candidate frontier fired one recorded reopen trigger. Workbench commits `a8aeff5` and `1784bfe` implemented exact formation of a separate, non-active candidate from raw retained bundle facts. The candidate has no behavior influence, preserves the exact future activation requirements, and uses typed lineage: every consumed participant is basis, epistemically favoring evidence is support, and the direct disposition is separately recorded as transition ancestry. Fresh independent review of the exact stack through `1784bfe` passed; governance closure is recorded at `d9d76df`.

This pressure did not expose an unanswered mechanism question. The owned explicit transition model represented formation, immutable non-active state, provenance, replay, and run isolation without a storage, statechart, graph, or temporal-database dependency. External candidate review and the contingent XTDB experiment therefore remain dormant.

## Delayed-activation trigger reassessment

The next bounded trigger was exercised by workbench stack `d9d76df..a355962`, with governance closure at `6728a9d`. The SUT now retains the unchanged candidate, a separate assessment that recomputes all nine checks from exact material basis, and a separate active delayed-correction trial with exact candidate-and-assessment ancestry. Activation does not consume a second user approval, does not treat V-003 as future-trial acceptance, and creates no preference, global policy, durable adaptation, or later behavior.

Independent review first blocked stack `d9d76df..4cf6af5` because evaluation accepted a competing retention-basis record that the SUT rejected. The corrected evaluator requires the same global singleton retention identity as the SUT. Fresh review of `d9d76df..a355962` passed with no further blocker. This trigger again exposed no external-mechanism gap: explicit owned transitions remain reviewable and exact. Wider research stays dormant; `DP-LATER-USE` applicability and scope counterpressure are the next engineering frontier.

## Later-use and realization trigger reassessment

The later-use trigger was exercised by corrected workbench stack `6728a9d..6f0cb02`, with governance closure at `ae0eba5`. Canonical spontaneous production now rechecks the same-run active delayed trial, creates a bounded later behavior disposition, and records exact matched realization. The mandatory focused-drill opt-in branch rechecks its own same-run trial, records `not_applicable`, emits nothing, and creates no disposition, realization, narrowing, supersession, retirement, or erasure.

Independent review first blocked `6728a9d..8285c83` because the opaque fixture state reference lacked ADR-007 projection metadata and a typed `projection_of` closure, and because SUT drill attribution did not require its creator pointer to equal the unique actual creator. Commit `6f0cb02` added a separate lineage-preserving projection and closed creator parity; fresh review passed with no further blocker. The correction exposed a missing local contract, not a need for an external state, graph, workflow, or temporal-database mechanism. Wider research remained dormant. At that checkpoint, `DP-OUTCOME-UPDATE` and `DP-EXPLAIN` became the next bounded engineering pressure and had to preserve intervention conditioning, causal limits, retained support, and uncertainty.

## Outcome and explanation trigger reassessment

The final bounded semantic trigger was exercised by corrected workbench stack `ae0eba57..b94dfda`, with governance closure at `4376bcc`. The SUT now records an intervention-conditioned association and a separate non-exhaustive uncertainty object after exact matched later behavior. It does not establish causality, long-term efficacy, global preference, fixed learning style, fatigue, or exclusion of private and unobserved causes. A separate explanation transition consumes the complete relevant retained lineage and explicit limitation records; hidden chain-of-thought is neither required nor retained.

Independent review first blocked `ae0eba57..f4422fa` because evaluator-owned canonical-premise fields crossed into and controlled the SUT, and because temporal-assessment result multiplicity differed across the boundary. Review of the first correction through `18365f6` found the inverse co-created-result parity gap. Commits `18365f6` and `b94dfda` keep the premise verdict evaluation-private, close every outbound uncertainty relation, and enforce global shared-result uniqueness in both SUT and evaluation. Fresh review of `ae0eba57..b94dfda` passed after 38 focused checks and all 345 aggregate tests.

This pressure again exposed local boundary and exact-closure defects, not an unanswered storage, statechart, graph, workflow, or temporal-database mechanism question. Wider Area 1 research remains dormant. The next workbench phase is formal evaluation and cannot begin until the separately governed `EVAL-004` and `EVAL-005` decisions are accepted; this research conclusion does not pre-solve them.
