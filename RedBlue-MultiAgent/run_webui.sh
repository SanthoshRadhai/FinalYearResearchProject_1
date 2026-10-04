#!/usr/bin/env bash
#
# Wrapper that runs the Phase-1 web UI (webui/server.py) and guarantees the
# cloakbrowser-mcp/Chromium subtree is torn down afterwards -- same
# underlying problem run_agent.sh already solves (stdio_client spawns `npx`,
# killing it doesn't cascade to the node server/Chromium, so they survive
# as orphans). ALWAYS launch the web UI through this script, never
# `uvicorn webui.server:app` directly.
#
# Usage:
#   ./run_webui.sh                # start the server on 127.0.0.1:8000
#   ./run_webui.sh 8080           # start it on a different port
#   ./run_webui.sh --clean-only   # just clean up stranded processes

set -uo pipefail

PORT="${1:-8000}"
PROFILE_GLOB="$HOME/.cache/ms-playwright-mcp/mcp-chromium-*"
GRACE_SECONDS=3

PATTERNS=(
  "$HOME/.cloakbrowser/chromium-.*/chrome"
  "chrome_crashpad_handler"
  "@playwright/mcp/cli.js"
  "cloakbrowser-mcp"
)

log() { printf '[cleanup] %s\n' "$*" >&2; }

count_matching() {
  pgrep -f -- "$1" 2>/dev/null | grep -vx "$$" | wc -l
}

terminate_pattern() {
  local pattern="$1" n
  n=$(count_matching "$pattern")
  [ "$n" -eq 0 ] && return 0

  log "SIGTERM -> $n process(es) matching:$pattern"
  pkill -f -- "$pattern" 2>/dev/null

  local waited=0
  while [ "$waited" -lt "$GRACE_SECONDS" ]; do
    sleep 1
    waited=$((waited + 1))
    [ "$(count_matching "$pattern")" -eq 0 ] && return 0
  done

  n=$(count_matching "$pattern")
  if [ "$n" -gt 0 ]; then
    log "SIGKILL -> $n stubborn process(es) matching:$pattern"
    pkill -9 -f -- "$pattern" 2>/dev/null
    sleep 1
  fi
}

clear_stale_locks() {
  local dir found=0
  for dir in $PROFILE_GLOB; do
    [ -d "$dir" ] || continue
    for lock in SingletonLock SingletonSocket SingletonCookie; do
      if [ -e "$dir/$lock" ] || [ -L "$dir/$lock" ]; then
        rm -f -- "$dir/$lock" && found=1
      fi
    done
  done
  [ "$found" -eq 1 ] && log "removed stale Singleton* lock file(s) from the profile dir"
  return 0
}

cleanup() {
  [ -n "${_CLEANUP_DONE:-}" ] && return 0
  _CLEANUP_DONE=1

  log "tearing down cloakbrowser-mcp subtree..."
  for pattern in "${PATTERNS[@]}"; do
    terminate_pattern "$pattern"
  done
  clear_stale_locks

  local leftover=0
  for pattern in "${PATTERNS[@]}"; do
    leftover=$((leftover + $(count_matching "$pattern")))
  done

  if [ "$leftover" -gt 0 ]; then
    log "WARNING: $leftover process(es) still alive -- inspect with:"
    log "  ps aux | grep -i -e cloakbrowser -e mcp-chromium -e ms-playwright"
  else
    log "done, nothing left running."
  fi
}

trap cleanup EXIT INT TERM

if [ "$PORT" = "--clean-only" ]; then
  cleanup
  exit 0
fi

cleanup
unset _CLEANUP_DONE

# Native WSL node/npx, not the Windows-native one WSL interop would otherwise
# resolve -- see RESULTS.md §4 for why this matters (silent MCP stdio hang).
export NVM_DIR="$HOME/.nvm"
if [ -s "$NVM_DIR/nvm.sh" ]; then
  \. "$NVM_DIR/nvm.sh"
  nvm use 22 >/dev/null
fi
log "node: $(which node 2>/dev/null || echo 'NOT FOUND') ($(node -v 2>/dev/null))"
log "npx:  $(which npx 2>/dev/null || echo 'NOT FOUND')"

log "Activating conda environment 'hexstrike'..."
source /home/johndoe/miniconda3/etc/profile.d/conda.sh
conda activate hexstrike

log "starting webui server on 127.0.0.1:$PORT"
python -m uvicorn webui.server:app --host 127.0.0.1 --port "$PORT"
exit_code=$?

log "uvicorn exited with code $exit_code"
exit "$exit_code"
