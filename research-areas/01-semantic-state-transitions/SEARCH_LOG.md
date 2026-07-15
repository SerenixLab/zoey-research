# Semantic-State Research Search Log

Status: `initial pass`  
Date: `2026-07-15`

## Inputs

- External feedback supplied by the user, including five primary repositories, four secondary references, and the WorldDB paper.
- [`../../CAPABILITY_MAP.md`](../../CAPABILITY_MAP.md) area 1.
- Zoey state/control, open-question, selected-slice, and dependency-identity sources at the baselines already recorded in the capability map.

## Local review

- Compared the feedback with the canonical time, provenance, lifecycle, correction, concurrency, deletion, and storage-independence requirements.
- Inspected the SCN-001 direct-correction frontier and state/projection exclusions.
- Performed a capability-bounded Iris/Yuki audit recorded in [`LEGACY_AUDIT.md`](LEGACY_AUDIT.md).

## Upstream verification

- Verified all five cited repository commits through GitHub's read-only commit API.
- Inspected XTDB's temporal, query-basis, transaction, assertion, erasure, key-concept, and license files at the exact registered revision.
- Checked current official XState guard, persistence, and testing documentation for shortlist plausibility.
- Checked the official Graphiti repository and Zep documentation for episode provenance, temporal fact fields, provider/backend requirements, and telemetry posture.
- Checked current official TerminusDB documentation for schema, immutable commit history, structured diffs, branches, and time-travel behavior.
- Checked current official KurrentDB documentation for expected-state checks and atomic multi-stream append behavior, plus the official license-change notice.
- Verified the WorldDB paper metadata and abstract on arXiv; no implementation repository was identified by the searches performed.

## Claim handling

- Moving documentation was used to assess current shortlist plausibility.
- Registered XTDB claims rely on revision-pinned repository files listed in its candidate lock.
- The four unregistered repository entries remain working-notes evidence even though their cited commits were verified.
- Community issue reports were treated only as risk signals, not authoritative capability facts.
- No repositories were cloned, no weights or artifacts were downloaded, and no benchmark was run.
