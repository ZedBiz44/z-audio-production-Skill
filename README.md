# Z Audio Production

This repository is the technical source of truth for `z-audio-production`, which guides approved narration and production-audio packages from brief through delivery.

## When to Use This Skill

- Plan or produce approved voiceover, narration, sound design, music, or a complete audio package.
- Revise an existing audio asset while preserving the approved brief and delivery constraints.
- Check audio deliverables against the requested format, rights, identity, and approval requirements.

## When Not to Use It

- Use it for a standalone video, image, logo, or publishing assignment with no audio-production scope.
- Generate paid media or imitate a person’s voice without appropriate authority and consent.
- Change an approved voice, message, offer, format, or brand treatment without approval.

## Authoritative Source and Repository Contents

`SKILL.md` is the authoritative runtime guide. The repository root is the authoritative technical source, while operational SOPs or governed business records remain in their approved operational systems.

- `SKILL.md` is the authoritative runtime guide and defines the skill contract.
- `agents/openai.yaml` provides runtime discovery metadata for supported OpenAI-compatible environments.
- `references/` contains focused guidance that the runtime instructions may load when needed.
- `assets/` contains templates or other resources directly required by the skill.
- `scripts/` contains deterministic validation and, where required, package-build helpers.

## Validation and Deployment

This lean repository has no local build or validator. Before release, check that the frontmatter in `SKILL.md` is valid, every referenced resource exists, the runtime can discover the skill, and one representative approved task completes as expected.

## Safety and Approval Boundaries

Respect rights, consent, brand constraints, and the approved scope. Do not use protected voices, music, or source material without authorization, and do not release a deliverable until it meets the agreed brief.

## Status and Contributions

Keep this README aligned with the actual skill contract and file structure. Make changes through version control, validate them before release, and document material deployment or governance decisions in the repository’s approved records.
