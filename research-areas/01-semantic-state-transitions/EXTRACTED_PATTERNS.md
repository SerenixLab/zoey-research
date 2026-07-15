# Extracted Semantic-State And Temporal-Transition Patterns

Status: `source-review extraction complete; V-003 conclusion accepted`
Reviewed: `2026-07-15`
Primary external source: [`XTDB`](https://github.com/xtdb/xtdb) at the revision locked in [`../../external-capabilities/xtdb/SOURCES.lock.yml`](../../external-capabilities/xtdb/SOURCES.lock.yml)

## Status and authority

This document is the concise research extraction from the completed XTDB source-review phase, interpreted through Zoey's canonical constraints and the capability-bounded Iris/Yuki audit.

It is:

- a bounded research extraction;
- implementation and test pressure for SCN-001 direct current-session correction.

It is not:

- architecture or an ADR;
- a storage or database decision;
- permission to modify SCN-001 semantics opportunistically;
- a compatibility, benchmark, or formal evaluation claim;
- authorization for a dependency, clone, experiment, or workbench.

## Accepted reference patterns

1. **Separate domain/effective validity from storage-recording history.** When both meanings matter, record when a version applies independently from when the system recorded that version. Neither timestamp defines semantic truth or authority.
2. **Preserve as-known independently from corrected history.** A later correction may change today's best reconstruction without erasing what the system had recorded and could have used earlier.
3. **Bind consequential reads and decisions to a repeatable basis.** Historical reconstruction needs an exact visible-state basis, not only an approximate wall-clock time.
4. **Reject transitions whose material basis is stale.** A correction, activation, narrowing, or retirement must fail closed or re-enter evaluation when its relied-on evidence, scope, authority, policy, capability, or state has materially changed.
5. **Treat current state as a projection.** Current accepted or applicable state is derived from retained semantic objects and transitions; it is not the only retained record and is not equivalent to the latest write.
6. **Keep source lineage separate from transition provenance.** Evidence ancestry answers what a state depends on. Actor, policy, configuration, guard, and authority records answer why a transition was permitted.
7. **Keep lifecycle relationships distinct.** Conflict, narrowing, supersession, revocation, retirement, deletion, and erasure have different effects on current applicability, historical reconstruction, lineage, and retained artifacts.
8. **Treat erasure as exceptional and governed.** Ordinary correction preserves history. Erasure may intentionally remove historical queryability under a separate deletion basis and must account honestly for backups, logs, projections, and derived artifacts.
9. **Keep temporal mechanisms behind Zoey-owned contracts.** Database validity, transaction success, event ordering, and snapshot identity provide mechanisms only; Zoey retains semantic roles, dependency identity, authority, and promotion rules.
10. **Preserve a vendor-independent export path.** A future store must export semantic objects, transitions, lineage, and bases without making a vendor snapshot token or row-version identifier permanent Zoey identity.

## Rejected mappings

The source review explicitly rejects:

```text
valid time       == semantic truth
system time      == observation time
database row     == authoritative Zoey state
latest write     == accepted correction
transaction pass == authority
event history    == sufficient provenance
immutable history == unlimited retention permission
erasure          == correction
snapshot token   == permanent Zoey object identity
```

These mappings remain invalid even if a storage engine implements them conveniently.

## Legacy and external synthesis

The bounded conclusion is:

```text
Iris-like lifecycle and promotion discipline
    + XTDB-like corrected/as-known temporal projection concepts
    + Zoey-owned semantic roles, dependency identity, and authority
    -> useful contract pressure
```

It is not:

```text
Iris + XTDB -> adopted architecture
```

Iris supplies the strongest implemented legacy lifecycle discipline inspected for this family. XTDB supplies the strongest reviewed corrected-history/as-known and repeatable-basis pattern. Yuki remains a useful negative/reference case: it has correction-shaped current-state fields and passive snapshot inspection without an implemented correction history.

No evidence supports combining the systems or importing their topology into Zoey.

## Conclusions from direct-correction pressure

- Explicit owned transitions and exact closure tests are sufficient; no general statechart mechanism is required.
- The selected-slice run-scoped store preserves enough immutable object, relation, order, and transition evidence for passive reconstruction.
- V-003 requires exact retained objects and transitions, not a corrected-history/as-known query pair, because the new spontaneous-session control does not correct the earlier focused-drill instruction's truth or scope.
- Stale, substituted, ambiguous, and retargeted bases fail closed with the owned dependency-identity mechanism.
- The required relationship is scoped coexistence. Supersession, narrowing, contradiction, revocation, and retirement are deliberately not asserted.
- Competing current evidence withholds a disposition and multiple outputs are not arbitrated. General conflict objects and cyclic non-convergence remain later pressure.
- No unanswered mechanism question justifies the XTDB experiment, XState registration, or Graphiti registration.

## Preserved SCN-001 invariants

Apply the following as implementation and test invariants only:

1. A correction has its own stable identity.
2. It binds to the exact state, realization, behavior occurrence, or retained evidence being corrected.
3. The corrected object is not mutated into the correction.
4. Current state is a projection rather than the only retained record.
5. A materially stale correction or activation basis fails closed.
6. Narrowing, contradiction, revocation, supersession, retirement, and deletion are not aliases.
7. Earlier as-known state remains passively inspectable unless a separate governed erasure rule applies.
8. Correction does not automatically create a durable adaptation.
9. Research mechanisms must not expose fixture/oracle-only data to the SUT.
10. No XTDB type, SQL term, snapshot token, or database topology enters the SCN-001 semantic contract from this research alone.

Observed evidence and deferred gaps are recorded in [`IMPLEMENTATION_REASSESSMENT.md`](IMPLEMENTATION_REASSESSMENT.md) and [`REQUIREMENT_COVERAGE.md`](REQUIREMENT_COVERAGE.md). Register [`XState`](https://github.com/statelyai/xstate), activate the contingent XTDB experiment, or register [`Graphiti`](https://github.com/getzep/graphiti) only if a recorded reopen trigger creates a concrete unanswered mechanism question.
