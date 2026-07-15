# Qwen3-TTS External Capability Assessment

Status: `watchlisted`  
Priority: `high`  
Reviewed: `2026-07-15`  
Adopted dependency: `no`  
Active workbench: `no`

## Decision

Qwen3-TTS is a strong future candidate for Zoey's voice surface, especially for multilingual synthesis, expressive control, voice design, and reusable voice cloning. Preserve and monitor the candidate now; do not vendor either reviewed repository, download model weights, or alter the current SCN-001 workbench.

The preferred future path is:

```text
Zoey voice specification
    -> Qwen VoiceDesign candidate recordings
    -> human review and approval
    -> approved synthetic reference recording
    -> reusable Base-model clone prompt
    -> Zoey-owned voice adapter boundary
```

This creates an original voice without beginning from an unconsented real-person clone. It does not eliminate the need to govern the resulting recording and prompt artifacts.

## Why it fits Zoey

The official release provides 0.6B and 1.7B variants across Base, CustomVoice, and VoiceDesign roles. It supports English, Italian, Japanese, and seven other languages. The Base models support rapid voice cloning; CustomVoice adds preset speakers and instruction-driven delivery; VoiceDesign creates a voice from a natural-language description.

That maps well to Zoey's likely needs:

- English for ordinary interaction;
- Italian for native-language interaction;
- Japanese for the longitudinal learning scenario when a real voice frontier is selected;
- instruction-controlled emotion, tone, rhythm, and prosody;
- an original voice-design workflow followed by reusable prompt extraction;
- a 0.6B/1.7B latency-versus-quality comparison.

These are upstream capability claims, not yet Zoey compatibility claims. Qwen's published quality and latency results are useful screening evidence but must be reproduced on Zoey's target hardware and interaction loop.

## Integration boundary

Use `QwenLM/Qwen3-TTS` as the authoritative technical upstream. If adopted later, Zoey should own a narrow adapter around the official package or an explicitly evaluated serving runtime. The adapter should expose capability-oriented operations rather than upstream classes directly:

```text
design_voice(specification, review_text)
build_voice_prompt(approved_reference, transcript, provenance)
synthesize(text, language, delivery, voice_prompt)
cancel(request_id)
inspect_runtime_capabilities()
```

The adapter contract should keep model loading, device selection, prompt custody, streaming support, cancellation, and observability explicit. No current Zoey repository has accepted responsibility for that boundary, so it belongs in a future voice workbench first.

## Streaming and latency qualification

The architecture and Qwen-hosted real-time APIs demonstrate credible streaming potential. They do not establish a ready local streaming integration for Zoey.

At the reviewed official commit:

- the Python wrapper states that `non_streaming_mode=False` simulates streaming text input and does not enable true streaming input or streaming audio generation;
- the documented vLLM-Omni path supports offline inference only, with online serving listed as future work;
- the advertised 97 ms result is a first-packet result under Qwen's optimized benchmark, not turn-end-to-first-audible latency for a complete assistant.

Any future benchmark must separately measure model first packet, application first playable buffer, first audible sound, and complete utterance time. A simulated-streaming result must not be reported as real streaming.

## Runtime and dependency risks

The official package is early and intentionally isolated-environment oriented. At the reviewed revision, `qwen-tts` is version `0.1.1` and pins `transformers==4.57.3` and `accelerate==1.12.0`. Official examples are CUDA-centric and recommend FlashAttention 2 where supported.

Apple Silicon evidence currently comes mainly from community adaptation work rather than an official support claim. MPS should therefore be classified as experimental until a Zoey benchmark reproduces correct output, memory behavior, and acceptable latency.

Model identifiers are recorded in `SOURCES.lock.yml`, but model weight revisions are deliberately unpinned because no weights were downloaded or inspected. A benchmark must pin exact weight revisions or digests before claiming reproducibility.

## Role of ComfyUI-Qwen-TTS

`flybirdxx/ComfyUI-Qwen-TTS` is a useful reference-only adapter and listening interface. It should not become Zoey's voice foundation because it bundles its own Qwen implementation and adds a second evolving compatibility surface.

Useful ideas to carry into a future Zoey adapter are:

- extract a reusable prompt once instead of recomputing it for every utterance;
- persist prompt metadata separately and validate model-size compatibility on load;
- key model caches by model and attention implementation;
- expose explicit model unloading for constrained memory;
- make device and attention fallback visible rather than silent;
- avoid naive punctuation-based independent generation after the adapter observed voice inconsistency across segments;
- treat ComfyUI results as evidence about that plugin configuration, not automatically about a direct integration.

The plugin's MPS fixes, dependency workarounds, saved-voice workflow, and later removal of pause-based segmentation are evidence of useful experimentation and of current integration fragility.

## Voice artifact controls

A reusable voice-clone prompt can contain encoded reference speech, a speaker embedding, cloning-mode flags, and a reference transcript. A generated reference recording may also be identifying or behavior-shaping. These are not harmless configuration files.

Before retaining or reusing any real prompt, the workbench must record at least:

- source and creation provenance;
- whether the source is synthetic or a real person;
- consent or other permitted-use basis;
- model identifier and exact weight revision;
- prompt construction parameters and transcript linkage;
- sensitivity, custody location, and encryption expectation;
- allowed surfaces and purposes;
- retention, deletion, rebuild, and backup implications;
- compatibility and invalidation behavior across model upgrades.

This is a planning constraint, not a substitute for resolving Zoey's deferred derived-artifact governance.

## Adoption gates

Do not move this candidate beyond `watchlisted` until all applicable gates are explicit:

1. A voice frontier and bounded workbench are selected without changing SCN-001's current claim scope.
2. `MEM-004`, `SURF-002`, and `PROD-003` are re-triaged, along with any trust-boundary, consent, continuity, or disclosure questions the experiment activates.
3. The official implementation is benchmarked directly on target hardware using the locked model revisions.
4. Local streaming is proven end to end or the product honestly declares a non-streaming/hosted boundary.
5. Voice identity stability, multilingual quality, cancellation, recovery, and artifact deletion meet predeclared acceptance targets.
6. License, generated-audio transparency, consent, and deployment obligations receive an appropriate review before external distribution.
7. An accepted responsibility boundary owns dependency updates, prompt custody, runtime isolation, and fallback behavior.

## Standard research rubric

Ratings follow [`../../METHOD.md`](../../METHOD.md) and are qualitative screening judgments, not benchmark scores.

| Dimension | Rating | Basis |
| --- | --- | --- |
| Requirement alignment | `strong` | Directly addresses multilingual TTS, voice design, expressive control, and reusable voice cloning within capability area 13. |
| Semantic compatibility | `conditional` | The model can remain a mechanism, but Zoey must own prompt provenance, permitted use, disclosure, and voice-surface controls. |
| Modularity | `strong` for official package; `weak` for ComfyUI foundation | The official API can sit behind a narrow adapter; the community plugin bundles a divergent implementation and UI runtime. |
| Inspectability | `conditional` | Source and prompt structures are inspectable, but model behavior, identity drift, and genuine streaming require measurement. |
| User control | `weak` upstream | Upstream generation APIs do not provide Zoey's required review, revocation, retention, or deletion lifecycle. |
| Privacy and custody | `conditional` | Local inference is possible, but reference recordings and reusable prompts are sensitive derived artifacts; hosted APIs cross a trust boundary. |
| Evaluation quality | `conditional` | Official benchmarks are useful screening evidence; no Zoey hardware, multilingual, stability, or end-to-end benchmark exists yet. |
| Operational maturity | `weak` | Local online serving, true wrapper streaming, cancellation, recovery, and production behavior are not established. |
| Maintenance | `conditional` | The upstream is active but young and pins a narrow dependency surface. |
| License and assets | `strong` for reviewed source/models | Reviewed source and model cards identify Apache-2.0; deployment still requires revision-specific verification. |
| Replaceability | `conditional` | A Zoey-owned adapter helps, but clone prompts and voice behavior may be model-version dependent. |
| Identity assumptions | `strong` if bounded | TTS need not create a second identity, provided the voice remains one replaceable expression mechanism of Zoey. |

## Current disposition

```text
potential quality:                 high
capability fit:                    high
multilingual fit:                  high
real-time architectural potential: high
ready local streaming integration: low
Apple Silicon readiness:           experimental
CUDA readiness:                    moderate
production maturity:               early
privacy/governance burden:         high
action now:                         record and monitor
adoption now:                       no
```

See [`SOURCES.lock.yml`](SOURCES.lock.yml) for exact inspected revisions and [`BENCHMARK_PLAN.md`](BENCHMARK_PLAN.md) for the future evidence plan.
