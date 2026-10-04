"""Shared llama.cpp endpoint client. Two use cases share the same endpoint:

  * Plain chat (app.py's Chat tab) -- `make_llm(...)` is called fresh per turn
    with whatever temperature/max_tokens/top_p the session's Settings panel
    currently holds.
  * RedBlue multi-agent pipeline (ported from ../RedBlue-MultiAgent) -- its
    agents were tuned against FIXED parameters (see RESULTS.md there for why:
    temp=0.2 was more reliable than gpt-oss's "recommended" temp=1.0 for
    structured tool-call output). TOOL_AGENT_LLM/JUDGMENT_LLM below are that
    same proven configuration, kept separate from the chat tab's
    user-tunable client so changing chat settings can never destabilize the
    multi-agent pipeline's tool-calling reliability.
"""

import os

import httpx
from langchain_openai import ChatOpenAI

LLAMACPP_BASE_URL = os.environ.get("LLAMACPP_BASE_URL", "http://localhost:5500/v1")


def _detect_model_path() -> str:
    """llama.cpp's OpenAI-compat API requires the exact model PATH as the
    "model" field, not a short name. Auto-detect it from /v1/models instead
    of hardcoding, so a tunnel/server swap doesn't silently 404 every call."""
    env_override = os.environ.get("GPT_OSS_MODEL_PATH")
    if env_override:
        return env_override
    resp = httpx.get(f"{LLAMACPP_BASE_URL}/models", timeout=10)
    resp.raise_for_status()
    models = resp.json().get("data", [])
    if not models:
        raise RuntimeError(f"{LLAMACPP_BASE_URL}/models returned no models -- is llama-server running?")
    return models[0]["id"]


MODEL_PATH = _detect_model_path()

DEFAULT_SETTINGS = {
    "temperature": 0.7,
    "max_tokens": 2000,
    "top_p": 0.95,
    "system_prompt": "",
}


def make_llm(temperature: float, max_tokens: int, top_p: float) -> ChatOpenAI:
    return ChatOpenAI(
        base_url=LLAMACPP_BASE_URL,
        api_key="EMPTY",
        model=MODEL_PATH,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        streaming=True,
    )


# --- RedBlue multi-agent clients, ported from ../RedBlue-MultiAgent/llm.py ---
def _make_fixed_llm(temperature: float, max_tokens: int) -> ChatOpenAI:
    return ChatOpenAI(
        base_url=LLAMACPP_BASE_URL,
        api_key="EMPTY",
        model=MODEL_PATH,
        temperature=temperature,
        max_tokens=max_tokens,
        streaming=False,
    )


# Tool-using specialist agents (Recon, Vulnerability Analysis): lower
# temperature, per RedBlue-MultiAgent's finding that this is more reliable
# for structured tool-call output than gpt-oss's "recommended" temp=1.0.
TOOL_AGENT_LLM = _make_fixed_llm(temperature=0.2, max_tokens=8000)

# Orchestrator/Evaluator: pure-reasoning roles. 6000 (not the original 2000)
# to leave room for gpt-oss-20b's internal reasoning channel before it emits
# the final structured JSON -- 2000 caused "Could not parse response content
# as the length limit was reached" truncation failures under
# with_structured_output (see RedBlue-MultiAgent's fix for the same bug).
JUDGMENT_LLM = _make_fixed_llm(temperature=0.1, max_tokens=6000)
