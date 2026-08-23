#!/bin/bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
target="$repo_root/dist/z-audio-production"

if [[ "$target" != "$repo_root/dist/z-audio-production" ]]; then
  echo "Refusing to clean unexpected package path: $target" >&2
  exit 1
fi

rm -rf -- "$target"
mkdir -p "$target/references" "$target/assets" "$target/scripts"
cp "$repo_root/SKILL.md" "$target/"
cp "$repo_root/references/provider-selection.md" "$target/references/"
cp "$repo_root/references/audio-workflows.md" "$target/references/"
cp "$repo_root/references/quality-gates.md" "$target/references/"
cp "$repo_root/references/implementation-profile.md" "$target/references/"
cp "$repo_root/references/security-review.md" "$target/references/"
cp "$repo_root/references/video-handoff.md" "$target/references/"
cp "$repo_root/assets/"* "$target/assets/"
cp "$repo_root/scripts/inspect_audio.py" "$target/scripts/"
echo "Build complete."
