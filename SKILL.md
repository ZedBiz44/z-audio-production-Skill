---
name: z-audio-production
description: Create, revise, inspect, and package production-ready narration, branded voices, TTS, voice clones, audio masters, and video-ready audio handoffs.
---

# Z Audio Production

Produce an approved, reusable audio package without taking over the visual production job. Treat the approved dry master as the timing and performance source for every downstream consumer, including the future `z-video-production` skill.

## Establish The Job

Confirm or derive:

- project, audience, purpose, language, speaker, and delivery channel;
- final approved script and script version;
- voice route: approved brand voice, approved cloned voice, approved stock voice, or audition required;
- pronunciation, pace, tone, emotion, and accessibility requirements;
- required master and delivery formats;
- output folder, deadline, cost ceiling, and approval owner;
- whether downstream work needs the full master, timecoded segments, a lip-sync-safe copy, or all three.

Do not spend credits or clone a voice from a draft script. If the script is not final, create only a clearly labelled proof when the user authorizes one.

## Enforce Rights And Identity Controls

- Require recorded permission before cloning or imitating a real person.
- Never infer permission from possession of a recording.
- Keep source recordings, transcripts, consent or licence references, pronunciation rules, and provider settings in a Voice Identity Package.
- Keep credentials in the approved secret manager or runtime environment. Never place secret values in prompts, files, logs, or this skill.
- Do not claim that a provider voice ID is portable. Preserve the original lawful source material and approved outputs so the voice can be recreated elsewhere.

Read [Voice identity and provider selection](references/provider-selection.md) when selecting, creating, or changing a voice.

## Verify The Production Route

- Confirm the selected tool, API, MCP, plugin, or local engine is callable in the current runtime.
- Verify the actual account, model, voice ID, supported inputs, output formats, limits, and current price before paid generation.
- Distinguish documented capability, configured access, and an end-to-end tested route.
- Do not assume a reasoning-model subscription or OAuth login pays for a separate audio API.
- Do not silently change providers, voices, models, or languages.

For provider-specific operating constraints, read [Voice identity and provider selection](references/provider-selection.md). For target-platform placement and discovery, read the relevant adapter: [Codex](references/codex.md), [OpenClaw](references/openclaw.md), or [Hermes](references/hermes.md).

## Choose The Execution Lane

Use **Rapid Production** when the job uses an existing approved brand voice or an approved stock voice for a one-off narration, temporary proof, training item, or short promotion. Do not run a new audition matrix. Still verify the live route, estimate cost, label proofs, perform quality checks, and preserve the output record.

Use **Brand Voice Creation** only when creating or materially changing a recurring voice such as Zeke, Maggie, or another durable identity. Run the controlled audition and approval process before full production.

For a talking-avatar handoff, choose only the audio route:

- keep an established recurring brand voice with its approved master-audio provider and hand the exact approved audio to the avatar workflow;
- for a proof or non-brand job, the avatar provider may create the audio when its native voice is already approved, the combined route is demonstrably faster or less expensive, and a reusable dry master can be retained;
- never replace an established voice merely to save one provider step.

The future `z-video-production` skill still owns avatar generation and visual production.

## Approve A New Brand Voice

For a new or materially changed recurring voice:

- use one controlled script across candidates;
- generate short, low-cost auditions before the full narration;
- compare identity, naturalness, pronunciation, emotional range, consistency, artifacts, latency, cost, account control, and long-term survivability;
- record the chosen provider, model, voice ID, settings, and approval evidence;
- lock the approved identity for the production.

For an already approved voice, confirm its recorded identity and settings rather than auditioning again.

## Produce The Approved Dry Master

- Generate the complete narration from the final script before avatar, caption-timing, or scene assembly work begins.
- Keep narration dry: no music, sound effects, or video-specific mixing in the authoritative master.
- Listen to the complete file. Check every word, pronunciation, pause, pace, emotion, noise, clipping, truncation, and voice consistency.
- Correct the smallest failed unit. Do not regenerate approved passages without a reason.
- Save a lossless production master. For video handoff, prefer 48 kHz PCM WAV unless the receiving system specifies another format.
- Never overwrite an approved master. Create a new version and identify which version is current.

Read [Audio production workflows](references/audio-workflows.md) for narration, auditions, cleanup, segmentation, and revision rules.

## Create Derivatives From The Master

- Derive scene audio, previews, compressed copies, transcripts, and timing files from the approved master.
- Cut scene segments only at approved timecodes, preferably at breaths or natural pauses; never through words.
- Never independently regenerate the same line for a different avatar pose or scene. That breaks timing and performance continuity.
- Preserve the full master as the authoritative soundtrack. Downstream tools may receive exact extracts, but they must not replace the master.
- Keep music, effects, ducking, visible captions, and video assembly outside this skill.

Read [Audio-to-video handoff contract](references/video-handoff.md) whenever audio will feed avatar, lip-sync, caption-timing, or video production.

## Inspect And Package

- Run `scripts/inspect_audio.py` on every master and representative derivatives.
- Record duration, codec, sample rate, channels, bit depth when available, file size, and any specified loudness or peak measurements.
- Use listening review as well as technical inspection; valid metadata does not prove a good performance.
- Complete the manifest using [the audio manifest template](assets/audio-manifest-template.json).
- Use [the production brief template](assets/audio-production-brief-template.md) when the project has no controlling brief.
- Apply [the quality and completion gates](references/quality-gates.md) before approval.

## Output Package

Deliver only the files the job needs, normally:

- approved lossless dry master;
- optional review copy;
- optional scene-safe extracts;
- final script and pronunciation notes;
- transcript or timing data when requested;
- Voice Identity Package reference;
- manifest containing provider, model, voice, settings, job IDs, cost, filenames, hashes when required, approvals, and QC results.

Use stable, versioned names. A video project normally receives `audio/master/`, `audio/scenes/`, `audio/references/`, and `records/audio-manifest.json`, but follow an existing project structure when one is authoritative.

## Video Boundary

This skill may prepare and hand off audio for video. It must not own:

- avatar or lip-sync video generation;
- B-roll, stock footage, or image generation;
- character visuals or scene direction;
- visible caption styling or rendering;
- Remotion timelines, video editing, compositing, or final video export.

The future `z-video-production` skill should call this skill, accept its approved package, and leave the master audio unchanged unless a new audio approval cycle is opened.

## Failure And Stop Conditions

- Follow the user's stated budget or the approved organization implementation profile. Without either, stop before paid work.
- Treat the applicable micro-budget as the estimated total for the entire assignment, including segments and expected retries—not as a per-call allowance.
- Never use a micro-budget to create or clone a new recurring voice, buy a subscription, top up credits, or spend in Diagnose Mode.
- Retry one clearly transient failure after checking final job status.
- After two failed paid generations for the same unit, preserve evidence and stop; do not burn credits through blind retries.
- Stop when consent, ownership, provider access, voice identity, script version, or output destination is unresolved.
- Preserve the last approved master and manifest before any revision or rollback.
- Report the exact failed unit, provider job ID, cost impact, retained files, and decision needed.

## Completion Report

Report:

- approved master path and version;
- provider, model, voice identity, and script version;
- duration and technical format;
- derivative and manifest paths;
- estimated and actual cost when available;
- listening and technical QC results;
- approval status and downstream handoff recipient;
- any unproven capability, open risk, or blocked step.
