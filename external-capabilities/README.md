# External Capability Records

Each candidate directory should contain:

- an assessment that separates evidence from recommendation;
- a machine-readable source lock with exact inspected revisions;
- a benchmark plan describing what evidence would be required before adoption.

The candidate must also be linked from `../CANDIDATE_REGISTER.md` and evaluated using `../METHOD.md`. A candidate directory does not imply that a benchmark, clone, or adoption is authorized.

Candidate status terms:

- `researching`: source-bounded review is active; no experiment or implementation is authorized;
- `source-reviewed`: the bounded source review is complete; the candidate is retained as an architecture reference, pattern source, watch target, or contingent experiment candidate, but no implementation, experiment, compatibility claim, dependency, or adoption is active;
- `watchlisted`: worth monitoring; no implementation is active;
- `workbench-candidate`: bounded experimentation is justified but not yet started;
- `under-evaluation`: an explicitly governed workbench is producing evidence;
- `adoption-proposed`: evidence exists and an architectural decision is awaiting acceptance;
- `adopted`: an accepted decision and owned integration boundary exist;
- `rejected` or `superseded`: the recorded rationale explains why evaluation stopped.

Status changes are explicit and non-monotonic. A repository update, benchmark result, or attractive demo does not by itself advance or adopt a capability. Refresh a `source-reviewed` record before an experiment, adoption proposal, or claim that depends on current upstream behavior.
