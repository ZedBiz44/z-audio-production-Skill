#!/usr/bin/env python3
"""Inspect WAV files with Python and other audio formats through ffprobe."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import wave
from pathlib import Path


def inspect_wav(path: Path) -> dict:
    with wave.open(str(path), "rb") as audio:
        frames = audio.getnframes()
        rate = audio.getframerate()
        return {
            "format": "wav",
            "codec": "pcm",
            "duration_seconds": round(frames / rate, 6) if rate else 0,
            "sample_rate_hz": rate,
            "channels": audio.getnchannels(),
            "sample_width_bits": audio.getsampwidth() * 8,
            "frames": frames,
        }


def inspect_with_ffprobe(path: Path) -> dict:
    executable = shutil.which("ffprobe")
    if not executable:
        raise RuntimeError("ffprobe is required for non-WAV files but was not found")
    command = [
        executable,
        "-v",
        "error",
        "-select_streams",
        "a:0",
        "-show_entries",
        "stream=codec_name,sample_rate,channels,channel_layout,bit_rate,duration:format=duration,bit_rate,format_name",
        "-of",
        "json",
        str(path),
    ]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    payload = json.loads(result.stdout)
    streams = payload.get("streams", [])
    if not streams:
        raise RuntimeError("no audio stream found")
    stream = streams[0]
    container = payload.get("format", {})
    duration = stream.get("duration") or container.get("duration") or 0
    return {
        "format": container.get("format_name", path.suffix.lstrip(".")),
        "codec": stream.get("codec_name", ""),
        "duration_seconds": round(float(duration), 6),
        "sample_rate_hz": int(stream.get("sample_rate") or 0),
        "channels": int(stream.get("channels") or 0),
        "channel_layout": stream.get("channel_layout", ""),
        "bit_rate": int(stream.get("bit_rate") or container.get("bit_rate") or 0),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect an audio file and verify basic invariants.")
    parser.add_argument("path", type=Path)
    parser.add_argument("--expected-sample-rate", type=int)
    parser.add_argument("--expected-channels", type=int)
    args = parser.parse_args()

    path = args.path.resolve()
    if not path.is_file():
        print(json.dumps({"ok": False, "error": "file not found", "path": str(path)}, indent=2))
        return 2
    if path.stat().st_size == 0:
        print(json.dumps({"ok": False, "error": "file is empty", "path": str(path)}, indent=2))
        return 2

    try:
        details = inspect_wav(path) if path.suffix.lower() in {".wav", ".wave"} else inspect_with_ffprobe(path)
    except (OSError, RuntimeError, subprocess.SubprocessError, json.JSONDecodeError, wave.Error) as exc:
        print(json.dumps({"ok": False, "error": str(exc), "path": str(path)}, indent=2))
        return 2

    checks = []
    if args.expected_sample_rate is not None:
        checks.append({
            "name": "sample_rate_hz",
            "expected": args.expected_sample_rate,
            "actual": details.get("sample_rate_hz"),
            "passed": details.get("sample_rate_hz") == args.expected_sample_rate,
        })
    if args.expected_channels is not None:
        checks.append({
            "name": "channels",
            "expected": args.expected_channels,
            "actual": details.get("channels"),
            "passed": details.get("channels") == args.expected_channels,
        })

    ok = all(check["passed"] for check in checks)
    print(json.dumps({
        "ok": ok,
        "path": str(path),
        "size_bytes": path.stat().st_size,
        "audio": details,
        "checks": checks,
    }, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
