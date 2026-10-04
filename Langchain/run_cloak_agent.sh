#!/usr/bin/env bash
#
# Wrapper that runs the LangChain <-> cloakbrowser-mcp client and guarantees the
# server/browser subtree is torn down afterwards.
#
# Why this exists: stdio_client spawns `npx`, which on this system is an `sh -c`
# wrapper. Killing that sh does NOT cascade to the node servers or to Chromium,
# so they survive as orphans and keep holding the Chromium profile lock at
# ~/.cache/ms-playwright-mcp/mcp-chromium-<hash>/. The next run then fails with
# "Browser is already in use for ...".
#
# Usage:
#   ./run_cloak_agent.sh                       # run the default script, clean up after
#   ./run_cloak_agent.sh my_other_client.py    # run a different script
#   ./run_cloak_agent.sh --clean-only          # just clean up stranded processes
#   DEBUG_HARMONY=1 ./run_cloak_agent.sh       # env vars pass through
#
# Note: pkill -f matches on the full command line, so this kills EVERY
# cloakbrowser-mcp / @playwright/mcp process owned by this user -- including one
# started by a different tool (Claude Desktop, VS Code, a second terminal).
# That is the intended behaviour for a single-user dev box; if you ever need to
# run two clients at once, use PLAYWRIGHT_MCP_ISOLATED instead of this script.

set -uo pipefail

PYTHON_SCRIPT="${1:-6_langchain_cloakbrowser_lama_cpp.py}"
PROFILE_GLOB="$HOME/.cache/ms-playwright-mcp/mcp-chromium-*"
GRACE_SECONDS=3

# Patterns are ordered deliberately: browser first (so no surviving parent can
# relaunch it), then the MCP servers, then the npx/sh wrapper.
PATTERNS=(
  "$HOME/.cloakbrowser/chromium-.*/chrome"
  "chrome_crashpad_handler"
  "@playwright/mcp/cli.js"
  "cloakbrowser-mcp"
)

log() { printf '[cleanup] %s\n' "$*" >&2; }

# Count processes matching a pattern, excluding this script and its children.
count_matching() {
  pgrep -f -- "$1" 2>/dev/null \vert{} grep -vx "$$" | wc -l
}

terminate_pattern() {
  local pattern="$1" n

  n=$(count_matching "$pattern")
  [ "$n" -eq 0 ] && return 0

  log "SIGTERM -> $n process(es) matching:$pattern"
  pkill -f -- "$pattern" 2>/dev/null

  # Give them a moment to exit cleanly; Chromium releases its profile lock
  # properly on SIGTERM but not on SIGKILL.
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
  # Make the handler idempotent: EXIT fires after INT/TERM, so without this the
  # whole teardown would run twice on Ctrl-C.
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

if [ ! -f "$PYTHON_SCRIPT" ]; then
  echo "error: no such file: $PYTHON_SCRIPT" >&2
  exit 1
fi

# Clean first too: a previous hard crash may have stranded a browser that would
# otherwise make this run fail before it starts.
cleanup
unset _CLEANUP_DONE

# --- CONDA ACTIVATION ---
log "Activating conda environment 'hexstrike'..."
# Source conda initialization so `conda activate` works inside this bash script
source /home/johndoe/miniconda3/etc/profile.d/conda.sh
conda activate hexstrike
# ------------------------

log "starting $PYTHON_SCRIPT"
python "$PYTHON_SCRIPT"
exit_code=$?

log "python exited with code $exit_code"
exit "$exit_code"