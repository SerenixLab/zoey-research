# XTDB External Capability Assessment

Status: `researching`  
Priority: `high`  
Reviewed: `2026-07-15`  
Register ID: `EXT-STATE-001`  
Adopted dependency: `no`  
Active workbench: `no`

## Decision

XTDB is the strongest first architecture and pattern-extraction reference for corrected-history versus as-known-at-the-time projections. Keep it in source-bounded review; do not adopt it, clone it into Zoey, create a workbench, or treat bitemporality as Zoey's semantic model.

The useful extraction is narrow:

```text
row valid-time interval
    -> possible mechanism for an application-declared effective interval

row system-time history + query snapshot
    -> possible mechanism for as-recorded and repeatable historical projections

transaction ASSERT
    -> possible mechanism for rejecting a transition whose stored basis is stale
```

All meanings of assertion, observation, inference, authority, proposal, correction, activation, applicability, conflict, retirement, and erasure remain Zoey-owned.

## Exact Zoey need

This review addresses capability-map area 1:

- preserve direct current-session correction as distinct from later candidate or active trial state;
- avoid destructive overwrite when a later correction changes the current projection;
- distinguish effective/domain time from when a version entered the store;
- reconstruct current, corrected-history, and as-known-at-the-time views;
- reject activation or correction based on materially stale state;
- retain enough source and transition basis for inspection without making the database authoritative for semantics.

It does not decide production memory, durable personal retention, or a final storage responsibility.

## Pinned upstream facts

At `xtdb/xtdb` commit `e98610e1de12074d17943aa282b4a0391539de33`:

- XTDB automatically maintains `_system_from`, `_system_to`, `_valid_from`, and `_valid_to` on every table.
- System time represents the audit history of record changes and when information entered the system. Valid time is user-managed and can represent out-of-order updates, backfills, or domain validity.
- Ordinary queries default to the latest processed system state and valid time as of the query clock. Explicit `FOR VALID_TIME` and `FOR SYSTEM_TIME` clauses expose corrected and historical views.
- Queries execute against a basis containing a transaction snapshot plus a clock time. A `SNAPSHOT_TOKEN`, rather than only a wall-clock timestamp, is the repeatable upper bound on visible transactions.
- Non-interactive DML transactions are serialized through a totally ordered log. `ASSERT` rolls back the transaction when its predicate is false, enabling atomic invariant checks.
- Transaction metadata can carry correlation or lineage identifiers into `xt.txs`.
- `ERASE` irrevocably removes matching documents across all valid and system time so earlier system-time queries no longer return them.
- XTDB uses a single-writer architecture. The pinned key-concepts documentation says it has no native foreign keys and no uniqueness concept beyond `_id`; other integrity rules must be expressed by the application or transaction logic.
- The inspected source license is MPL-2.0.

These are XTDB capabilities, not evidence that Zoey implements or should adopt them.

## Semantic mapping

| XTDB mechanism | Potential Zoey use | Boundary that must remain explicit |
| --- | --- | --- |
| Valid-time interval | Application-declared period in which a semantic version is effective or applicable. | Valid time is not truth, confidence, observation time, decision time, authority, or current applicability unless Zoey explicitly defines that mapping for the object. |
| System-time history | When a stored version entered or left the database's recorded view. | Database system time is not necessarily event occurrence, Zoey observation, user assertion, model inference, decision, or activation time. |
| Current/default projection | Efficient current effective-state read. | “Current row” does not prove accepted authority or valid transition basis. |
| `FOR VALID_TIME` | Corrected domain-history projection. | Later correction can change this projection; consumers must know they are not seeing the original as-known view. |
| `FOR SYSTEM_TIME AS OF` | As-recorded-at-a-prior-basis projection. | Reconstructing the semantic decision also requires behavior configuration, source lineage, actor, policy, and dependency state outside the temporal row version. |
| `SNAPSHOT_TOKEN` | Repeatable query basis and evidence-package reference. | A snapshot covers stored XTDB transactions, not unrecorded external state or a model/runtime configuration. |
| `ASSERT` | Atomic stale-basis or invariant rejection within a DML transaction. | Zoey must define the material basis, dependency closure, and re-evaluation disposition. A successful predicate does not confer authority. |
| Transaction metadata | Correlation to request, actor, policy, or evidence package. | Metadata is only an attached reference unless referential closure and content identity are validated by Zoey. |
| `ERASE` | Possible low-level mechanism for an applicable deletion obligation. | Erasure is not correction, forgetting, retirement, or revocation. It destroys historical queryability and needs separate evidence plus derived-copy handling. |

## What the feedback got right

XTDB directly demonstrates the otherwise easy-to-miss difference between:

1. the history currently believed to be correct;
2. the history that the system recorded at an earlier point;
3. the current effective view.

It also makes temporal queries ordinary database operations rather than a convention of ad hoc audit tables. That is a strong architecture reference for Zoey's projection requirements.

The feedback was also right that bitemporality is insufficient. Zoey's canonical temporal meanings are broader and conditional. Observation, decision, activation, expiry, refresh, supersession, revocation, and reconciliation cannot be collapsed into either XTDB timeline.

## Important limitations added by this review

### Valid time is application-declared

XTDB cannot tell whether a row's valid interval means occurrence, claimed validity, active applicability, or effective policy time. A misclassified inference can be stored bitemporally with perfect fidelity and still be semantically wrong.

### Historical rows do not reconstruct a decision

An as-known row version does not by itself identify:

- the source event or assertion;
- the epistemic status and uncertainty;
- the actor and authority basis;
- the policy and behavior configuration;
- the dependencies tested for activation;
- the reason a correction superseded, narrowed, conflicted with, or merely coexisted with earlier state.

Zoey still needs source lineage, transition provenance, and effective configuration identity.

### `ASSERT` is a mechanism, not a lifecycle

An assertion can atomically reject a stale database predicate, but Zoey must decide what happens next: withhold, re-evaluate, narrow, conflict, retire, or request clarification. External state not represented in the same transaction basis can still become stale.

### Integrity is substantially application-owned

The lack of native foreign keys and general uniqueness constraints increases the burden on Zoey-owned contracts for dependency identity, source closure, typed relations, and deletion propagation. A flexible temporal store could preserve invalid graphs unless application checks fail closed.

### Immutability has a deliberate erasure exception

The feedback described immutable history without emphasizing `ERASE`. That exception is useful for privacy obligations but prevents the stronger claim that every past belief is always reconstructible. Any design must specify which projection, tombstone, audit fact, or derived artifact may survive a governed erasure.

### Operational topology is not neutral

The single-writer design provides straightforward serialization but creates throughput, latency, availability, deployment, backup, and migration questions. None is justified by the current selected-slice need, which can still be served by a smaller scenario-provisional mechanism.

## Legacy comparison

Iris already provides an implemented transition table, fail-closed illegal-transition rejection, source-bound memory candidates, explicit review promotion, expiry, deletion, and source revocation. Its implementation is closer to Zoey's lifecycle-control need than XTDB is.

XTDB adds what the inspected Iris capability lacks: native corrected versus as-known history, stable query bases, and database-level temporal versioning. Iris adds what XTDB lacks: candidate semantics, review authority, source eligibility, and explicit promotion boundaries.

Yuki's runtime playbook has correction and provenance-shaped fields and exposes a current snapshot, but the inspected implementation does not establish correction mutation, supersession, or historical projections. XTDB is therefore useful pressure against treating a versioned JSON snapshot as temporal correction history.

The likely extraction is complementary, not substitutive:

```text
Zoey/Iris-like owned lifecycle and promotion controls
    + XTDB-like temporal projection and basis concepts
    -> candidate contract to test later, not an adoption decision
```

## Standard research rubric

Ratings follow [`../../METHOD.md`](../../METHOD.md) and are qualitative source-review judgments, not benchmark scores.

| Dimension | Rating | Basis |
| --- | --- | --- |
| Requirement alignment | `strong` for temporal projections; `conditional` overall | Directly addresses corrected versus as-known history and repeatable query bases, but not semantic roles or authority. |
| Semantic compatibility | `conditional` | Compatible only when valid/system time are treated as storage mechanics under Zoey-owned meanings. |
| Modularity | `conditional` | SQL is a clear boundary, but adopting the database is an infrastructure commitment and temporal columns can leak into domain semantics. |
| Inspectability | `strong` for row history; `weak` for semantic decisions | Temporal queries and transaction records are inspectable; decision basis and authority remain application-owned. |
| User control | `weak` upstream | Query/update/erase mechanisms exist, but no Zoey user-review, correction, revocation, or explanation UX exists. |
| Privacy and custody | `conditional` | Self-hosting and erasure are useful; backups, replicas, logs, derived artifacts, and metadata custody still require design and evidence. |
| Evaluation quality | `unknown` for Zoey | Pinned documentation is strong mechanism evidence; no Zoey fixture, workload, failure, or migration experiment exists. |
| Operational maturity | `conditional` | Serialized transactions and snapshot bases are strong; single-writer topology and current constraint limitations require target-specific assessment. |
| Maintenance | `conditional` | Active upstream at the inspected revision; no Zoey compatibility or upgrade policy exists. |
| License and assets | `conditional` | MPL-2.0 is identified at the pinned source; any distribution or modification posture needs review before adoption. |
| Replaceability | `conditional` | SQL and explicit exports may help, but authoritative temporal history could become tightly coupled to XTDB semantics and snapshot tokens. |
| Identity assumptions | `strong` | XTDB is infrastructure and does not posit a competing agent identity. |

## Workbench trigger

Do not create a workbench merely to demonstrate that bitemporal SQL works. A controlled experiment becomes justified only if direct-correction implementation or later extraction leaves this concrete question unanswered:

> Can a minimal Zoey-owned semantic contract use XTDB temporal projections and transaction assertions to preserve late correction, as-known reconstruction, and stale-basis rejection without leaking XTDB's row-validity model into Zoey semantics?

The contingent plan is recorded in [`BENCHMARK_PLAN.md`](BENCHMARK_PLAN.md). Before activation, re-triage any open questions triggered by retained state, formal comparison, trust boundaries, or durable repository proposals.

## Claims this review does not support

- Zoey needs a temporal database.
- XTDB should become Zoey's memory layer or system of record.
- Two timestamps are sufficient for Zoey.
- XTDB valid time represents semantic truth or user authority.
- Immutable storage satisfies provenance, correction, privacy, or deletion by itself.
- `ASSERT` provides a complete concurrency or transition-control solution.
- Passing a future database spike would establish SCN-001, memory, continuity, or production readiness.

## Current disposition

```text
temporal-pattern value:          high
current selected-slice adjacency: high
semantic completeness:           low
mechanism adoption evidence:      none
operational evidence for Zoey:    none
action now:                       finish pattern review; no experiment yet
adoption now:                     no
```

See [`SOURCES.lock.yml`](SOURCES.lock.yml) for the exact inspected revision and files.
