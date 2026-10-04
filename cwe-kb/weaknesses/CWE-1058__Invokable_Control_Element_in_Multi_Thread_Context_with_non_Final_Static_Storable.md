# CWE-1058: Invokable Control Element in Multi-Thread Context with non-Final Static Storable or Member Element

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1058.html  

## Description
The code contains a function or method that operates in a multi-threaded environment but owns an unsafe non-final static storable or member data element.

## Related Weaknesses
- ChildOf: CWE-662
- ChildOf: CWE-662
- ChildOf: CWE-662

## Common Consequences
- Scope: Other; Impact: Reduce Reliability — This issue can prevent the product from running reliably. If the relevant code is reachable by an attacker, then this reliability problem might introduce a vulnerability.
