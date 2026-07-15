# XTDB Contingent Mechanism Experiment Plan

Status: `planned, contingent, not authorized or active`  
Candidate: `EXT-STATE-001`

## Activation question

Run this experiment only if source review and the SCN-001 direct-correction implementation cannot answer:

> Can XTDB supply bounded temporal and stale-basis mechanisms behind a Zoey-owned contract without defining the semantic meaning of correction, authority, or applicability?

Demonstrating generic XTDB time travel is not sufficient reason to activate the plan.

## Preconditions

- Re-triage the applicable Zoey open questions for the actual experiment scope.
- Keep all fixtures synthetic and run-scoped; do not introduce real personal-state custody.
- Pin the exact XTDB source, image/package, JVM/runtime, configuration, and storage format.
- Decide whether the experiment is disposable or a governed workbench; do not create a durable `projects/` boundary without `REPO-001`.
- Define artifact retention and deletion for database files, logs, backups, and exported results.
- Predeclare invariants and failure criteria before implementation.

## Owned boundary

The experiment must define semantic objects and transitions outside XTDB. The adapter may expose operations such as:

```text
record_version(semantic_object, effective_interval, source_lineage)
propose_transition(expected_basis, transition_intent)
commit_if_current(expected_basis, transition_evidence)
project_current(query_basis)
project_corrected_history(valid_interval, query_basis)
project_as_known(snapshot_token, clock_time)
erase_under_authorized_policy(target, evidence)
```

These are experiment responsibilities, not accepted API names.

## Required fixtures

1. **Late correction:** version B arrives after its effective start and corrects version A.
2. **As-known reconstruction:** query before and after B was recorded while holding domain time constant.
3. **Stale activation:** two transitions share basis A; the first changes the basis and the second must fail its atomic assertion.
4. **Narrowing:** an active state becomes inapplicable in one scope without making its source assertion false.
5. **Unresolved conflict:** two supported states coexist and the current projection must report conflict instead of selecting the later write.
6. **Configuration reconstruction:** historical decision evidence references an exact synthetic behavior configuration outside the XTDB row version.
7. **Governed erasure:** erase one source-bearing object, then verify declared consequences for history, dependents, exports, backups, and residual metadata.
8. **Crash/restart:** repeat projections and stale-basis behavior after a cold restart.

## Measurements and evidence

- exact SQL and adapter inputs for every transition;
- transaction result, assertion outcome, and snapshot token;
- current, corrected-history, and as-known query outputs;
- object, source, transition, and behavior-configuration references;
- cold and warm query latency only as descriptive evidence, not a product target;
- database size and history growth for the bounded fixture set;
- restart, export, migration, and erasure observations;
- explicit list of semantics enforced by Zoey code versus XTDB.

## Acceptance basis

The mechanism remains viable for later study only if:

- ordinary correction preserves earlier as-known state;
- the three projections remain observably distinct;
- a stale transition fails atomically and produces an inspectable re-evaluation basis;
- source lineage and transition provenance remain separate and reconstructable;
- narrowing and conflict are not encoded as destructive overwrite;
- the adapter prevents raw valid-time fields from becoming semantic authority;
- erasure behavior is honest about lost history and residual artifacts;
- export can recover authoritative semantic objects without requiring XTDB-specific snapshot tokens as permanent identity.

## Rejection signals

- application code must duplicate or reverse-engineer XTDB temporal behavior to preserve correctness;
- valid time becomes an overloaded substitute for multiple Zoey meanings;
- historical projection depends on unpinned wall-clock approximation rather than a repeatable basis;
- stale-basis protection cannot cover the material dependency set;
- referential or deletion integrity requires an unbounded bespoke layer;
- operational footprint exceeds the scenario-provisional need;
- migration loses semantic identity or corrected/as-known distinctions;
- privacy erasure cannot meet the declared scope without unsupported claims.

Passing this experiment would establish only a bounded mechanism result. It would not select a production store, authorize personal-state retention, prove memory behavior, or establish a formal SCN-001 evaluation result.
