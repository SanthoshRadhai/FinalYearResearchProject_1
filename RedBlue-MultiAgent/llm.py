"""Shared LLM client — one llama.cpp endpoint, reused by every agent node.

Same backend already proven in Langchain/4_langchain_stealth_llamacpp_CVE_Agent.py
and Langchain/6_langchain_cloakbrowser_lama_cpp.py: llama.cpp (llama-server)
launched with --jinja so it applies gpt-oss-20b's native Harmony chat template,
which is what makes tool-calling actually work for this model (see
Research-Paper resources/06-GPT-OSS-LLAMACPP-TOOLCALLING-FINDINGS.md).

All specialist agents share this ONE model instance/process on IT-GPU — do not
spin up a second llama-server for a different agent; that wastes VRAM and
reintroduces the "which server is on which port" confusion from earlier
sessions. If a node needs a different temperature, instantiate a second
ChatOpenAI object pointed at the SAME base_url/model, not a new server.
"""

import os

import httpx
from langchain_openai import ChatOpenAI

LLAMACPP_BASE_URL = os.environ.get("LLAMACPP_BASE_URL", "http://localhost:5500/v1")


def _detect_model_path() -> str:
    """llama.cpp's OpenAI-compat API requires the exact model PATH as the
    "model" field, not a short name — and that path changes whenever the GGUF
    moves or a different server/user is running behind the same port (this bit
    us during testing: the port-5500 tunnel briefly pointed at a HPC-hosted
    gpt-oss-20b under a different home directory than the one this file used to
    hardcode). Auto-detect it from /v1/models instead of hardcoding, so a
    tunnel/server swap doesn't silently break every agent with a 404."""
    env_override = os.environ.get("GPT_OSS_MODEL_PATH")
    if env_override:
        return env_override
    resp = httpx.get(f"{LLAMACPP_BASE_URL}/models", timeout=10)
    resp.raise_for_status()
    models = resp.json().get("data", [])
    if not models:
        raise RuntimeError(f"{LLAMACPP_BASE_URL}/models returned no models — is llama-server running?")
    return models[0]["id"]


MODEL_PATH = _detect_model_path()


def make_llm(temperature: float = 0.2, max_tokens: int = 8000) -> ChatOpenAI:
    return ChatOpenAI(
        base_url=LLAMACPP_BASE_URL,
        api_key="EMPTY",
        model=MODEL_PATH,
        temperature=temperature,
        max_tokens=max_tokens,
        streaming=False,
    )


# Tool-using specialist agents: lower temperature, per scripts 4/6's finding
# that this is more reliable for structured tool-call output than gpt-oss's
# "recommended" temp=1.0 (script 5 tried temp=1.0 and was the noisiest run).
TOOL_AGENT_LLM = make_llm(temperature=0.2, max_tokens=8000)

# Orchestrator/Evaluator: pure-reasoning roles. gpt-oss-20b spends tokens on
# an internal reasoning channel before emitting the final structured JSON, so
# this budget has to cover that reasoning too, not just the short answer --
# 2000 was too tight and caused "Could not parse response content as the
# length limit was reached" truncation failures under with_structured_output.
JUDGMENT_LLM = make_llm(temperature=0.1, max_tokens=6000)
