# CWE-821: Incorrect Synchronization

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/821.html  

## Description
The product utilizes a shared resource in a concurrent manner, but it does not correctly synchronize access to the resource.

## Extended Description
If access to a shared resource is not correctly synchronized, then the resource may not be in a state that is expected by the product. This might lead to unexpected or insecure behaviors, especially if an attacker can influence the shared resource.

## Related Weaknesses
- ChildOf: CWE-662
- ChildOf: CWE-662
- ChildOf: CWE-662

## Common Consequences
- Scope: Integrity, Confidentiality, Other; Impact: Modify Application Data, Read Application Data, Alter Execution Logic

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
