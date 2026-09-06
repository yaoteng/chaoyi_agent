#!/usr/bin/env python3
"""Render demo-30s.html to a sequence of PNG frames at fixed FPS."""
import os, subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HTML = ROOT / "demo-30s.html"
FRAMES = ROOT / "frames"
EDGE = Path("/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
if not EDGE.exists():
    EDGE = Path("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
DURATION_MS = 30000
DEFAULT_FPS = 15


def render(fps: int = DEFAULT_FPS, start: int = 0, end: int = None):
    if not EDGE.exists():
        print(f"Edge not found at {EDGE}", file=sys.stderr)
        sys.exit(1)
    FRAMES.mkdir(exist_ok=True)
    total_frames = int(round(DURATION_MS / 1000 * fps))
    if end is None:
        end = total_frames - 1
    step = DURATION_MS / (total_frames - 1) if total_frames > 1 else 0
    url_base = HTML.as_uri()
    started = time.time()
    for i in range(start, end + 1):
        t = int(round(i * step))
        if i == total_frames - 1:
            t = DURATION_MS
        out = FRAMES / f"frame_{i:04d}.png"
        if out.exists() and out.stat().st_size > 0:
            continue
        url = f"{url_base}?t={t}"
        cmd = [
            str(EDGE),
            "--headless",
            "--no-sandbox",
            "--disable-gpu",
            "--hide-scrollbars",
            "--window-size=1920,1080",
            f"--screenshot={out}",
            url,
        ]
        try:
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Frame {i} (t={t}) failed: {e}", file=sys.stderr)
            continue
        if (i - start) % 50 == 0 or i == end:
            elapsed = time.time() - started
            print(f"Rendered {i+1}/{total_frames} frames ({elapsed:.1f}s)")
    elapsed = time.time() - started
    print(f"Done range {start}-{end}: {total_frames} frames total -> {FRAMES}")


if __name__ == "__main__":
    fps = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_FPS
    start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    end = int(sys.argv[3]) if len(sys.argv) > 3 else None
    render(fps, start, end)
