# CWE-820: Missing Synchronization

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/820.html  

## Description
The product utilizes a shared resource in a concurrent manner but does not attempt to synchronize access to the resource.

## Extended Description
If access to a shared resource is not synchronized, then the resource may not be in a state that is expected by the product. This might lead to unexpected or insecure behaviors, especially if an attacker can influence the shared resource.

## Related Weaknesses
- ChildOf: CWE-662
- ChildOf: CWE-662
- ChildOf: CWE-662

## Common Consequences
- Scope: Integrity, Confidentiality, Other; Impact: Modify Application Data, Read Application Data, Alter Execution Logic

## Demonstrative Examples (summary)
- The following code intends to fork a process, then have both the parent and child processes print a single line.
