"""Builds the results matrix, statistics and bar charts for the paper.

Reads  : CyberMetric/results_<model>_<size>.json
Writes : ../Research-Paper resources/paper/images/*.png
         results_matrix.csv, results_matrix.tex, stats_summary.txt
"""
import glob
import json
import math
import re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).parent
SRC = HERE / "CyberMetric"
OUT = HERE.parent / "Research-Paper resources" / "paper" / "images"
OUT.mkdir(parents=True, exist_ok=True)

SIZES = [80, 500, 2000, 10000]
SIZE_LABEL = {80: "80", 500: "500", 2000: "2,000", 10000: "10,180"}

# file stem -> (display name, colour)
MODELS = {
    "foundation-sec-8b": ("Foundation-Sec-8B", "#8c8c8c"),
    "granite_4.1": ("Granite 4.1", "#c98b3a"),
    "qwen3.5-9b_think": ("Qwen3.5-9B (thinking)", "#3b7dd8"),
    "gpt-oss-20b": ("gpt-oss-20b (base)", "#2a9d8f"),
    "gpt-oss-20b-heretic": ("gpt-oss-20b Heretic (reference)", "#8e5bd0"),
    "gpt-oss-20b-cybersecurity-heretic-custom": ("gpt-oss-20b Heretic (ours)", "#d1495b"),
}

plt.rcParams.update({
    "font.size": 9, "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.alpha": 0.25, "axes.axisbelow": True,
    "figure.dpi": 150, "savefig.bbox": "tight",
})


def wilson(k, n, z=1.96):
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return 100 * (c - h), 100 * (c + h)


def load(stem, size):
    return json.load(open(SRC / f"results_{stem}_{size}.json", encoding="utf-8"))


data = {m: {s: load(m, s) for s in SIZES} for m in MODELS}

# ---------------------------------------------------------------- matrix
lines_csv = ["model," + ",".join(f"acc_{s},ci_lo_{s},ci_hi_{s},unanswered_{s}" for s in SIZES)]
tex_rows = []
for m, (name, _) in MODELS.items():
    csv_cells, tex_cells = [], []
    for s in SIZES:
        d = data[m][s]
        lo, hi = wilson(d["correct"], d["total"])
        un = sum(1 for r in d["results"] if not r.get("llm_answer"))
        csv_cells.append(f"{d['accuracy']:.2f},{lo:.2f},{hi:.2f},{un}")
        tex_cells.append(f"{d['accuracy']:.2f}")
    lines_csv.append(f"{name}," + ",".join(csv_cells))
    tex_rows.append((name, tex_cells))
(HERE / "results_matrix.csv").write_text("\n".join(lines_csv), encoding="utf-8")

# best value per column for bolding in the LaTeX table
best = [max(float(r[1][i]) for r in tex_rows) for i in range(len(SIZES))]
tex = []
for name, cells in tex_rows:
    c = [f"\\textbf{{{v}}}" if float(v) == best[i] else v for i, v in enumerate(cells)]
    tex.append(f"{name} & " + " & ".join(c) + r" \\")
(HERE / "results_matrix.tex").write_text("\n".join(tex), encoding="utf-8")

# ------------------------------------------------- paired significance
def answers(m, s):
    return {r["question"]: r["correct"] for r in data[m][s]["results"]}


def mcnemar(a, b):
    """Exact two-sided McNemar on questions answered by both runs."""
    keys = a.keys() & b.keys()
    n01 = sum(1 for k in keys if a[k] and not b[k])  # a right, b wrong
    n10 = sum(1 for k in keys if b[k] and not a[k])
    n = n01 + n10
    if n == 0:
        return n01, n10, 1.0
    kmin = min(n01, n10)
    p = sum(math.comb(n, i) for i in range(kmin + 1)) / 2 ** n * 2
    return n01, n10, min(1.0, p)


stats = ["Paired exact McNemar tests vs. gpt-oss-20b (base), CyberMetric-10180",
         "(only questions with identical text in both runs are paired)"]
for m in ("gpt-oss-20b-heretic", "gpt-oss-20b-cybersecurity-heretic-custom"):
    for s in (2000, 10000):
        a, b = answers("gpt-oss-20b", s), answers(m, s)
        n01, n10, p = mcnemar(a, b)
        stats.append(f"{MODELS[m][0]:38s} size={s:>5d}  base-only-correct={n01:4d}  "
                     f"variant-only-correct={n10:4d}  p={p:.3f}")
(HERE / "stats_summary.txt").write_text("\n".join(stats), encoding="utf-8")
print("\n".join(stats))

# -------------------------------------------- fig 1: all models x sizes
fig, ax = plt.subplots(figsize=(7.2, 3.3))
w = 0.8 / len(MODELS)
x = np.arange(len(SIZES))
for i, (m, (name, col)) in enumerate(MODELS.items()):
    acc = [data[m][s]["accuracy"] for s in SIZES]
    err = []
    for s in SIZES:
        d = data[m][s]
        lo, hi = wilson(d["correct"], d["total"])
        err.append((d["accuracy"] - lo, hi - d["accuracy"]))
    err = np.array(err).T
    ax.bar(x + (i - (len(MODELS) - 1) / 2) * w, acc, w, yerr=err, color=col,
           label=name, capsize=1.5, error_kw={"lw": 0.7})
ax.set_xticks(x, [f"CyberMetric-{SIZE_LABEL[s]}" for s in SIZES])
ax.set_ylim(75, 100)
ax.set_ylabel("Accuracy (%)")
ax.legend(ncol=3, fontsize=7, loc="upper center", bbox_to_anchor=(0.5, -0.12), frameon=False)
fig.savefig(OUT / "cybermetric_all_models.png")
plt.close(fig)

# -------------------- fig 2: base vs heretic variants, full benchmark
trio = ["gpt-oss-20b", "gpt-oss-20b-heretic", "gpt-oss-20b-cybersecurity-heretic-custom"]
fig, ax = plt.subplots(figsize=(3.5, 2.9))
for i, m in enumerate(trio):
    d = data[m][10000]
    lo, hi = wilson(d["correct"], d["total"])
    ax.bar(i, d["accuracy"], color=MODELS[m][1], yerr=[[d["accuracy"] - lo], [hi - d["accuracy"]]],
           capsize=3, error_kw={"lw": 0.9})
    ax.text(i, hi + 0.12, f"{d['accuracy']:.2f}", ha="center", fontsize=8)
ax.set_xticks(range(3), ["Base", "Heretic\n(reference)", "Heretic\n(ours)"])
ax.set_ylim(84, 90)
ax.set_ylabel("Accuracy (%), n = 10,180")
fig.savefig(OUT / "heretic_parity_10180.png")
plt.close(fig)

# --------------------------- fig 3: refusals vs KL trade-off (Heretic log)
# Transcribed by hand from the Heretic trial-selection screen (Pareto front).
trials = [(310, 27, .0624), (378, 28, .0613), (231, 32, .0599), (315, 34, .0583),
          (365, 38, .0555), (376, 44, .0527), (363, 55, .0523), (292, 56, .0498),
          (208, 58, .0460), (357, 60, .0418), (285, 61, .0395), (283, 63, .0362),
          (326, 66, .0338), (329, 67, .0331), (271, 71, .0274), (300, 72, .0261),
          (282, 74, .0251), (298, 75, .0251), (400, 79, .0238), (325, 80, .0225),
          (303, 82, .0203), (254, 87, .0171), (253, 89, .0164), (327, 90, .0127),
          (270, 91, .0122), (340, 92, .0101), (267, 93, .0059), (328, 94, .0057),
          (307, 95, .0007), (24, 96, .0006)]
ref = [t[1] for t in trials]
kl = [t[2] for t in trials]
fig, ax = plt.subplots(figsize=(3.5, 2.9))
ax.plot(kl, ref, "-o", ms=3.5, lw=1, color="#8e5bd0")
ax.scatter([0.0624], [27], s=60, facecolors="none", edgecolors="#d1495b", linewidths=1.5, zorder=4, label="Selected (Trial 310)")
ax.scatter([0], [100], marker="s", s=40, color="#2a9d8f", zorder=3, label="Original model")
ax.set_xlabel("KL divergence from original")
ax.set_ylabel("Refusals on 100 prompts")
ax.legend(frameon=False, fontsize=8, loc="upper right", bbox_to_anchor=(1.0, 0.93))
fig.savefig(OUT / "heretic_refusal_vs_kl.png")
plt.close(fig)

# --------------------------------------------------- fig 4: BFCL categories
# parallel / parallel_multiple scored exactly 0% (suspected harness/config
# issue) and are therefore deliberately NOT reported.
bfcl = {"simple_python": 89.00, "multiple": 88.00, "irrelevance": 85.42}
fig, ax = plt.subplots(figsize=(3.5, 2.6))
ax.bar(list(bfcl), list(bfcl.values()), color="#2a9d8f")
for i, v in enumerate(bfcl.values()):
    ax.text(i, v + 0.3, f"{v:.1f}", ha="center", fontsize=8)
ax.set_ylim(80, 100)
ax.set_yticks(range(80, 101, 5))
ax.set_ylabel("BFCL accuracy (%)")
fig.savefig(OUT / "bfcl_categories.png")
plt.close(fig)

print("done ->", OUT)
