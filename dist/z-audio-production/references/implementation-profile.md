# ZedBiz Implementation Profile: z-audio-production

## Governance & Risk
- **Risk Tier:** Fleet / Public (Handles paid API generation, private voice clones, and client deliverables).
- **Authoritative Branch:** `main`
- **Ownership:** ZedBiz Proprietary
- **Human Approver:** Jack (Required for budget overrides or new brand voice approvals).

## Deployment & Budgets
- **Auto-Approved Micro-Budget:** $2.00 cumulative per assignment. Any assignment estimated above this requires explicit human approval.
- **Deployment Package:** `/dist/z-audio-production/` (Contains only runtime-required files).
- **Rollback Procedure:** Revert to previous Git commit and restore previous `dist/` package.

## Provider Preferences (Current as of Aug 2026)
- **Fish Audio:** Preferred for sample cloning and durable brand voices (Zeke/Maggie).
- **ElevenLabs:** Benchmark and approved fallback.
- **Grok / OpenAI TTS:** Preferred for Rapid Execution stock narration.
- **Percify:** Preferred for downstream avatar integration.

## Triggers
- **Positive:** "Generate the audio for this script using the Zeke voice."
- **Negative (Do not trigger):** "Create a talking avatar video." (Route to video production).
