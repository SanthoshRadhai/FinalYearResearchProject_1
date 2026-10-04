const statusEl = document.getElementById("status");
const runForm = document.getElementById("run-form");
const objectiveInput = document.getElementById("objective");
const runBtn = document.getElementById("run-btn");
const traceFeed = document.getElementById("trace-feed");
const findingsFeed = document.getElementById("findings-feed");
const answerFeed = document.getElementById("answer-feed");

function setStatus(text, cls) {
  statusEl.textContent = text;
  statusEl.className = "status " + cls;
}

function fmtTime(ts) {
  const d = new Date(ts * 1000);
  return d.toLocaleTimeString([], { hour12: false });
}

function escapeHtml(text) {
  const div = document.createElement("div");
  div.textContent = text;
  return div.innerHTML;
}

// Findings/final-answer text is LLM-generated Markdown (headers, tables,
// bold, lists) -- render it properly instead of showing raw "**bold**"
// syntax. Falls back to escaped plain text if the marked.js CDN script
// didn't load (e.g. offline), so a network hiccup degrades gracefully
// rather than breaking the page.
function renderMarkdown(text) {
  if (typeof marked !== "undefined") {
    return marked.parse(text || "");
  }
  return `<p>${escapeHtml(text || "")}</p>`;
}

function appendTrace(entry) {
  const row = document.createElement("div");
  row.className = "trace-entry";

  const time = document.createElement("span");
  time.className = "trace-time";
  time.textContent = fmtTime(entry.ts || Date.now() / 1000);

  const node = document.createElement("span");
  node.className = "trace-node node-" + (entry.node || "graph");
  node.textContent = entry.node || "graph";

  const msg = document.createElement("span");
  msg.className = "trace-message";
  let text = `[${entry.event}] ${entry.message}`;
  if (entry.reason) text += ` (reason: ${entry.reason})`;
  msg.textContent = text;

  row.append(time, node, msg);
  traceFeed.appendChild(row);
  traceFeed.scrollTop = traceFeed.scrollHeight;
}

function renderFindings(verified, rejected) {
  findingsFeed.innerHTML = "";
  const all = [
    ...(verified || []).map((f) => ({ ...f, badge: "verified" })),
    ...(rejected || []).map((f) => ({ ...f, badge: "rejected" })),
  ];
  if (all.length === 0) {
    findingsFeed.innerHTML = '<p class="empty">No findings yet.</p>';
    return;
  }
  for (const f of all) {
    const card = document.createElement("div");
    card.className = "finding-card";
    const badge = document.createElement("span");
    badge.className = "finding-badge " + f.badge;
    badge.textContent = f.badge;
    const source = document.createElement("div");
    source.className = "finding-source";
    source.textContent = `[${f.source_agent}]`;
    const claim = document.createElement("div");
    claim.className = "markdown-body";
    claim.innerHTML = renderMarkdown(f.claim);
    card.append(badge, source, claim);
    findingsFeed.appendChild(card);
  }
}

function renderFinal(payload) {
  if (payload.ok === false) {
    setStatus("error", "error");
    answerFeed.innerHTML = `<p class="empty">Error: ${payload.error || "unknown error"}</p>`;
    return;
  }
  setStatus("done", "done");
  renderFindings(payload.verified_findings, payload.rejected_findings);
  answerFeed.innerHTML = "";
  runBtn.disabled = false;

  if (payload.halted) {
    answerFeed.textContent = `[halted] ${payload.halt_reason}`;
    return;
  }

  // The final message is the model's own wrap-up text -- it can read as
  // confident and complete even when EVERY finding behind it was rejected
  // by the Evaluator (see RESULTS.md §8c/§8d: the model still produces a
  // natural-sounding answer after a stall-limit abort). Never let that look
  // the same as an answer actually backed by verified evidence.
  if ((payload.verified_findings || []).length === 0) {
    const warning = document.createElement("p");
    warning.className = "unverified-warning";
    warning.textContent =
      "⚠ No verified findings support this answer (see Findings panel — " +
      "the Evaluator rejected every claim). Treat the text below with caution.";
    answerFeed.appendChild(warning);
  }

  const answerText = document.createElement("div");
  answerText.className = "markdown-body";
  answerText.innerHTML = renderMarkdown(payload.answer || "(no answer produced)");
  answerFeed.appendChild(answerText);
}

function connectWebSocket() {
  const proto = location.protocol === "https:" ? "wss:" : "ws:";
  const ws = new WebSocket(`${proto}//${location.host}/ws`);

  ws.onmessage = (ev) => {
    const data = JSON.parse(ev.data);
    if (data.type === "final") {
      renderFinal(data);
    } else {
      appendTrace(data);
    }
  };

  ws.onclose = () => {
    // Auto-reconnect -- the server loops waiting for the next run, so a
    // dropped connection (e.g. page reload) shouldn't need a manual retry.
    setTimeout(connectWebSocket, 1000);
  };

  return ws;
}

connectWebSocket();

runForm.addEventListener("submit", async (ev) => {
  ev.preventDefault();
  const objective = objectiveInput.value.trim();
  if (!objective) return;

  traceFeed.innerHTML = "";
  findingsFeed.innerHTML = '<p class="empty">No findings yet.</p>';
  answerFeed.innerHTML = '<p class="empty">Running...</p>';
  runBtn.disabled = true;
  setStatus("running", "running");

  const resp = await fetch("/api/run", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ objective }),
  });

  if (!resp.ok) {
    const err = await resp.json();
    setStatus("error", "error");
    answerFeed.innerHTML = `<p class="empty">${err.error || "Failed to start run."}</p>`;
    runBtn.disabled = false;
  }
});
