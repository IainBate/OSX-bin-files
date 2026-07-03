# OSX-bin-files

Personal macOS utility scripts for backups, file conversions, media management, and system administration.

## Backup & Sync

| Script | Description |
|--------|-------------|
| `backup_home_dir` | Archives home directory to tar/xz in ~/Downloads, extracts Movies/Pictures/compiled_videos separately |
| `camera_backup_local` | Rsync from SD card (`/Volumes/Untitled`) to dated local folder |
| `camera_backup_NAS` | Rsync from SD card to NAS (`/Volumes/raw_photos`) |
| `films_backup` | Rsync film collection from network share (`/Volumes/share/films/`) to CARAVAN drive (max 4GB/file) |
| `films_backup_directly_connected` | Same as above but from local `/Volumes/Home/films/` |
| `home_backup_full` | Rsync all `/Volumes/Home` subdirs to Google Drive over SSH |
| `home_backup_HD_attached` | Rsync iPhones from attached HDD to Google Drive via rclone |
| `home_backup_HD_not_attached` | Rsync iPhones/other_photos/GoPros from mounted volumes to Google Drive |
| `lucys_hard_drive` | Rsync films and iTunes music to Lucy drive (192.168.68.206) |
| `Malta backup` | Rsync Malta 2022 photos to Google Drive |
| `marvin_music` | Rsync iTunes music from MARVIN drive, clean m3u playlists |
| `digby_music` | Rsync iTunes music from DIGBY drive, clean m3u playlists |
| `raspberry_pi_backup` | Rsync from remote Raspberry Pi (`pi@144.32.50.117`) |
| `sd_backup` | Rsync SD card to NAS camera backups folder |
| `shared_backup` | Copy JSA PDFs to Google Drive submitted papers folder |
| `safeguards` | Rsync home directory + `.claude` to external backup drive |
| `slow_sync_to_Google_Drive` | Slow-sync compiled videos to Google Drive with 2-hour sleep intervals |
| `sync_CRSY_to_Google_Drive` | Sync CRSY course materials to Google Drive |
| `sync_lecture_slides_to_server` | Rsync lecture slides to York CS server |
| `Google_Drive_sync` | Manage Google Drive sync cycle (launch/monitor/quit) via DriveFS log parsing |
| `Google_Drive_sync.py` | Python version of Google Drive sync management |

## Video Conversion

| Script | Description |
|--------|-------------|
| `convert_video` | FFmpeg video conversion (H.264 + AAC to MP4) |
| `convert_video_OSX` | macOS-specific FFmpeg video conversion |
| `convert_video_with_subtitles` | FFmpeg conversion with subtitle embedding |
| `convert1` | Single-pass FFmpeg conversion to 1024p MP4 with title/genre metadata |
| `mass_convert_to_iPad` | Batch convert all video files in current directory for iPad |
| `convert_to_iPad` | Convert single video for iPad playback |
| `convert_olympus_videos.py` | Batch convert Olympus camera video files |
| `run_convert_olympus_videos` | Run script wrapper for Olympus video conversion |
| `increase_volume` | Boost audio volume 3x on a video file |
| `reduce_audio_bit_rate` | Reduce audio quality for mp3/m4a files |
| `install_ffmpeg_with_all_options` | Full FFmpeg reinstall with every optional codec |

## Photo Management

| Script | Description |
|--------|-------------|
| `change_photo_dates` | Set file timestamps from EXIF DateTimeOriginal using exiftool |
| `change_time_stamps` | Copy timestamps from source files to JPG/MP4/MOV files |
| `change_time_stamps_for_2014` | Same as above but for 2014 photo library |
| `copy_time_stamps.py` | Python utility to copy timestamps between files |
| `overall_change_time_stamps` | Run change_time_stamps across all month subdirectories |
| `recent_photos` | Rsync recent photos from SD cards and cameras to `~/recent_photos/` |
| `copy_yearly_photos` | Copy photos from a year based on date range |
| `copy_years_photos_leaf_folders.py` | Copy leaf folders (year/month dirs) from photo library |
| `remove_HDRs` | Delete MOV files matching HDR JPG filenames |
| `resize_photos_for_photo_frame` | Resize photos for digital photo frame (skips "originals" dir) |

## File Conversion

| Script | Description |
|--------|-------------|
| `convert` | General image/video conversion wrapper |
| `convert_image_to_jpg` | Convert single image to JPG |
| `convert_rtf_to_pdf` | Batch convert RTF files to PDF via LibreOffice |
| `convert1` | See video conversion section |
| `rr2unix` | Remove carriage returns from a file (Windows→Unix line endings) |
| `remove_metadata_general` | Strip metadata from MKV and re-encode to MP4 |

## Music

| Script | Description |
|--------|-------------|
| `marvin_music` | See backup section (MARVIN drive music sync) |
| `digby_music` | See backup section (DIGBY drive music sync) |

## System Administration

| Script | Description |
|--------|-------------|
| `rebuild_spotlight` | Disable, delete, and rebuild Spotlight index |
| `reset_WiFi` | Reset WiFi by removing system preference plists |
| `reset_network_and_reboot` | Reset all network configs and reboot |
| `umount_drives` | Unmount external drives by name |
| `increase_volume` | See video conversion section |
| `pip_upgrade` | Upgrade all outdated pip packages |
| `upgrade_brew_npm_and_pip_packages` | Update brew, pip, npm and clean up |

## LLM / Model Tools

| Script | Description |
|--------|-------------|
| `install_LLMs` | Install local LLM models (set -e, one-shot) |
| `build_qwen3.6_model` | Build Qwen 3.6 Ollama model |
| `build_qwen2.5_model` | Build Qwen 2.5 Ollama model |
| `build_gemma_model` | Build Gemma Ollama model |
| `Modelfile_qwen2.5` | Ollama Modelfile for Qwen 2.5 |
| `Modelfile_gemma4` | Ollama Modelfile for Gemma |
| `run_claude_qwen` | Run Claude via local LMStudio proxy (sets ANTHROPIC_* env vars) |
| `run_claude_gemma` | Launch Claude with Gemma model via ollama |
| `connect_to_claude_server` | SSH tunnel to York CS GPU server (csgpu3) |
| `dmgcrack` | Crack DMG password using john/dmg2john |

## LaTeX

| Script | Description |
|--------|-------------|
| `slatex` | Build LaTeX document (pdflatex → bibtex → pdflatex ×3) |
| `build_group_healthcare_proposal` | Build group healthcare proposal from Google Drive |
| `build_independent_healthcare_proposal` | Build independent healthcare proposal from Google Drive |

## Cleanup & Maintenance

| Script | Description |
|--------|-------------|
| `cleanup_cloud_files` | Remove Google Drive/Dropbox conflict and duplicate files |
| `remove_duplicates` | Deduplicate Google Drive Archive/Home folders (keep newest) |
| `fix_video_camera_for_zoom` | Kill camera assistant processes to fix Zoom camera issues |

## Other

| Script | Description |
|--------|-------------|
| `Brewfile` | Homebrew bundle file for package installation |
| `save and restore dates.txt` | Notes on saving/restoring file timestamps |
| `franks scraper.rtf` | Frank's scraper documentation |
| `update_svns` | Update local SVN working copies (PROXIMA, FBI) |
| `upload_draft_web_pages` | Rsync draft web pages to tmp for web serving |
