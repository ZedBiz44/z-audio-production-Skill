# Codex Adapter

- Install the committed skill folder into the active Codex skills root through the approved installer or deployment workflow.
- Keep `SKILL.md` frontmatter limited to `name` and `description`.
- Keep `agents/openai.yaml` synchronized with the canonical name and trigger.
- Do not assume Codex media plugins exist because a provider is named in this skill. Confirm the actual callable tool or connected app.
- Run the Skill Creator quick validator and test triggering in a fresh task after installation.
- Treat the GitHub repository as the authoring source and the installed folder as a replaceable deployment copy.
