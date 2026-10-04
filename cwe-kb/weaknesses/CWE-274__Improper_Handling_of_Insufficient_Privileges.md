# CWE-274: Improper Handling of Insufficient Privileges

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/274.html  

## Description
The product does not handle or incorrectly handles when it has insufficient privileges to perform an operation, leading to resultant weaknesses.

## Related Weaknesses
- ChildOf: CWE-755
- ChildOf: CWE-269
- PeerOf: CWE-271
- CanAlsoBe: CWE-280

## Common Consequences
- Scope: Other; Impact: Other, Alter Execution Logic

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
