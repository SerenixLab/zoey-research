# Qwen3-TTS Future Benchmark Plan

Status: `planned, not authorized or active`  
Suggested future location: `workbenches/voice-qwen3-tts-spike/`

## Purpose

Produce Zoey-specific evidence about voice quality, identity stability, multilingual behavior, resource use, and genuine end-to-end latency. The benchmark must not imply that a TTS result proves a complete conversational voice stack.

## Preconditions

Before creating the workbench or downloading weights:

- explicitly select the voice frontier and workbench scope;
- re-triage `MEM-004`, `SURF-002`, and `PROD-003` plus applicable trust-boundary and consent questions;
- choose target Apple Silicon and/or CUDA hardware;
- pin every model weight revision or digest;
- define where caches, recordings, prompts, and results may be stored;
- declare whether network access is forbidden, permitted only for initial download, or part of a hosted-runtime comparison;
- predeclare acceptance targets for the intended product experience.

## Configurations

Run the official Qwen implementation directly as the primary evidence path:

1. `0.6B CustomVoice`: preset-voice latency and runtime baseline.
2. `0.6B Base`: lowest-cost reusable clone-prompt path.
3. `1.7B Base`: clone fidelity and identity-stability path.
4. `1.7B VoiceDesign -> approved reference -> 1.7B Base prompt`: original persistent Zoey voice path.

The ComfyUI adapter may be run as a separately labelled exploratory comparison for MPS, caching, and listening workflow. Its results must not be merged with official-runtime results.

For every configuration, record:

- source commit, package lock, model revision/digest, tokenizer revision, device, precision, and attention implementation;
- cold versus warm state and cache contents;
- generation parameters and random seed when applicable;
- reference audio provenance and prompt-construction mode;
- whether text input, audio output, both, or neither are truly streamed.

## Corpus

Use equivalent English, Italian, and Japanese suites with native-speaker review where possible:

- short acknowledgement and notification lines;
- ordinary conversational replies;
- long explanatory turns;
- numbers, dates, abbreviations, code-switching, and proper names;
- punctuation-heavy and punctuation-free variants;
- calm, warm, uncertain, excited, serious, and urgent delivery requests;
- interruption points at early, middle, and late generation;
- at least 20–50 repeated turns for identity drift evaluation.

Keep semantic content and length bands aligned across languages. Do not translate idioms mechanically when that would distort naturalness.

## Timing model

Measure these clocks separately:

```text
request accepted
    -> model begins generation
    -> first model audio chunk exists
    -> first playable application buffer exists
    -> first audible sound
    -> final audio chunk
    -> playback complete
```

Report at minimum:

- cold start and warm start;
- model first-packet latency;
- request-to-first-playable-buffer latency;
- turn-end-to-first-audible latency;
- total generation time;
- real-time factor and generated audio duration;
- p50, p95, maximum, sample count, and failure count.

If the API returns only a completed waveform, record it as non-streaming even when `non_streaming_mode=False` was used. Chunking completed audio after generation is not streaming.

## Quality and stability

Evaluate:

- intelligibility and transcription error;
- pronunciation and prosody in each language;
- perceived naturalness and instruction adherence;
- speaker similarity for clone configurations;
- identity drift across turns, long text, punctuation changes, and different emotions;
- unwanted environmental sound copied from a reference;
- deterministic versus sampled variation;
- text segmentation effects, especially independent punctuation chunks;
- clipping, silence, channel mismatch, truncation, looping, and hallucinated speech.

Retain raw ratings and measurement provenance. Do not collapse disagreement into a single unsupported quality label.

## Runtime behavior

Measure:

- peak and steady RAM, VRAM, or unified-memory use;
- model load and unload time;
- prompt creation and repeated prompt reuse time;
- cache hit/miss behavior and cache invalidation after parameter changes;
- cancellation latency and whether already-buffered audio stops;
- concurrent request behavior, overload handling, and isolation;
- crash recovery, restart recovery, corrupted prompt handling, and model mismatch rejection;
- network calls made during load and inference.

On Apple Silicon, verify output correctness before drawing performance conclusions. Record every MPS fallback or CPU operation. On CUDA, report FlashAttention and standard SDPA results separately where both are viable.

## Artifact manifest

Every retained reference recording or reusable prompt needs a manifest containing:

```yaml
artifact_id: stable-local-id
artifact_type: reference-recording | voice-clone-prompt
created_at: timestamp
source_kind: synthetic-voice-design | consented-human-reference
source_provenance: inspectable-reference
permitted_use: explicit-scope
model_id: exact-model-id
model_revision: exact-revision-or-digest
tokenizer_revision: exact-revision-or-digest
construction_parameters: inspectable-reference
sensitivity: explicit-classification
custody_location: governed-location
retention_basis: explicit-basis
deletion_and_rebuild: documented-procedure
compatible_runtime: exact-compatibility-claim
```

This manifest is an experiment requirement only. It does not resolve the canonical common contract deferred under `MEM-004`.

## Evidence package

The completed workbench should produce:

- an immutable environment and source lock;
- model weight digests or immutable revisions;
- machine-readable per-run measurements;
- listening samples with consent and disclosure constraints;
- failure logs and known-limit records;
- a comparison report that separates vendor claims, observed facts, and inference;
- an explicit recommendation: reject, continue watching, repeat on other hardware, propose adoption, or retain only as an exploratory tool.

Passing this benchmark would support a TTS-runtime decision only. It would not prove STT, endpoint detection, barge-in, conversational orchestration, actor assurance, private/shared disclosure, or full Zoey voice-surface readiness.
