# CWE-1088: Synchronous Access of Remote Resource without Timeout

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1088.html  

## Description
The code has a synchronous call to a remote resource, but there is no timeout for the call, or the timeout is set to infinite.

## Related Weaknesses
- ChildOf: CWE-821

## Common Consequences
- Scope: Other; Impact: Reduce Reliability — This issue can prevent the product from running reliably, since an outage for the remote resource can cause the product to hang. If the relevant code is reachable by an attacker, then this reliability problem might introduce a vulnerability.
