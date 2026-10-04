"""Scaled-up (N=8) reliability-harness benchmark — bumps RESULTS.md §8 from
n=2 to n=8: single malformed call (should NOT trip the breaker yet), streak
reset after a clean call, a true-negative check (clean message unchanged),
and the browser ref-redirect logic (both triggered and correctly scoped-off
for non-browser agents). No LLM call needed -- reliability.py is pure Python.
"""

import asyncio
import json

from langchain_core.messages import AIMessage, ToolMessage
from reliability import make_sanitize_hook

CASES = []


def _msg(content, tool_calls, mid):
    return AIMessage(content=content, tool_calls=tool_calls, id=mid)


async def case_A_two_consecutive_malformed_trips_breaker():
    hook = make_sanitize_hook()
    m1 = _msg("", [{"name": "parse_cvss_vector", "args": {"vector": ""}, "id": "c1", "type": "tool_call"}], "a1")
    m2 = _msg("", [{"name": "parse_cvss_vector", "args": {"vector": ""}, "id": "c2", "type": "tool_call"}], "a2")
    await hook({"messages": [m1]})
    out = await hook({"messages": [m1, m2]})
    fired = bool(out.get("messages")) and not out["messages"][0].tool_calls
    return {"case": "A_two_consecutive_malformed_trips_breaker", "expected": "aborts on 2nd",
            "breaker_fired": fired, "correct": fired}


async def case_B_single_malformed_does_not_trip():
    hook = make_sanitize_hook()
    m1 = _msg("", [{"name": "parse_cvss_vector", "args": {"vector": ""}, "id": "c1", "type": "tool_call"}], "a1")
    out = await hook({"messages": [m1]})
    # First malformed call alone (limit=2): should NOT abort -- either {} (no change)
    # or a sanitized passthrough, but NOT an aborting content-only message.
    aborted = bool(out.get("messages")) and not out["messages"][0].tool_calls
    return {"case": "B_single_malformed_does_not_trip", "expected": "does not abort yet",
            "aborted": aborted, "correct": not aborted}


async def case_C_streak_resets_after_clean_call():
    hook = make_sanitize_hook()
    malformed = _msg("", [{"name": "parse_cvss_vector", "args": {"vector": ""}, "id": "c1", "type": "tool_call"}], "a1")
    clean = _msg("Here is a clean answer.", [], "a2")
    malformed2 = _msg("", [{"name": "parse_cvss_vector", "args": {"vector": ""}, "id": "c3", "type": "tool_call"}], "a3")
    await hook({"messages": [malformed]})          # streak = 1
    await hook({"messages": [malformed, clean]})    # streak reset to 0 (clean call)
    out = await hook({"messages": [malformed, clean, malformed2]})  # streak = 1 again, not 2
    aborted = bool(out.get("messages")) and not out["messages"][0].tool_calls
    return {"case": "C_streak_resets_after_clean_call", "expected": "does not abort (streak was reset)",
            "aborted": aborted, "correct": not aborted}


async def case_D_harmony_sanitizer_strips_content():
    hook = make_sanitize_hook()
    leaky = _msg("<|channel|>final<|message|>The answer is 42.", [], "a1")
    out = await hook({"messages": [leaky]})
    cleaned = bool(out.get("messages")) and "<|" not in out["messages"][0].content
    return {"case": "D_harmony_sanitizer_strips_content", "expected": "tokens stripped",
            "cleaned": cleaned, "correct": cleaned}


async def case_E_harmony_sanitizer_strips_tool_name():
    hook = make_sanitize_hook()
    leaky = _msg("", [{"name": "lookup_cve<|call|>", "args": {"cve_id": "CVE-2024-3400"}, "id": "c1", "type": "tool_call"}], "a1")
    out = await hook({"messages": [leaky]})
    cleaned = bool(out.get("messages")) and all("<|" not in c["name"] for c in out["messages"][0].tool_calls)
    return {"case": "E_harmony_sanitizer_strips_tool_name", "expected": "tool name cleaned",
            "cleaned": cleaned, "correct": cleaned}


async def case_F_clean_message_no_false_positive():
    hook = make_sanitize_hook()
    clean = _msg("Here is a perfectly normal answer with no issues.",
                 [{"name": "lookup_cve", "args": {"cve_id": "CVE-2024-3400"}, "id": "c1", "type": "tool_call"}], "a1")
    out = await hook({"messages": [clean]})
    return {"case": "F_clean_message_no_false_positive", "expected": "no changes ({})",
            "got_empty_update": out == {}, "correct": out == {}}


async def case_G_ref_redirect_triggers_for_browser_agent():
    hook = make_sanitize_hook(ref_requiring_tools=frozenset({"browser_click"}))
    bad_click = _msg("", [{"name": "browser_click", "args": {"ref": ""}, "id": "c1", "type": "tool_call"}], "a1")
    out = await hook({"messages": [bad_click]})
    redirected = (bool(out.get("messages"))
                  and out["messages"][0].tool_calls
                  and out["messages"][0].tool_calls[0]["name"] == "browser_snapshot")
    return {"case": "G_ref_redirect_triggers_for_browser_agent", "expected": "redirected to browser_snapshot",
            "redirected": redirected, "correct": redirected}


async def case_H_ref_redirect_scoped_off_for_non_browser_agent():
    """Same bad browser_click call, but ref_requiring_tools is the default
    empty frozenset (as used by non-browser agents like vuln_analysis) --
    the redirect must NOT fire, since this agent was never given browser
    tools in the first place and 'browser_click' isn't even a real tool
    name it could call."""
    hook = make_sanitize_hook()  # default: empty ref_requiring_tools
    bad_click = _msg("", [{"name": "browser_click", "args": {"ref": ""}, "id": "c1", "type": "tool_call"}], "a1")
    out = await hook({"messages": [bad_click]})
    redirected = (bool(out.get("messages"))
                  and out["messages"][0].tool_calls
                  and out["messages"][0].tool_calls[0]["name"] == "browser_snapshot")
    return {"case": "H_ref_redirect_scoped_off_for_non_browser_agent",
            "expected": "NOT redirected (feature correctly scoped off)",
            "redirected": redirected, "correct": not redirected}


async def main():
    results = []
    for fn in [case_A_two_consecutive_malformed_trips_breaker, case_B_single_malformed_does_not_trip,
               case_C_streak_resets_after_clean_call, case_D_harmony_sanitizer_strips_content,
               case_E_harmony_sanitizer_strips_tool_name, case_F_clean_message_no_false_positive,
               case_G_ref_redirect_triggers_for_browser_agent,
               case_H_ref_redirect_scoped_off_for_non_browser_agent]:
        r = await fn()
        print(json.dumps(r, indent=2))
        results.append(r)

    n_correct = sum(1 for r in results if r["correct"])
    print(f"\n=== RELIABILITY HARNESS SUMMARY (N={len(results)}) === {n_correct}/{len(results)} as expected")
    with open("bench_reliability_n8_results.json", "w") as f:
        json.dump(results, f, indent=2)


if __name__ == "__main__":
    asyncio.run(main())
