# Sync Dotfiles to GitHub

Sync local config files to the GitHub dotfiles repo at `git@github.com:mikehlim/dotfiles.git`.

## Steps

1. Clone or update the dotfiles repo at `/tmp/dotfiles`:
   - If `/tmp/dotfiles` doesn't exist: `git clone git@github.com:mikehlim/dotfiles.git /tmp/dotfiles`
   - If it does exist: `git -C /tmp/dotfiles pull`

2. Diff each tracked config against the local version. The canonical local paths are:
   - `~/.config/i3/config` → `.config/i3/config`
   - `~/.config/i3/i3lock-dpms` → `.config/i3/i3lock-dpms`
   - `~/.config/i3/alternating_layouts.py` → `.config/i3/alternating_layouts.py`
   - `~/.config/i3/wallpapers/` → `.config/i3/wallpapers/`
   - `~/.config/i3status/config` → `.config/i3status/config`
   - `~/.config/i3status/run_bar.sh` → `.config/i3status/run_bar.sh`
   - `~/.config/i3status/wrapper.py` → `.config/i3status/wrapper.py`
   - `~/.config/i3status/weather.conf` → `.config/i3status/weather.conf`
   - `~/.config/dunst/dunstrc` → `.config/dunst/dunstrc`
   - `~/.config/dunst/notification_default.sh` → `.config/dunst/notification_default.sh`
   - `~/.screenlayout/` → `.screenlayout/`
   - `~/.bashrc` → `.bashrc`
   - `~/.xinitrc` → `.xinitrc`
   - `~/.Xresources` → `.Xresources`
   - `~/.claude/commands/` → `.claude/commands/`
   - `~/.claude/CLAUDE.md` → `.claude/CLAUDE.md`

3. Show a summary of which files changed, were added, or removed.

4. Copy all updated local files into `/tmp/dotfiles`, then `git add` and commit with a descriptive message summarizing what changed.

5. `git push` to origin.

## Notes

- Always treat local as the source of truth.
- For wallpapers: resize any new images to **3440×1440** (ultrawide QHD) using center-crop before adding to repo.
- Do not commit `settings.json` — it contains machine-specific permission paths.
- The dotfiles repo branch is `master`.
