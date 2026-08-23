---
name: z-audio-production
description: Create, revise, inspect, and package production-ready narration, branded voices, TTS, voice clones, audio masters, and video-ready audio handoffs.
---

# Z Audio Production

Produce an approved, reusable audio package without taking over the visual production job. Treat the approved dry master as the timing and performance source for every downstream consumer.

## 1. Establish The Job (Select Lane)

Confirm the project, script, voice route, deadline, and cost ceiling. Choose the appropriate production lane:

**Rapid Execution Lane** (For quick social media, temporary proofs, or internal TTS)
- Use an approved stock voice (e.g., Grok, OpenAI TTS).
- Bypass the formal audition matrix.
- Generate native provider files (no mandatory 48 kHz WAV or JSON manifest unless requested).

**Brand Voice / Client Lane** (For recurring brand identities, voice clones, or video handoffs)
- Require a Voice Identity Package and explicit consent.
- Run a controlled same-script audition if the voice is new.
- Deliver a 48 kHz PCM WAV dry master and a completed JSON audio manifest.

## 2. Enforce Rights And Identity Controls

- **Consent:** Require recorded permission before cloning or imitating a real person. Possession of a recording is not consent.
- **Identity:** Keep source recordings, consent references, and provider settings in a Voice Identity Package.
- **Portability:** Do not claim a provider voice ID is portable. Preserve original sources to recreate the voice elsewhere.

## 3. Verify The Production Route

- Confirm the tool/API is callable. Documented capability ≠ live route.
- Estimate the whole assignment before paid work. Stop if it exceeds the user budget or the organization limit. For ZedBiz work, the default is **$2.00 cumulative only when Get-er-Done authority applies**; follow the [ZedBiz implementation profile](references/implementation-profile.md).
- Do not silently change provider, model, voice, or language.
- *Avatar Routing:* For a disposable proof or approved non-brand rapid job, provider-native avatar audio may be used when it is the simplest reliable route and a usable dry master is retained. For recurring voices, approved brand identities, or lip-sync-critical work, keep an independent approved dry master and give the avatar tool exact extracts from that master.

## 4. Produce The Approved Dry Master

- **Listen:** Script-in means script-out. Listen to the whole file. Do not report done without a real playable file you heard.
- **Dry:** Keep narration dry (no music/effects).
- **Integrity:** Never invent job IDs or "it rendered."
- **Versioning:** Never overwrite an approved master. Version it.

## 5. Create Derivatives From The Master

- The approved dry master is the timing and performance source.
- Do not regenerate the same line for a new pose or scene.
- Video owns visuals. Audio does not make avatars, B-roll, captions, or final video.

## 6. Failure And Stop Conditions

- One transient retry after checking real job status.
- Two paid failures on the same unit → stop.
- Stop when consent, ownership, or budget is unresolved.
- Follow the [security and rollback review](references/security-review.md) for data privacy, credentials, and rollback procedures.

## References (Load as needed based on Lane)
- [Provider Selection & Auditions](references/provider-selection.md) (Brand Voice)
- [Audio Workflows](references/audio-workflows.md) (Brand Voice)
- [Quality Gates](references/quality-gates.md) (Brand Voice)
- [Audio-To-Video Handoff](references/video-handoff.md) (Video Handoff)
- [Audio Manifest Template](assets/audio-manifest-template.json) (Brand Voice / Handoff)
- [Production Brief Template](assets/audio-production-brief-template.md) (Brand Voice)
