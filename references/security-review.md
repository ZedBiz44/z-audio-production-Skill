# Security and Rollback Review

## Credential Handling
- **Rule:** Never place passwords, tokens, private keys, or API keys in the skill files, prompts, or logs.
- **Mechanism:** Use the approved secret manager or runtime environment variables (e.g., `FISH_API_KEY`, `PERCIFY_API_KEY`).

## Data Privacy & Consent
- **Voice Recordings:** Private voice recordings used for cloning must be stored in the designated secure ZedBiz cloud storage, not in public repositories.
- **Consent Records:** Written consent for voice cloning must be verified and recorded in the Voice Identity Package before generation begins.

## Paid Generation Limits
- **Threshold:** The agent is authorized to spend up to the $2.00 micro-budget per task without human intervention.
- **Enforcement:** The agent must estimate the cost of the job (including expected retries) before submitting the API request.

## Rollback & Removal
- **Conditions for Immediate Rollback:** Unauthorized spend, credential leakage in logs, or repeated API failures causing looping.
- **Procedure:** 
  1. Halt agent execution of the skill.
  2. Revert the `z-audio-production-Skill` repository to the last known-good commit.
  3. Re-deploy the `dist/` package to the agent's runtime environment.
