# Zoey External Research Instructions

This tree records reproducible research about third-party capabilities. It does not contain adopted Zoey implementation or canonical governance.

When adding or updating a candidate:

- start from a capability gap in `CAPABILITY_MAP.md`, not from an interesting repository;
- register the candidate in `CANDIDATE_REGISTER.md` before cloning or proposing adoption;
- apply the classifications and evaluation dimensions in `METHOD.md` consistently;
- distinguish upstream facts, Zoey-specific assessment, and future proposals;
- pin every inspected source repository to an exact commit;
- record model identifiers separately from source revisions;
- do not claim model-weight reproducibility unless the weight revision or digest is pinned;
- do not vendor upstream source, copy model weights, or commit generated voice artifacts here;
- label community integrations as reference-only unless an explicit adoption decision says otherwise;
- keep benchmark plans honest about end-to-end behavior, hardware, cold versus warm state, and vendor-reported results;
- treat reusable voice prompts, embeddings, and reference recordings as potentially sensitive derived artifacts;
- re-triage applicable Zoey open questions before a candidate becomes a non-throwaway workbench or dependency.

Research records may recommend a future workbench. They may not create one merely to archive a repository or download weights.

Keep the capability map explicit about whether legacy coverage is merely signalled, initially reviewed, or audited. A filename or legacy design claim is not evidence that a capability is implemented or suitable for reuse.
