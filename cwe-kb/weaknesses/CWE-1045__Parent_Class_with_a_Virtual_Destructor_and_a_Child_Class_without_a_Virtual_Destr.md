# CWE-1045: Parent Class with a Virtual Destructor and a Child Class without a Virtual Destructor

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1045.html  

## Description
A parent class has a virtual destructor method, but the parent has a child class that does not have a virtual destructor.

## Related Weaknesses
- ChildOf: CWE-1076

## Common Consequences
- Scope: Other; Impact: Reduce Reliability — This issue can prevent the product from running reliably, since the child might not perform essential destruction operations. If the relevant code is reachable by an attacker, then this reliability problem might introduce a vulnerability, such as a memory leak (CWE-401).
