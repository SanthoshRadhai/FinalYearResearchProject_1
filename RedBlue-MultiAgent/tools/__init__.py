"""In-process LangChain tools — deliberately NOT MCP servers.

See ../../Research-Paper resources/08-MCP-TOOL-IMPLEMENTATION-OPTIONS.md: every
capability here that doesn't need a live browser is a plain Python function, run
in-process, with no subprocess to spawn, hang, or orphan. The only subprocess in
this whole system is the single shared cloakbrowser-mcp instance used by the
Recon agent (agents/recon.py) — everything else stays in this file/tools module
on purpose.
"""

from .cvss_tool import parse_cvss_vector
from .attack_kb_tool import lookup_attack_technique, search_attack_kb
from .nvd_tool import lookup_cve
from .rag_tool import search_knowledge_base

ALL_TOOLS = [parse_cvss_vector, lookup_attack_technique, search_attack_kb, lookup_cve, search_knowledge_base]
