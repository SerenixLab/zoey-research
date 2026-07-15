# Semantic State, Correction, And Temporal Transition Research Brief

Status: `active research direction`  
Reviewed: `2026-07-15`  
Capability area: `1` Semantic state and transitions  
Current engineering adjacency: `SCN-001` direct current-session correction

## Decision

Adopt this as the first capability-family research direction. Do not adopt the proposed multi-framework composition as architecture, choose a storage engine, create a workbench, or broaden the current SCN-001 milestone from this research alone.

The near-term question is narrower than a general memory architecture:

> Which external patterns help Zoey preserve semantic distinctions, correction history, temporal meaning, transition basis, and inspectable projections while direct current-session correction is implemented?

The family is valuable because the canonical state/control model already requires non-destructive history, typed temporal meanings, basis re-evaluation, and visible conflict handling. External research should pressure and operationalize those requirements, not redefine them.

## Feedback assessment

The external feedback identified the right family and a strong first candidate. It also needs seven corrections before it can govern repository work.

1. **Zoey already owns the semantics.** The research is not deciding what belief, authority, correction, retirement, or continuity mean. It is looking for mechanisms and tests that preserve the existing canonical distinctions.
2. **Time is not a fixed five-column schema.** Occurrence, observation, claimed validity, effective interval, expiry, refresh, supersession, revocation, reconciliation, decision, activation, and recording time are state-dependent meanings. Each record should carry only the applicable typed meanings; XTDB's two database timelines do not replace the rest.
3. **“Belief” is too broad for acceptance criteria.** Research must distinguish current accepted state, current applicable state, corrected history, as-known-at-the-time history, attributed assertions, inferences, authority, and external projections.
4. **History preservation has a governed erasure exception.** Correction, supersession, retirement, forgetting, revocation, redaction, and deletion remain distinct. Audit preservation cannot override privacy or deletion obligations, and an erasure mechanism cannot be reported as ordinary correction.
5. **The proposed composition is a responsibility/source map, not an architecture.** XState-like guards, XTDB-like bitemporality, event-store concurrency, Graphiti-like episode lineage, and TerminusDB-like diffs may be useful independently. There is no basis to combine or adopt all of them.
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

## Research sequence

1. Preserve the capability-bounded Iris/Yuki audit in [`LEGACY_AUDIT.md`](LEGACY_AUDIT.md).
2. Complete the pinned XTDB review in [`../../external-capabilities/xtdb/ASSESSMENT.md`](../../external-capabilities/xtdb/ASSESSMENT.md).
3. Review XState next if lifecycle guards or path generation remain an unanswered mechanism question after the direct-correction implementation.
4. Review Graphiti only at the candidate/promotion boundary: episode lineage and temporal retrieval are useful, but LLM-derived graph mutations cannot be authoritative by default.
5. Review TerminusDB for inspectable semantic diffs and KurrentDB for expected-basis append patterns only if those responsibilities remain unsatisfied by smaller owned mechanisms.
6. Reconcile the extracted contracts against SCN-002 authority and operation pressure before claiming generality.

## Completion basis

This research family is ready to recommend an experiment only when it has:

- a concrete mechanism question not answerable from pinned source review;
- a minimal Zoey-owned semantic contract and explicit non-goals;
- legacy comparison and at least one negative case;
- synthetic fixtures for late correction, stale basis, narrowing, conflict, and erasure;
- predeclared projection and transition invariants;
- applicable open-question re-triage;
- a disposable or governed workbench boundary with no production or milestone claim.

Until then, the outcome is pattern extraction and requirements refinement only.
