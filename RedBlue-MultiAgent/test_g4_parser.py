"""Regression tests for g4_common.parse_claim / check_claim, built from the real
claim wordings that the first version of the parser misread (table cells that
answer "No", "returned no matches", and CVSS version strings such as "3.1")."""
import g4_common as g

TRUTH = {"scores": [{"score": 9.8, "severity": "CRITICAL"}]}

CASES = [
    # (text, in_kev, expected_status)
    ("| In CISA KEV catalog? | **No** |", False, "correct"),
    ("2. **CISA KEV catalog** - A search of the CISA Known‑Exploited Vulnerabilities catalog page "
     "returned no matches for “CVE‑2022‑31206”.", False, "correct"),
    ("| CISA KEV catalog | **Yes** (listed on the CISA Known‑Exploited Vulnerabilities Catalog) |", True, "correct"),
    ("| CISA KEV catalog | **Yes** (listed on the CISA Known‑Exploited Vulnerabilities Catalog) |", False, "incorrect"),
    ("| In CISA KEV catalog | **No** – a search of the catalog did not return this CVE. |", False, "correct"),
    ("| In CISA KEV catalog | **No** – a search of the catalog did not return this CVE. |", True, "incorrect"),
    ("- **CISA KEV catalog:** Yes – the vulnerability is listed in the CISA KEV catalog.", True, "correct"),
    ("| CVSS 3.1 Base Score | **9.8** |\n| Severity | **CRITICAL** |", False, "correct"),
    ("CVSS 3.1 Critical, base score 9.8.", False, "correct"),
    ("CVSS v4.0 base score 7.5 HIGH.", False, "incorrect"),
    ("A remote code execution flaw in version 3.1 of the product.", False, "no_checkable_fact"),
    ("It gives the base score, and severity: `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H` with 9.8 CRITICAL.", False, "correct"),
]

bad = 0
for text, kev, expect in CASES:
    r = g.check_claim(text, TRUTH, kev)
    ok = r["status"] == expect
    bad += not ok
    print("OK " if ok else "BAD", f"expect {expect:18s} got {r['status']:18s}", r["parsed"])
print("failures:", bad)
raise SystemExit(1 if bad else 0)
