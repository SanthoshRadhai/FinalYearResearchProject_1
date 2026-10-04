# CWE-549: Missing Password Field Masking

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/549.html  

## Description
The product does not mask passwords during entry, increasing the potential for attackers to observe and capture passwords.

## Related Weaknesses
- ChildOf: CWE-522

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism

## Potential Mitigations
- [Implementation, Requirements] Recommendations include requiring all password fields in your web application be masked to prevent other users from seeing this information.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
