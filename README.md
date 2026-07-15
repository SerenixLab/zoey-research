# Zoey Research

This directory holds bounded, reproducible evaluations of external capabilities that may become useful to Zoey.

Research placement means:

- the capability is being observed or assessed;
- no dependency, repository boundary, compatibility claim, or production commitment has been accepted;
- upstream source remains externally owned;
- any later experiment must enter a governed workbench with its own source, artifact, and claim controls.

## Research System

- [`CAPABILITY_MAP.md`](CAPABILITY_MAP.md): capability-first landscape connecting Zoey needs, governance, current implementation, legacy signals, and external evidence gaps.
- [`METHOD.md`](METHOD.md): classifications, evaluation rubric, research sequence, and claim boundaries.
- [`CANDIDATE_REGISTER.md`](CANDIDATE_REGISTER.md): the authoritative index of external candidates that have entered review.
- [`tools/check_research.py`](tools/check_research.py): offline structural conformance for candidate records, research families, relative links, and repository artifact hygiene.

Capability-family research:

- [`Semantic state, correction, and temporal transitions`](research-areas/01-semantic-state-transitions/RESEARCH_BRIEF.md): delayed activation re-triaged after independently reviewed implementation; later-use applicability is next and wider research remains dormant.

Current external capability records:

- [`XTDB`](external-capabilities/xtdb/ASSESSMENT.md): source-reviewed reference for corrected/as-known projections and stale-basis mechanisms; not adopted.
- [`Qwen3-TTS`](external-capabilities/qwen3-tts/ASSESSMENT.md): high-priority future voice candidate; watchlisted, not adopted.

## Local Conformance

Run:

```text
python tools/check_research.py
```

The checker validates local record structure, status/classification agreement, required source-lock fields, relative Markdown links, obvious archive/model artifacts, conventional vendored-source directories, nested repository metadata, and repository files above the documented 5 MiB limit. It does not validate research truth, remote source freshness, legal compliance, compatibility, benchmark results, or adoption decisions.
