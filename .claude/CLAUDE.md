# Claude Rules

## General

- Keep responses short and concise.
- No emojis unless explicitly asked.
- No trailing summaries — user can read the diff/output.
- Default to light theme for any desktop/UI config changes.

## System

- OS: Debian Linux (bookworm)
- WM: i3 with i3status (not i3blocks)
- Display: Ultrawide 3440×1440
- Shell: bash

## Dotfiles

- Repo: `git@github.com:mikehlim/dotfiles.git` (branch: `master`)
- Local clone: `/tmp/dotfiles` (ephemeral — re-clone if missing)
- Use `/sync-dotfiles` skill to push config changes to GitHub.
- Wallpapers live at `~/.config/i3/wallpapers/` — always resize to 3440×1440 before committing.
- Do not commit `~/.claude/settings.json` (machine-specific permissions).
- SSH auth to GitHub is configured; `gh` CLI is installed at `/usr/bin/gh`.

## i3 / Desktop

- Bar: i3status with `~/.config/i3status/run_bar.sh` (wraps i3status with weather widget).
- Wallpapers: `feh --randomize --recursive --bg-fill ~/.config/i3/wallpapers`.
- Lock screen: `~/.config/i3/i3lock-dpms`.
- Dunst: light theme (bg `#fafafa`, fg `#333333`); left-click invokes action, right-click closes all.
