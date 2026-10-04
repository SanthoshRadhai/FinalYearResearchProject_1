# CWE-414: Missing Lock Check

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/414.html  

## Description
A product does not check to see if a lock is present before performing sensitive operations on a resource.

## Related Weaknesses
- ChildOf: CWE-667

## Common Consequences
- Scope: Integrity, Availability; Impact: Modify Application Data, DoS: Instability, DoS: Crash, Exit, or Restart

## Potential Mitigations
- [Architecture and Design, Implementation] Implement a reliable lock mechanism.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
