# CWE-394: Unexpected Status Code or Return Value

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/394.html  

## Description
The product does not properly check when a function or operation returns a value that is legitimate for the function, but is not expected by the product.

## Related Weaknesses
- ChildOf: CWE-754

## Common Consequences
- Scope: Integrity, Other; Impact: Unexpected State, Alter Execution Logic

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
