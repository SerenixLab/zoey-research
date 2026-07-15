# External Capability Records

Each candidate directory should contain:

- an assessment that separates evidence from recommendation;
- a machine-readable source lock with exact inspected revisions;
- a benchmark plan describing what evidence would be required before adoption.

The candidate must also be linked from `../CANDIDATE_REGISTER.md` and evaluated using `../METHOD.md`. A candidate directory does not imply that a benchmark, clone, or adoption is authorized.

Candidate status terms:

- `watchlisted`: worth monitoring; no implementation is active;
- `workbench-candidate`: bounded experimentation is justified but not yet started;
- `under-evaluation`: an explicitly governed workbench is producing evidence;
- `adoption-proposed`: evidence exists and an architectural decision is awaiting acceptance;
- `adopted`: an accepted decision and owned integration boundary exist;
- `rejected` or `superseded`: the recorded rationale explains why evaluation stopped.

Status progression is not automatic. A repository update, benchmark result, or attractive demo does not by itself adopt a capability.
