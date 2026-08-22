# ZedBiz Skill Implementation Profile

## Identity And Ownership

- Organization and owner: ZedBiz
- Namespace: `z-`
- Canonical skill: `z-audio-production`
- Technical repository: `ZedBiz44/z-audio-production-Skill`
- Operational record: Z-Audio-Production-Skill-SOP in the Notion AI-Agent-Skills-SOPs database

## Supported Platforms

- Shared target: Codex, OpenClaw, and Hermes
- Pilot agent: Ruby on VPS3/Hermes
- Future consumer: `z-video-production`
- The canonical shared core remains provider-neutral and portable.

## Operating Controls

- Get-er-Done Mode: build the smallest working approved route, test immediately, and record evidence.
- Diagnose Mode: investigate and propose; make no changes until confirmation.
- Require consent for voice cloning, approval for material paid generation, and explicit authorization for production-impacting deployment.
- Test one agent first, verify, then expand.
- Stop after two failed paid attempts for the same unit or three failed validation/repair attempts.
- Roll back to the last committed and approved skill version.

## Sources Of Truth

- GitHub owns skill files, scripts, tests, and deployment evidence.
- Notion owns the business-readable SOP, ownership, approvals, and operating summary.
- The Notion SOP links to GitHub and must not duplicate the complete `SKILL.md`.
- Record activities and changes in the repository issue and Cody's Technical Documentation daily journal.

## Security

- Secrets remain in 1Password or the approved runtime secret mechanism.
- Never commit provider keys, complete environment files, private voice samples, or confidential consent records.
- Store only secure references to restricted assets in manifests and documentation.
