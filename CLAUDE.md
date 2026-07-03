# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when operating in this directory.

## Nature of this directory

This is a personal utility scripts collection — not a software project. Scripts are standalone shell scripts and Python utilities for daily tasks: backups, file conversions, LLM model management, and Google Drive sync.

## Active scripts (current)

- `Google_Drive_sync` — Launches, monitors, and quits Google Drive sync via DriveFS log parsing
- `install_LLMs` — Installs local LLM models (set -e, one-shot)
- `build_qwen3.6_model` / `build_qwen2.5_model` / `build_gemma_model` — Build Ollama models from Modelfile_*, Modelfile_gemma4
- `run_claude_qwen` — Runs Claude via local LMStudio proxy (sets ANTHROPIC_* env vars)
- `safeguards` — rsync-based home directory backup to external drive
- `convert_olympus_videos.py` — Batch convert Olympus camera video files
- `upgrade_brew_npm_and_pip_packages` — System package updates

## Legacy subdirectories

- `old_routines/` — Older video processing scripts (mts_to_mp4, processdir variants)
- `old_process_dirs/` — Alternative video processing pipelines
- `old_backup_routines_for_mac/` — Archived backup scripts
- `recover dropbox commands/` — Dropbox-specific utilities
- `rclone/` — Rclone configuration/scripts

## Common patterns

- All shell scripts use `#!/bin/bash` shebang, most are executable (`chmod +x`)
- Python scripts are in the root; none have requirements files or virtual envs
- No tests, no CI, no package manager configuration
- Modelfile_*, Modelfile_gemma4 are Ollama model definition files
