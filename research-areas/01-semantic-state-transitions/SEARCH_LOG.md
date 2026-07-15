# Semantic-State Research Search Log

Status: `XTDB source-review pass complete`
Date: `2026-07-15`

## Inputs

- External feedback supplied by the user, including five primary repositories, four secondary references, and the [`WorldDB`](https://arxiv.org/abs/2604.18478) paper.
- [`../../CAPABILITY_MAP.md`](../../CAPABILITY_MAP.md) area 1.
- Zoey state/control, open-question, selected-slice, and dependency-identity sources at the baselines already recorded in the capability map.

## Local review

- Compared the feedback with the canonical time, provenance, lifecycle, correction, concurrency, deletion, and storage-independence requirements.
- Inspected the SCN-001 direct-correction frontier and state/projection exclusions.
- Performed a capability-bounded Iris/Yuki audit recorded in [`LEGACY_AUDIT.md`](LEGACY_AUDIT.md).

## Upstream verification

- Verified all five cited repository commits through GitHub's read-only commit API.
- Inspected [`XTDB`](https://github.com/xtdb/xtdb)'s temporal, query-basis, transaction, assertion, erasure, key-concept, and license files at the exact registered revision.
- Checked current official [`XState`](https://github.com/statelyai/xstate) guard, persistence, and testing documentation for shortlist plausibility.
- Checked the official [`Graphiti`](https://github.com/getzep/graphiti) repository and Zep documentation for episode provenance, temporal fact fields, provider/backend requirements, and telemetry posture.
- Checked current official [`TerminusDB`](https://github.com/terminusdb/terminusdb) documentation for schema, immutable commit history, structured diffs, branches, and time-travel behavior.
- Checked current official [`KurrentDB`](https://github.com/kurrent-io/KurrentDB) documentation for expected-state checks and atomic multi-stream append behavior, plus the official license-change notice.
- Verified the [`WorldDB`](https://arxiv.org/abs/2604.18478) paper metadata and abstract on arXiv; no implementation repository was identified by the searches performed.

## Claim handling

- Moving documentation was used to assess current shortlist plausibility.
- Registered [`XTDB`](https://github.com/xtdb/xtdb) claims rely on revision-pinned repository files listed in its candidate lock.
- The four unregistered repository entries remain working-notes evidence even though their cited commits were verified.
- Community issue reports were treated only as risk signals, not authoritative capability facts.
- No repositories were cloned, no weights or artifacts were downloaded, and no benchmark was run.
- [`XTDB`](https://github.com/xtdb/xtdb)'s reviewed revision did not change during reassessment; the existing pinned evidence was sufficient to produce the extracted-pattern and requirement-coverage records.
