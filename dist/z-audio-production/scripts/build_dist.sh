#!/bin/bash
mkdir -p dist/z-audio-production/references
mkdir -p dist/z-audio-production/assets
cp SKILL.md dist/z-audio-production/
cp references/provider-selection.md dist/z-audio-production/references/
cp references/audio-workflows.md dist/z-audio-production/references/
cp references/quality-gates.md dist/z-audio-production/references/
cp references/implementation-profile.md dist/z-audio-production/references/
cp references/security-review.md dist/z-audio-production/references/
cp -r assets/* dist/z-audio-production/assets/ 2>/dev/null || true
mkdir -p dist/z-audio-production/scripts
cp -r scripts/* dist/z-audio-production/scripts/ 2>/dev/null || true
echo "Build complete."
