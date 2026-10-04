#!/usr/bin/env bash
#
# Wrapper that runs main.py and guarantees the cloakbrowser-mcp/Chromium
# subtree is torn down afterwards. Adapted from Langchain/run_cloak_agent.sh —
# same underlying problem: stdio_client spawns `npx`, which is an `sh -c`
# wrapper; killing that sh does NOT cascade to the node server or Chromium,
# so they survive as orphans holding the Chromium profile lock. ALWAYS launch
# this project through this script, never `python main.py` directly.
#
# Usage:
#   ./run_agent.sh                        # run main.py, clean up after
#   ./run_agent.sh bench_full_graph.py    # run a different script, clean up after
#   ./run_agent.sh --clean-only           # just clean up stranded processes

set -uo pipefail

PYTHON_SCRIPT="${1:-main.py}"
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

if [ "$PYTHON_SCRIPT" = "--clean-only" ]; then
  cleanup
  exit 0
fi

cleanup
unset _CLEANUP_DONE

# Use nvm's NATIVE Linux node/npx, not the Windows-native one WSL interop would
# otherwise resolve via /mnt/c/Program Files/nodejs/. Spawning a Windows process
# from a WSL Python asyncio subprocess and piping its stdio back across the
# interop boundary is what caused the MCP stdio handshake to hang indefinitely
# (session.initialize() never got a response) — see RESULTS.md §4. Installed
# via nvm (user-space, no sudo) since apt isn't available without a password.
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

log "starting $PYTHON_SCRIPT"
python "$PYTHON_SCRIPT"
exit_code=$?

log "python exited with code $exit_code"
exit "$exit_code"
