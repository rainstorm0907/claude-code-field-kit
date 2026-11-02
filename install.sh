#!/usr/bin/env bash
# Install the kit into Claude Code: skills -> ~/.claude/skills, agents -> ~/.claude/agents.
# Default links to this checkout so `git pull` updates everything. --copy copies instead.
set -euo pipefail

root="$(cd -P "$(dirname "$0")" && pwd)"
claude_dir="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
mode=link
[[ "${1:-}" == "--copy" ]] && mode=copy
backup="$claude_dir/backup-field-kit-$(date +%Y%m%d-%H%M%S)"

place() { # src dest
  local src="$1" dest="$2"
  if [[ -L "$dest" && "$(readlink "$dest")" == "$src" ]]; then
    echo "  = $(basename "$dest")"; return
  fi
  if [[ -e "$dest" || -L "$dest" ]]; then
    mkdir -p "$backup/$(basename "$(dirname "$dest")")"
    mv "$dest" "$backup/$(basename "$(dirname "$dest")")/"
    echo "  ~ $(basename "$dest") (old one moved to $backup)"
  fi
  if [[ $mode == link ]]; then ln -s "$src" "$dest"; else cp -R "$src" "$dest"; fi
  echo "  + $(basename "$dest")"
}

mkdir -p "$claude_dir/skills" "$claude_dir/agents"
echo "skills -> $claude_dir/skills"
for s in "$root"/skills/*/; do s="${s%/}"; place "$s" "$claude_dir/skills/$(basename "$s")"; done
echo "agents -> $claude_dir/agents"
for a in "$root"/agents/*.md; do place "$a" "$claude_dir/agents/$(basename "$a")"; done

echo
echo "Done ($mode). Open a new Claude Code session to load them."
