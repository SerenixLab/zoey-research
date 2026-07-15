# Zoey External Candidate Register

Status: `active research index`  
Method: [`METHOD.md`](METHOD.md)  
Capability landscape: [`CAPABILITY_MAP.md`](CAPABILITY_MAP.md)

This is the authoritative index of external projects that have entered Zoey research. It is not a dependency manifest, adoption list, product roadmap, or formal evaluation record.

## Registered candidates

| ID | Capability area | Candidate | Classification | Status | Current disposition | Evidence record |
| --- | --- | --- | --- | --- | --- | --- |
| `EXT-STATE-001` | `1` Semantic state and transitions | [`XTDB`](https://github.com/xtdb/xtdb) | `architecture-reference`, `pattern-extraction-source`, conditional `mechanism-candidate` | `source-reviewed` | Bounded temporal-projection source review complete; retained as a reference with only a contingent experiment path. No storage choice, dependency, clone, compatibility claim, or workbench is active. | [`external-capabilities/xtdb/`](external-capabilities/xtdb/ASSESSMENT.md) |
| `EXT-VOICE-001` | `13` Conversational voice stack | Qwen3-TTS | `mechanism-candidate`, `pattern-extraction-source`, `archive-watch-candidate` | `watchlisted` | Strong multilingual voice-design and cloning candidate; no code, weights, runtime, or compatibility claim adopted. | [`external-capabilities/qwen3-tts/`](external-capabilities/qwen3-tts/ASSESSMENT.md) |

`flybirdxx/ComfyUI-Qwen-TTS` is recorded inside `EXT-VOICE-001` as a reference-only community adapter, not as an independently adopted candidate.

## Register rules

- Search queues and repository names that have not been reviewed belong in working notes, not this register.
- Each ID is stable. A renamed or superseded upstream keeps its historical ID and records the relationship.
- One candidate may cover several capability areas, but the primary area and exact need must remain clear.
- Status changes require a dated evidence update; attractive demos or upstream popularity do not change status.
- A workbench result remains experimental evidence until the applicable evaluation and decision controls authorize a stronger claim.
