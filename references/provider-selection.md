# Voice Identity And Provider Selection

Use this reference when choosing, creating, cloning, or changing a voice.

## Durable Voice Decision

Treat the provider as replaceable and the lawful Voice Identity Package as the durable asset. The package should contain:

- clean original recordings and exact transcripts;
- written consent, licence, and permitted business uses;
- voice personality, pacing, emotional range, and pronunciation guide;
- approved audition and reference outputs;
- provider, model, voice ID, settings, and dates tested;
- instructions and rights needed to recreate the voice with a successor provider.

Do not describe a provider-specific voice ID as owned or portable unless the provider contract explicitly grants that right.

## Human And Agent Responsibilities

- The human voice producer defines the character, gathers lawful source material, creates or auditions candidates, and gets approval.
- The approver selects the winning voice and permitted business uses.
- The human voice producer delivers a completed [Brand Voice Package](../assets/brand-voice-package-template.md), including the exact provider voice ID. Never send an API key in the package.
- The production agent uses the approved voice ID and locked settings. It must not redesign, clone, replace, or “improve” the identity without a new approval cycle.
- Keep a separate package for every venture and recurring character. Do not reuse a voice across ventures merely because it sounds suitable.

## Route Selection

Choose by the job, not by novelty.

- **Permanent branded voice:** use a ZedBiz-owned account and a provider that supports persistent private voices, commercial rights, reproducible settings, lossless output, and reliable API access. Run a same-script audition before committing.
- **Quick general narration:** use an approved stock voice through a ready native route when uniqueness is not required.
- **Temporary proof:** use the least expensive approved route and label the output as a proof, not the brand master.
- **Avatar or lip-sync input:** deliver the approved dry master or exact scene extracts. The avatar provider does not need to own the voice.
- **Conversational agent replies:** keep separate from production narration. Ordinary chat TTS should not activate this skill unless the user requests production audio.

## Current ZedBiz Provider Profile

Verify current availability, terms, model support, and price before use.

- **Fish Audio:** current preferred first candidate for durable Zeke and Maggie voice auditions because it supports voice design and sample-based cloning at low usage cost. It must still win the listening and consistency test.
- **ElevenLabs:** maturity and quality benchmark and approved fallback candidate when its account and API route are ready.
- **Gradium, Inworld, and MiniMax:** legitimate audition candidates when the job benefits from their cloning, voice-design, language, latency, or workspace features.
- **xAI/Grok Audio:** strong native stock-narration route on supported runtimes. Custom-voice availability and geography must be verified for the ZedBiz account; a Grok subscription or reasoning OAuth does not cover separately billed Voice API usage.
- **Percify:** approved audio and media provider. Use its live model discovery and cost tools. It may generate narration, but it is also a downstream avatar/lip-sync consumer of audio produced elsewhere.
- **OpenAI TTS and other stock routes:** useful for quick approved narration and fallback, but do not treat stock voices as unique ZedBiz brand identities.
- **Self-hosted voice engines:** consider only when privacy, scale, or provider independence justifies GPU hosting, maintenance, monitoring, and QA.

No provider should be selected solely because it is newly integrated into a platform.

## Fish Audio Through OpenClaw

- Use the official `@openclaw/fish-audio-speech` plugin and install the version compatible with the active OpenClaw runtime.
- Keep `FISH_API_KEY` in the approved secret manager and expose it through an environment SecretRef. Never place its value in skill files, agent prompts, manifests, or chat.
- Treat Fish API billing as separate from ordinary Fish platform credit. A `402` response means the API balance must be reviewed by the account owner; do not retry.
- Use hosted `s2.1-pro` for production unless a currently verified requirement supports another model.
- Keep automatic chat narration limited to explicitly tagged output when production agents share the same TTS provider.
- A Fish voice must be created, trained, or selected in Fish before OpenClaw can use it. OpenClaw consumes the approved `speakerVoiceId`; it does not create the voice identity.
- For a temporary route proof without an approved voice ID, use the default Fish voice and label the result `default-voice-proof`. Never present it as a brand voice.
- After generation, download the real MP3 or other requested audio file, inspect it, listen to it, and attach it to the thread or save it at the requested destination. A remote link alone is incomplete.
- Record model, voice ID, script version, expressive tags, output filename, duration, cost when available, and approval state.

## Controlled Audition

Use one script containing:

- ordinary conversational lines;
- brand names, Alberta and Saskatchewan place names, acronyms, numbers, and calls to action;
- calm, energetic, trustworthy, and persuasive passages;
- a sentence long enough to reveal pacing and breath behavior.

Keep script, language, speed, and output format as comparable as the providers allow. Score:

- identity fit and memorability;
- naturalness and emotional control;
- pronunciation and repeat consistency;
- noise, clipping, artifacts, and long-form stability;
- generation speed and failure behavior;
- account ownership, consent, terms, and provider survivability;
- current cost per approved minute, including plan minimums and failed attempts.

Save the results and approval decision. Do not casually change a recurring brand voice after downstream production begins.

## Percify-Specific Rules

- Confirm the `percify` connection with live model or avatar discovery.
- Inspect the selected model schema immediately before generation.
- Estimate credits before submitting paid work.
- Use approved reference audio only.
- Record the model, voice or avatar ID, job ID, estimate, actual credits, script version, and downloaded output.
- Do not submit duplicate jobs because polling is slow.
- A successful model listing proves access, not output quality. A paid or controlled generation proves the end-to-end route.

