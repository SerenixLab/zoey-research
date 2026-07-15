# Initial Semantic-State Candidate Shortlist

Status: `working shortlist`  
Reviewed: `2026-07-15`

This file records reviewed search direction, not adopted candidates. Only XTDB has entered source-bounded candidate review and is registered as `EXT-STATE-001`. Other repository names remain search-queue items until registered.

## Prioritization

| Project | Narrow responsibility worth studying | Primary incompatibility or uncertainty | Next action |
| --- | --- | --- | --- |
| [`xtdb/xtdb`](https://github.com/xtdb/xtdb) | Bitemporal rows; corrected versus as-known queries; stable query bases; transaction assertions. | Database validity is not Zoey semantic validity; no authority or lifecycle meaning; single-writer topology and no native foreign keys. | Registered and `source-reviewed`. Apply extracted patterns to SCN-001; no clone, experiment, or workbench. |
| [`statelyai/xstate`](https://github.com/statelyai/xstate) | Executable transition guards, hierarchical statecharts, path generation, and model-based tests. | Snapshots and actor events do not supply authoritative history, evidence lineage, or temporal truth. | Register only if the direct-correction implementation leaves a concrete lifecycle/test-generation question. |
| [`getzep/graphiti`](https://github.com/getzep/graphiti) | Episode-to-fact lineage, validity windows, incremental graph integration, and hybrid retrieval. | Ingestion and contradiction handling rely substantially on LLM/embedding output; derived graph facts must remain candidates. Opt-out telemetry and backend/provider custody also require review. | Register after XState only if episode lineage remains a live need. |
| [`terminusdb/terminusdb`](https://github.com/terminusdb/terminusdb) | Structured diffs, immutable commits, versioned graph/schema, and time-travel review. | Commit history is not domain validity or transition authority; branch merge does not determine semantic admissibility. | Keep as later pattern source for human-readable change review. |
| [`kurrent-io/KurrentDB`](https://github.com/kurrent-io/KurrentDB) | Expected-revision checks, atomic append patterns, and event-native replay. | Event occurrence is not epistemic or authority status; custom licensing and infrastructure weight weaken dependency fit. | Extract concurrency patterns only unless a later experiment proves a unique need. |

## Secondary search hits

[`LangGraph`](https://github.com/langchain-ai/langgraph), [`Temporal`](https://github.com/temporalio/temporal), [`Automerge`](https://github.com/automerge/automerge), and [`Dolt`](https://github.com/dolthub/dolt) remain possible later search hits for durable execution, recovery, local-first convergence, and reviewable data history. They are not source-inspected or prioritized in this pass. Their names do not establish candidate status or evidence.

## Paper-only watch

[`WorldDB`](https://arxiv.org/abs/2604.18478) proposes content-addressed immutable nodes and programmed edge behaviors where supersession closes validity, contradiction preserves both sides, and identity merging produces a proposal. These concepts align with Zoey's no-silent-merge boundary.

The paper is currently treated as author-reported, paper-only evidence. No public implementation was identified in this pass, and its LongMemEval results do not establish Zoey compatibility, authority safety, or reproducibility. Do not create a mechanism candidate without source and artifact evidence.

## Verified repository snapshots

| Project | Inspected revision | Verification note |
| --- | --- | --- |
| [`XTDB`](https://github.com/xtdb/xtdb) | `e98610e1de12074d17943aa282b4a0391539de33` | GitHub commit API and revision-pinned source/docs verified 2026-07-15. |
| [`XState`](https://github.com/statelyai/xstate) | `c25dba07a2b68565edbe83d83c5d679dd85e00b2` | GitHub commit API verified 2026-07-15; not yet a candidate review. |
| [`Graphiti`](https://github.com/getzep/graphiti) | `526dcad7a300f3c5c506ff96a68bcdc7ca9f97ed` | GitHub commit API verified 2026-07-15; commit itself is a CLA-only change, so capability claims must use revision-pinned files rather than the commit message. |
| [`TerminusDB`](https://github.com/terminusdb/terminusdb) | `d2249d171ea5f287dbb882cd8f1826b99c57e282` | GitHub commit API verified 2026-07-15; not yet a candidate review. |
| [`KurrentDB`](https://github.com/kurrent-io/KurrentDB) | `67a6419ef9d5b8dc5496722f3dd3f7b5e5d54f8a` | GitHub commit API verified 2026-07-15; not yet a candidate review. |

Exact roles and evidence sources are recorded in [`SOURCES.lock.yml`](SOURCES.lock.yml).
