# CWE-1096: Singleton Class Instance Creation without Proper Locking or Synchronization

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1096.html  

## Description
The product implements a Singleton design pattern but does not use appropriate locking or other synchronization mechanism to ensure that the singleton class is only instantiated once.

## Related Weaknesses
- ChildOf: CWE-820
- ChildOf: CWE-662
- ChildOf: CWE-662

## Common Consequences
- Scope: Other; Impact: Reduce Reliability — This issue can prevent the product from running reliably, e.g. by making the instantiation process non-thread-safe and introducing deadlock (CWE-833) or livelock conditions. If the relevant code is reachable by an attacker, then this reliability problem might introduce a vulnerability.
