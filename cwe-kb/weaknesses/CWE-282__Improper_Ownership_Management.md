# CWE-282: Improper Ownership Management

**Abstraction:** Class  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/282.html  

## Description
The product assigns the wrong ownership, or does not properly verify the ownership, of an object or resource.

## Related Weaknesses
- ChildOf: CWE-284

## Common Consequences
- Scope: Access Control; Impact: Gain Privileges or Assume Identity

## Potential Mitigations
- [Architecture and Design, Operation] Very carefully manage the setting, management, and handling of privileges. Explicitly manage trust zones in the software.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- This function is part of a privileged program that takes input from users with potentially lower privileges.
