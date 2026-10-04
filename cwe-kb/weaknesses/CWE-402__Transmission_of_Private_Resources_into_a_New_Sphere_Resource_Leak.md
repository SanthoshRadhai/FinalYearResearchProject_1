# CWE-402: Transmission of Private Resources into a New Sphere ('Resource Leak')

**Abstraction:** Class  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/402.html  

## Description
The product makes resources available to untrusted parties when those resources are only intended to be accessed by the product.

## Related Weaknesses
- ChildOf: CWE-668

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
