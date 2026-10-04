"""Deterministic CVSS vector parsing — no LLM call, no network, no subprocess.

Per Research-Paper resources/07-...ARCHITECTURE.md §5.2: the Vulnerability
Analysis Agent must never re-derive a CVSS score itself from prose; it extracts
the vendor/NVD-published vector string verbatim and hands it to this tool for a
mechanical severity readout.

Requires: pip install cvss  (RedHatProductSecurity/cvss)
"""

from langchain_core.tools import tool

try:
    from cvss import CVSS2, CVSS3, CVSS4
except ImportError as e:  # pragma: no cover
    raise ImportError(
        "The 'cvss' package is required (pip install cvss). "
        "See Research-Paper resources/08-MCP-TOOL-IMPLEMENTATION-OPTIONS.md §1.7."
    ) from e


@tool
def parse_cvss_vector(vector: str) -> dict:
    """Parse a CVSS vector string (v2, v3.x, or v4.0) and return its base score
    and severity rating, computed deterministically — not estimated by the model.

    Args:
        vector: The full CVSS vector string, e.g.
            "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H" (as published by NVD).

    Returns:
        dict with keys: version, base_score, severity, vector (echoed back).
        On a malformed vector, returns {"error": "<message>"} instead of raising,
        so the calling agent can report the failure rather than crash the turn.
    """
    vector = vector.strip()
    try:
        if vector.startswith("CVSS:4.0"):
            c = CVSS4(vector)
            score = c.base_score
            severity = c.severity
        elif vector.startswith("CVSS:3"):
            c = CVSS3(vector)
            score = c.base_score
            severity = c.severities()[0]
        else:
            # RedHatProductSecurity/cvss's CVSS2 expects the bare metric string
            # (e.g. "AV:N/AC:L/Au:N/C:P/I:N/A:N"), NOT a "CVSS:2.0/" prefix —
            # unlike v3/v4 vectors, NVD-style v2 vectors are sometimes quoted
            # both ways in the wild. Strip the prefix if present so both forms
            # parse (found via testing: NVD's own historical v2 records use the
            # bare form, but some tooling/documentation prepends "CVSS:2.0/").
            v2_vector = vector
            for prefix in ("CVSS:2.0/", "CVSS2.0/", "CVSS:2/"):
                if v2_vector.startswith(prefix):
                    v2_vector = v2_vector[len(prefix):]
                    break
            c = CVSS2(v2_vector)
            score = c.base_score
            severity = c.severities()[0]
        return {
            "version": "4.0" if vector.startswith("CVSS:4.0") else ("3.x" if vector.startswith("CVSS:3") else "2.0"),
            "base_score": score,
            "severity": severity,
            "vector": vector,
        }
    except Exception as e:
        return {"error": f"could not parse CVSS vector '{vector}': {e}"}
