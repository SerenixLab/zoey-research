# Zoey External Research Method

Status: `active research method`  
Scope: `research/` only  
Canonical architecture authority: `none`

## Purpose

Zoey should learn from more than its thesis and the Iris/Yuki lineages. External systems, research implementations, established non-AI infrastructure, and negative examples can expose stronger mechanisms and failure modes.

The research unit is a Zoey capability need, not a repository:

```text
Zoey requirement
    + canonical control constraints
    + current implementation evidence
    + Iris/Yuki evidence
    + external patterns and components
    + negative evidence
    -> bounded recommendation
```

This method governs how candidates are collected and compared. It does not select final architecture, activate deferred questions, create a durable repository boundary, or authorize a dependency.

## Core rules

1. Define the capability gap and governing source before searching for projects.
2. Search beyond AI-assistant repositories when event sourcing, workflow, policy, local-first, provenance, recovery, or HCI projects solve the underlying problem better.
3. Compare external candidates with both Iris and Yuki before claiming that they fill a gap.
4. Separate implemented legacy evidence from specified, planned, archived, or merely named material.
5. Classify a candidate before cloning it. A repository may have more than one classification.
6. Prefer primary sources and exact inspected revisions. Keep model revisions separate from source-code revisions.
7. Extract a narrow pattern or contract when adopting a whole framework would import incompatible identity, authority, state, privacy, or lifecycle assumptions.
8. Treat security/privacy, observability/inspectability, and modularity/replaceability as cross-cutting gates.
9. Do not promote research or development runs into formal milestone evidence. The applicable `EVAL-004` and `EVAL-005` triggers remain authoritative.
10. Use a governed workbench only when a bounded experiment is justified; use `projects/` only after the applicable `REPO-001` decision basis is accepted.

## Candidate classifications

| Classification | Meaning |
| --- | --- |
| `mechanism-candidate` | Code or a service that may eventually run inside or behind Zoey. |
| `architecture-reference` | A design worth studying without copying its topology or ownership model. |
| `pattern-extraction-source` | A bounded subsystem, contract, algorithm, or operational technique is useful. |
| `evaluation-reference` | Fixtures, benchmarks, adversarial cases, or evaluation separation are useful. |
| `interoperability-reference` | Protocols, manifests, adapters, or migration contracts are useful. |
| `negative-reference` | The project demonstrates dangerous coupling, failure modes, or unsuitable assumptions. |
| `archive-watch-candidate` | Promising but immature, unsupported on target hardware, or not currently needed. |
| `rejected` | Evidence shows it is materially misaligned, unsafe, legally unsuitable, unmaintained, or not isolatable. |

Classification is distinct from status. For example, Qwen3-TTS is simultaneously a mechanism candidate, a pattern-extraction source, and an archive/watch candidate while its status remains `watchlisted`.

## Evaluation dimensions

Use qualitative ratings such as `strong`, `conditional`, `weak`, `unknown`, or `not applicable`. Avoid numeric scores unless the scoring rule and evidence are defined before evaluation.

| Dimension | Question |
| --- | --- |
| Requirement alignment | Which exact capability-map need does this address? |
| Semantic compatibility | Does it preserve Zoey's evidence, inference, authority, scope, and lifecycle distinctions? |
| Modularity | Can the useful responsibility be isolated behind a small owned contract? |
| Inspectability | Can decisions, state transitions, configuration, failures, and provenance be examined? |
| User control | Can relevant state, permissions, adaptations, and artifacts be reviewed, corrected, revoked, or deleted? |
| Privacy and custody | Can it respect destination-use policy, local custody, sensitivity, and deletion requirements? |
| Evaluation quality | Are tests, benchmarks, adversarial cases, baselines, and claim limits credible? |
| Operational maturity | Does it handle cancellation, overload, failure, restart, recovery, migration, and versioning? |
| Maintenance | Is ownership, release activity, documentation, and compatibility management credible? |
| License and assets | Can source, models, datasets, generated artifacts, and bundled assets be used as intended? |
| Replaceability | Can Zoey replace it without losing authoritative state or silently changing behavior? |
| Identity assumptions | Does it remain a mechanism, or does it assume a competing persistent agent identity or authority? |

## Research sequence

### 1. Capability inventory

Maintain `CAPABILITY_MAP.md` as the research-priority view connecting requirements, governance, implementation status, legacy signals, and missing external evidence.

### 2. Legacy coverage audit

For the selected capability, review the applicable Iris and Yuki implementation and current documents. Classify each item as:

```text
implemented candidate
adapt with rewrite
pattern/reference only
negative lesson
archive only
missing
```

This audit is capability-bounded. Do not treat a repository-wide README or old plan as a complete migration inventory. `LEG-001` through `LEG-004` still govern actual reuse or migration.

### 3. Targeted external search

Search one capability family at a time. Start with several candidates, deep-review only the strongest few, and preserve negative evidence where it prevents repeated mistakes.

### 4. Comparative extraction

For each requirement, state:

```text
best applicable legacy evidence
best external architecture pattern
best isolatable external component
known anti-pattern
remaining unresolved decision or experiment
```

### 5. Controlled experiment

Only candidates with a concrete unanswered empirical question receive a pinned clone, disposable or governed workbench, reproducible benchmark, artifact policy, and bounded compatibility claim.

## Minimum candidate record

Before a candidate can move beyond the register, record:

- capability-map area and exact Zoey need;
- classifications and current status;
- authoritative upstream and community/reference roles;
- exact inspected source revision;
- model/data/asset revision separately where applicable;
- evidence, inference, recommendation, and rejected alternatives;
- legacy comparison;
- rubric assessment;
- security, privacy, observability, and replaceability risks;
- trigger and acceptance basis for any future workbench;
- explicit claims that the research does not support.

## Claim boundary

Research may say that a project is promising, demonstrates a pattern, or justifies an experiment. It may not say that Zoey implements the capability, passes a scenario, is production-ready, or has accepted the architecture unless the corresponding governed evidence and decision artifacts exist.
