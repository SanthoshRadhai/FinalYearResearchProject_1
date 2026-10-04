"""CyberTuringAgnet -- Gradio frontend over two LangGraph graphs, navigated
through a single persistent left sidebar (not tabs):

  * Chat -- a plain single-LLM chat with persistent, switchable sessions
    (LangGraph's own sqlite checkpointer) and a per-session Settings panel
    (temperature/max_tokens/top_p/system prompt).
  * RedBlue Investigate -- the full multi-agent pipeline ported from
    ../RedBlue-MultiAgent (Safety -> Orchestrator -> {Recon, Vulnerability
    Analysis} -> Evaluator -> ... -> END), showing every agent's live trace,
    verified/rejected findings, and the final answer.
  * Agents (collapsible sidebar section) -- each agent from that pipeline
    exercised on its own, one page per agent, for demoing/debugging a single
    node in isolation.

The sidebar is a plain "page" switcher: one gr.Column per page, all in the
same Row, with only the active one visible=True at a time -- there is no
gr.Tabs anywhere, so there's no tab-strip/radio-button chrome to fight with.

Run via run_app.sh, never `python app.py` directly, so the shared
cloakbrowser-mcp subprocess (used by Recon, in both the pipeline and the
agent pages) is guaranteed torn down on exit.
"""

import gradio as gr
from langchain_core.messages import AIMessageChunk, HumanMessage

import agent_playground
import redblue
from checkpointer import get_checkpointer
from graph import build_chat_graph
from llm import DEFAULT_SETTINGS
import sessions

sessions.init_sessions_table()

_chat_graph = None


async def get_chat_graph():
    # Lazy + cached: the checkpointer's aiosqlite connection must be opened
    # from inside Gradio's own event loop (see checkpointer.py), so this
    # can't run at module import time -- it runs on first request instead.
    global _chat_graph
    if _chat_graph is None:
        checkpointer = await get_checkpointer()
        _chat_graph = build_chat_graph(checkpointer)
    return _chat_graph


def _session_choices() -> list[tuple[str, str]]:
    return [(s["title"], s["session_id"]) for s in sessions.list_sessions()]


async def _load_history(session_id: str) -> list[dict]:
    graph = await get_chat_graph()
    state = await graph.aget_state({"configurable": {"thread_id": session_id}})
    messages = state.values.get("messages", []) if state and state.values else []
    history = []
    for m in messages:
        role = "user" if m.type == "human" else "assistant"
        history.append({"role": role, "content": m.content})
    return history


def _settings_updates(settings: dict):
    return (
        settings["temperature"],
        settings["max_tokens"],
        settings["top_p"],
        settings["system_prompt"],
    )


async def on_app_load():
    existing = sessions.list_sessions()
    if not existing:
        sid = sessions.create_session()
        existing = sessions.list_sessions()
    else:
        sid = existing[0]["session_id"]
    session = sessions.get_session(sid)
    history = await _load_history(sid)
    return (
        gr.update(choices=_session_choices(), value=sid),
        history,
        sid,
        *_settings_updates(session["settings"]),
    )


def new_chat():
    sid = sessions.create_session()
    return (
        gr.update(choices=_session_choices(), value=sid),
        [],
        sid,
        *_settings_updates(DEFAULT_SETTINGS),
    )


async def select_session(session_id: str):
    if not session_id:
        return gr.update(), [], session_id, *_settings_updates(DEFAULT_SETTINGS)
    sessions.touch_session(session_id)
    session = sessions.get_session(session_id)
    history = await _load_history(session_id)
    return (
        gr.update(choices=_session_choices(), value=session_id),
        history,
        session_id,
        *_settings_updates(session["settings"]),
    )


async def delete_current(session_id: str):
    if session_id:
        sessions.delete_session(session_id)
    remaining = sessions.list_sessions()
    if not remaining:
        new_id = sessions.create_session()
        remaining = sessions.list_sessions()
    else:
        new_id = remaining[0]["session_id"]
    session = sessions.get_session(new_id)
    history = await _load_history(new_id)
    return (
        gr.update(choices=_session_choices(), value=new_id),
        history,
        new_id,
        *_settings_updates(session["settings"]),
    )


def reset_settings():
    return _settings_updates(DEFAULT_SETTINGS)


async def send_message(
    user_msg: str,
    history: list,
    session_id: str,
    temperature: float,
    max_tokens: float,
    top_p: float,
    system_prompt: str,
):
    if not user_msg or not user_msg.strip():
        yield history, "", gr.update()
        return

    settings = {
        "temperature": temperature,
        "max_tokens": int(max_tokens),
        "top_p": top_p,
        "system_prompt": system_prompt,
    }
    sessions.update_session_settings(session_id, settings)

    is_first_message = len(history) == 0
    history = history + [{"role": "user", "content": user_msg}, {"role": "assistant", "content": ""}]
    yield history, "", gr.update()

    config = {"configurable": {"thread_id": session_id, **settings}}
    assistant_text = ""
    graph = await get_chat_graph()
    async for chunk, _metadata in graph.astream(
        {"messages": [HumanMessage(content=user_msg)]},
        config=config,
        stream_mode="messages",
    ):
        if isinstance(chunk, AIMessageChunk) and chunk.content:
            assistant_text += chunk.content
            history[-1]["content"] = assistant_text
            yield history, "", gr.update()

    if is_first_message:
        title = user_msg.strip()[:40] + ("..." if len(user_msg.strip()) > 40 else "")
        sessions.rename_session(session_id, title)
        yield history, "", gr.update(choices=_session_choices(), value=session_id)


# --- Sidebar page-switching -------------------------------------------------
# Every "page" is a gr.Column; exactly one is visible=True at a time. A nav
# click sets its own button to variant="primary" (highlighted) and every
# other nav button back to "secondary", so the sidebar shows which page is
# active without needing a tab strip or radio-button chrome.

PAGES = ["chat", "redblue", "safety", "recon", "vuln", "evaluator", "orchestrator"]
PAGE_LABELS = {
    "chat": "Chat",
    "redblue": "RedBlue Investigate",
    "safety": "Safety",
    "recon": "Recon",
    "vuln": "Vulnerability Analysis",
    "evaluator": "Evaluator",
    "orchestrator": "Orchestrator",
}


def _select_page(name: str):
    page_updates = [gr.update(visible=(p == name)) for p in PAGES]
    nav_updates = [gr.update(variant=("primary" if p == name else "secondary")) for p in PAGES]
    chat_extra_update = gr.update(visible=(name == "chat"))
    return (*page_updates, *nav_updates, chat_extra_update)


CSS = """
.gradio-container { max-width: 1900px !important; width: 96vw !important; margin: auto; }
#sidebar { background: var(--background-fill-secondary); border-radius: 14px; padding: 14px 12px; }
#sidebar button { justify-content: flex-start !important; text-align: left !important; }
#nav-group button { margin-bottom: 4px !important; }
#agents-accordion { border: none !important; background: transparent !important; }
#trace_box textarea { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 12.5px; }
/* Session list restyled to look like a plain nav list, not radio buttons. */
#session_list .wrap { gap: 2px !important; }
#session_list label {
  border-radius: 8px !important;
  padding: 6px 10px !important;
  margin: 0 !important;
  border: none !important;
  background: transparent !important;
}
#session_list label:hover { background: var(--background-fill-primary) !important; }
#session_list input[type="radio"] { display: none !important; }
#session_list label:has(input:checked) {
  background: var(--color-accent-soft) !important;
  font-weight: 600;
}
footer { display: none !important; }
"""

with gr.Blocks(title="CyberTuringAgnet") as demo:
    gr.Markdown("# CyberTuringAgnet")

    with gr.Row():
        with gr.Column(scale=1, min_width=250, elem_id="sidebar"):
            with gr.Group(elem_id="nav-group"):
                chat_nav_btn = gr.Button("Chat", variant="primary")
                redblue_nav_btn = gr.Button("RedBlue Investigate", variant="secondary")

            with gr.Accordion("Agents", open=False, elem_id="agents-accordion"):
                safety_nav_btn = gr.Button("Safety", variant="secondary", size="sm")
                recon_nav_btn = gr.Button("Recon", variant="secondary", size="sm")
                vuln_nav_btn = gr.Button("Vulnerability Analysis", variant="secondary", size="sm")
                evaluator_nav_btn = gr.Button("Evaluator", variant="secondary", size="sm")
                orchestrator_nav_btn = gr.Button("Orchestrator", variant="secondary", size="sm")

            with gr.Group(visible=True) as chat_sidebar_extra:
                gr.Markdown("&nbsp;")
                new_chat_btn = gr.Button("+ New chat", variant="primary")
                session_list = gr.Radio(choices=[], label="Sessions", value=None, elem_id="session_list")
                delete_btn = gr.Button("Delete session", variant="stop", size="sm")

                with gr.Accordion("Settings", open=False):
                    temperature_slider = gr.Slider(0.0, 2.0, value=DEFAULT_SETTINGS["temperature"], step=0.05, label="Temperature")
                    max_tokens_slider = gr.Slider(256, 8000, value=DEFAULT_SETTINGS["max_tokens"], step=64, label="Max tokens")
                    top_p_slider = gr.Slider(0.0, 1.0, value=DEFAULT_SETTINGS["top_p"], step=0.01, label="Top-p")
                    system_prompt_box = gr.Textbox(
                        value=DEFAULT_SETTINGS["system_prompt"],
                        label="System prompt override",
                        placeholder="Leave empty for default behavior",
                        lines=4,
                    )
                    reset_settings_btn = gr.Button("Reset to defaults", size="sm")

        with gr.Column(scale=4):
            with gr.Column(visible=True) as chat_page:
                session_id_state = gr.State(value=None)
                chatbot = gr.Chatbot(height=560, show_label=False)
                msg_box = gr.Textbox(placeholder="Message CyberTuringAgnet...", show_label=False)

            with gr.Column(visible=False) as redblue_page:
                gr.Markdown(
                    "Runs the full **Safety → Orchestrator → {Recon, Vulnerability Analysis} "
                    "→ Evaluator → …→ END** pipeline for one objective. Single run at a time "
                    "(shared browser subprocess)."
                )
                objective_box = gr.Textbox(
                    label="Objective",
                    placeholder="Investigate CVE-2024-3400 and tell me if we should be worried.",
                )
                run_btn = gr.Button("Run investigation", variant="primary")

                with gr.Row():
                    with gr.Column(scale=2):
                        gr.Markdown("**Agent trace**")
                        trace_box = gr.Textbox(
                            elem_id="trace_box", show_label=False,
                            lines=24, max_lines=24, autoscroll=True, interactive=False,
                        )
                    with gr.Column(scale=1):
                        gr.Markdown("**Findings**")
                        findings_md = gr.Markdown("_No findings yet._")
                        gr.Markdown("**Final answer**")
                        answer_md = gr.Markdown("_Waiting for a run._")

            with gr.Column(visible=False) as safety_page:
                gr.Markdown("### Safety\nDeterministic scope allow/deny check, no LLM call for the common case.")
                s_objective = gr.Textbox(label="Objective")
                s_scope = gr.Textbox(label="Target scope (JSON, optional)", placeholder='{"host": "example.com"}')
                gr.Examples(
                    label="Sample test case",
                    examples=[["Assess CVE-2024-3400 and recommend mitigation steps for our PAN-OS firewalls.", ""]],
                    inputs=[s_objective, s_scope],
                )
                s_btn = gr.Button("Run Safety check", variant="primary")
                s_out = gr.Markdown()

            with gr.Column(visible=False) as recon_page:
                gr.Markdown("### Recon\nOSINT/CVE lookup agent -- browser, NVD API, and the local RAG knowledge base.")
                r_objective = gr.Textbox(label="Objective", placeholder="Look up CVE-2024-3400")
                r_scope = gr.Textbox(label="Target scope (JSON, optional)")
                gr.Examples(
                    label="Sample test case",
                    examples=[["Is CVE-2024-3400 in the CISA KEV catalog?", ""]],
                    inputs=[r_objective, r_scope],
                )
                r_btn = gr.Button("Run Recon", variant="primary")
                r_out = gr.Markdown()

            with gr.Column(visible=False) as vuln_page:
                gr.Markdown("### Vulnerability Analysis\nCVSS vector parsing + MITRE ATT&CK lookup, no browser.")
                v_objective = gr.Textbox(label="Objective")
                v_prior = gr.Textbox(
                    label="Prior findings (optional free text, e.g. a CVSS vector string)",
                    lines=3,
                    placeholder="CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
                )
                gr.Examples(
                    label="Sample test case",
                    examples=[[
                        "Assess the severity of this vulnerability and whether it warrants escalation.",
                        "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
                    ]],
                    inputs=[v_objective, v_prior],
                )
                v_btn = gr.Button("Run Vulnerability Analysis", variant="primary")
                v_out = gr.Markdown()

            with gr.Column(visible=False) as evaluator_page:
                gr.Markdown("### Evaluator\nTwo-tier evidence-grounding judge -- tests only step 2, the LLM judgment.")
                e_claim = gr.Textbox(label="Claim")
                e_excerpt = gr.Textbox(label="Evidence excerpt", lines=3)
                gr.Examples(
                    label="Sample test case",
                    examples=[[
                        "The vulnerability allows an unauthenticated attacker to execute arbitrary code, "
                        "and it is being actively exploited in the wild.",
                        "Palo Alto Networks PAN-OS GlobalProtect feature contains a command injection vulnerability "
                        "that allows an unauthenticated attacker to execute arbitrary code. CISA has confirmed this "
                        "vulnerability is being actively exploited in the wild.",
                    ]],
                    inputs=[e_claim, e_excerpt],
                )
                e_btn = gr.Button("Run Evaluator judgment", variant="primary")
                e_out = gr.Markdown()

            with gr.Column(visible=False) as orchestrator_page:
                gr.Markdown("### Orchestrator\nLLM router -- decides which specialist runs next, or ends the run.")
                o_objective = gr.Textbox(label="Objective")
                o_verified = gr.Textbox(label="Verified findings so far (one claim per line, optional)", lines=4)
                o_last_agent = gr.Textbox(label="Last agent run (optional)", placeholder="recon")
                o_stall = gr.Slider(0, 5, value=0, step=1, label="Consecutive stall count")
                gr.Examples(
                    label="Sample test case",
                    examples=[[
                        "Investigate CVE-2024-3400 and assess the risk to our PAN-OS deployment.",
                        "[recon] CVE-2024-3400 is listed in the CISA KEV catalog with known ransomware campaign use.",
                        "recon",
                        0,
                    ]],
                    inputs=[o_objective, o_verified, o_last_agent, o_stall],
                )
                o_btn = gr.Button("Run Orchestrator routing", variant="primary")
                o_out = gr.Markdown()

    # --- Navigation wiring ---
    page_columns = [chat_page, redblue_page, safety_page, recon_page, vuln_page, evaluator_page, orchestrator_page]
    nav_buttons = [chat_nav_btn, redblue_nav_btn, safety_nav_btn, recon_nav_btn, vuln_nav_btn, evaluator_nav_btn, orchestrator_nav_btn]
    nav_outputs = [*page_columns, *nav_buttons, chat_sidebar_extra]

    for name, btn in zip(PAGES, nav_buttons):
        btn.click(fn=lambda n=name: _select_page(n), outputs=nav_outputs)

    # --- Chat wiring ---
    settings_outputs = [temperature_slider, max_tokens_slider, top_p_slider, system_prompt_box]

    demo.load(
        fn=on_app_load,
        outputs=[session_list, chatbot, session_id_state, *settings_outputs],
    )
    new_chat_btn.click(
        fn=new_chat,
        outputs=[session_list, chatbot, session_id_state, *settings_outputs],
    )
    session_list.change(
        fn=select_session,
        inputs=[session_list],
        outputs=[session_list, chatbot, session_id_state, *settings_outputs],
    )
    delete_btn.click(
        fn=delete_current,
        inputs=[session_id_state],
        outputs=[session_list, chatbot, session_id_state, *settings_outputs],
    )
    reset_settings_btn.click(fn=reset_settings, outputs=settings_outputs)
    msg_box.submit(
        fn=send_message,
        inputs=[msg_box, chatbot, session_id_state, temperature_slider, max_tokens_slider, top_p_slider, system_prompt_box],
        outputs=[chatbot, msg_box, session_list],
        concurrency_limit=1,
    )

    # --- RedBlue Investigate wiring ---
    run_btn.click(
        fn=redblue.run_investigation,
        inputs=[objective_box],
        outputs=[trace_box, findings_md, answer_md],
        concurrency_limit=1,
    )

    # --- Agent pages wiring ---
    s_btn.click(agent_playground.test_safety, inputs=[s_objective, s_scope], outputs=[s_out])
    r_btn.click(agent_playground.test_recon, inputs=[r_objective, r_scope], outputs=[r_out])
    v_btn.click(agent_playground.test_vuln_analysis, inputs=[v_objective, v_prior], outputs=[v_out])
    e_btn.click(agent_playground.test_evaluator, inputs=[e_claim, e_excerpt], outputs=[e_out])
    o_btn.click(
        agent_playground.test_orchestrator,
        inputs=[o_objective, o_verified, o_last_agent, o_stall],
        outputs=[o_out],
    )


if __name__ == "__main__":
    demo.queue().launch(server_name="127.0.0.1", server_port=7860, theme=gr.themes.Soft(), css=CSS)
