# ZedBiz Implementation Profile: z-audio-production

## Identity And Ownership

- **Organization:** ZedBiz
- **Canonical skill:** `z-audio-production`
- **Technical repository:** `ZedBiz44/z-audio-production-Skill`
- **Authoritative branch:** `main`
- **Operational record:** `Z-Audio-Production-Skill-SOP` in the Notion AI-Agent-Skills-SOPs database
- **Human approver:** ZedBiz business owner or delegated approver

## Supported Use

- Use the shared skill on any supported AI-agent runtime where the skill is installed and the required provider or media tools are verified live.
- Do not assign permanent ownership of a voice, provider, or production lane to an individual AI agent.
- Select the production agent from current availability, permissions, project access, and tool readiness.

## Operating Controls

- **Get-er-Done Mode:** build the smallest approved working route, test promptly, and record real evidence.
- **Diagnose Mode:** investigate and propose; do not generate paid media or change production systems before confirmation.
- **Micro-budget:** up to USD $2.00 cumulative estimated provider spend per assignment when Get-er-Done authority applies. This excludes subscriptions, credit purchases, voice cloning, new recurring identities, Diagnose Mode, destructive actions, and production deployment.
- Require consent for voice cloning, approval for a new or materially changed recurring voice, and authorization for spending above the approved limit.
- Stop after two failed paid attempts for the same unit or three failed validation or repair attempts.

## Technical Package And Rollback

- **Deployment package:** `dist/z-audio-production/`
- Include every runtime resource linked from `SKILL.md`.
- Test one authorized runtime first, verify discovery and representative behaviour, then expand.
- Roll back to the last committed and approved skill version and restore its matching deployment package when a material failure occurs.

## Source And Record Boundaries

- GitHub owns skill files, scripts, tests, packaging, and deployment evidence.
- Notion owns the business-facing SOP, ownership, approvals, and operating explanation.
- Changing provider preferences, fleet readiness, pilot assignments, prices, and release evidence belong in GitHub issues or Technical Documentation rather than this profile.
- Secrets, private voice samples, and consent records remain in approved restricted storage. Store only secure references in manifests and documentation.

## Trigger Boundaries

- **Positive:** "Create approved narration for this final script using the existing brand voice."
- **Positive:** "Prepare this approved dry master and scene extracts for video production."
- **Negative:** "Create a talking-avatar video." Route the visual production to `z-video-production`; use this skill only for its audio package when needed.
