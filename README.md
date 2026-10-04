# Small Open-Weight LLMs for Security Tasks

Final-year project, Department of Information Technology, Kongu Engineering College.
A measurement study of small open-weight models for security work: knowledge
(CyberMetric), tool calling (BFCL), the capability cost of reducing refusals
(Heretic), and a five-agent LangGraph case study with an evidence-grounding
Evaluator. The paper source is in `Research-Paper resources/paper/`.

## Layout

| Folder | What it holds |
|---|---|
| `RedBlue-MultiAgent/` | The five-agent system (Safety, Orchestrator, Recon, Vulnerability Analysis, Evaluator), its benchmarks, `RESULTS.md`, and the held-out Evaluator on/off study (`build_cve_sets.py`, `bench_g4_onoff.py`, `bench_m3_claims.py`, `analyze_g4*.py`). |
| `CyberTuringAgnet/` | Gradio app: persistent chat sessions, the full RedBlue pipeline with a live trace, and one page per agent. |
| `Benchmark/` | CyberMetric results for six models and `make_figures.py`, which regenerates the paper's figures and statistics. |
| `Research-Paper resources/` | The paper (`paper/paper.tex`, `paper/paper.pdf`), design notes `01`-`12`, and the architecture diagrams. |
| `rag/`, `*-kb/` | Build scripts and READMEs for the local knowledge base (MITRE ATT&CK, CWE, CAPEC, CISA KEV, D3FEND, OWASP). |
| `Langchain/` | Earlier tool-calling experiments against llama.cpp. |
| `findings/` | An earlier model-evaluation note. |

## Running

The agents expect a `llama-server` serving gpt-oss-20b with `--jinja` at
`http://localhost:5500/v1`, a conda environment with the packages in each
folder's `requirements.txt`, and Node 22 for the one browser MCP subprocess.
Always start through the wrapper scripts, which clean up that subprocess:

```bash
cd RedBlue-MultiAgent && ./run_agent.sh        # terminal REPL
cd CyberTuringAgnet   && ./run_app.sh          # Gradio app on http://127.0.0.1:7860
```

To regenerate the paper's CyberMetric figures and statistics: `python Benchmark/make_figures.py`.
Compile the paper with `pdflatex paper.tex` (three passes) inside `Research-Paper resources/paper/`.

## Not in this repository

- **The 100 red-team prompts** used for the refusal experiment. The paper states they are withheld.
- **Third-party code and data** kept locally during the project (CAI, CALDERA, hexstrike-ai, and similar).
- **Raw knowledge-base downloads and `rag/rag_corpus.jsonl`.** Rebuild them with each folder's `build_kb.py` and `rag/ingest.py`.
- **Model weights, local chat history and secrets.**

## Before making the repository public

- Add a license. None has been chosen.
- Check the license of the CyberMetric question files in `Benchmark/CyberMetric/` before redistributing them.
- The design notes in `Research-Paper resources/` still describe a larger planned agent roster than the five agents implemented.
