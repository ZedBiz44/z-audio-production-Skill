---
name: z-audio-production
description: Use for approved narration and production audio packages.
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
- Use the [Brand Voice Package Template](assets/brand-voice-package-template.md) for the human-to-agent handoff.
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
- **Deliver:** Download and attach the requested audio file. A provider URL, job ID, or “still generating” message is not the deliverable.
- **Dry:** Keep narration dry (no music/effects).
- **Integrity:** Never invent job IDs or "it rendered."
- **Versioning:** Never overwrite an approved master. Version it.

## 5. Store The Production Package

- Use the **Video-Creation** Google Shared Drive as the permanent storage location for all ZedBiz audio and video production: [open the Shared Drive](https://drive.google.com/drive/folders/0AAlVr-SRjSeQUk9PVA).
- Treat Shared Drive ID `0AAlVr-SRjSeQUk9PVA` as the fixed root. Do not save the only retained copy in a personal My Drive, provider account, chat thread, or temporary VPS folder.
- Save project audio under `Ventures/<Venture>/Projects/<YYYY-MM-DD>-<Project-Name>/Audio/`. Put the approved full narration in `Master/`, exact scene extracts in `Scenes/`, and useful source or pronunciation references in `References/`.
- Save recurring voice identity records under `Ventures/<Venture>/Brand-Voice-Packages/<Voice-Name>/`. Keep source recordings, consent, and licence material in the restricted subfolder and grant access only to approved team members.
- Save the audio manifest, provider job reference, cost, settings, filenames, hashes when required, approval status, and Drive links under the project `Records/` folder.
- Local agent or VPS storage is temporary working space. After listening and technical checks, upload the retained files to the Shared Drive and verify them there before reporting completion.
- If the venture or project folder does not exist, create it under the fixed Shared Drive root when ordinary folder creation is authorized. Stop if the correct venture, permissions, or destination is unclear.

## 6. Create Derivatives From The Master

- The approved dry master is the timing and performance source.
- Do not regenerate the same line for a new pose or scene.
- Video owns visuals. Audio does not make avatars, B-roll, captions, or final video.

## 7. Failure And Stop Conditions

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
- [Brand Voice Package Template](assets/brand-voice-package-template.md) (New or changed recurring voice)


