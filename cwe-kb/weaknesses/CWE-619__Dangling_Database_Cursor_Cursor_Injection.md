# CWE-619: Dangling Database Cursor ('Cursor Injection')

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/619.html  

## Description
If a database cursor is not closed properly, then it could become accessible to other users while retaining the same privileges that were originally assigned, leaving the cursor "dangling."

## Extended Description
For example, an improper dangling cursor could arise from unhandled exceptions. The impact of the issue depends on the cursor's role, but SQL injection attacks are commonly possible.

## Related Weaknesses
- ChildOf: CWE-402

## Common Consequences
- Scope: Confidentiality, Integrity; Impact: Read Application Data, Modify Application Data

## Potential Mitigations
- [Implementation] Close cursors immediately after access to them is complete. Ensure that you close cursors if exceptions occur.
