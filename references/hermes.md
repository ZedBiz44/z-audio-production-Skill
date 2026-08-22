# Hermes Adapter

- Inspect the current Hermes installation, persistent skill path, and active tool inventory before deployment.
- Keep Ruby-specific configuration, credentials, voice IDs, projects, and runtime data outside the distributable skill.
- Use Hermes environment or credential metadata for secret requirements; never embed API keys.
- Confirm whether a provider is native, MCP-backed, plugin-backed, or reached through a ZedBiz adapter.
- On Ruby, xAI/Grok Audio may serve stock narration and Percify is a verified connected media route; Fish requires a reviewed Hermes plugin or ZedBiz adapter before it can be treated as live.
- Test discovery and a no-cost or explicitly approved controlled request in a fresh session.
- Treat the persistent host/repository copy as the source of the mounted container skill; do not create a competing container-only copy.
