# CWE-705: Incorrect Control Flow Scoping

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/705.html  

## Description
The product does not properly return control flow to the proper location after it has completed a task or detected an unusual condition.

## Related Weaknesses
- ChildOf: CWE-691

## Common Consequences
- Scope: Other; Impact: Alter Execution Logic, Other

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following example attempts to resolve a hostname.
- This code queries a server and displays its status when a request comes from an authorized IP address.
- Included in the doPost() method defined below is a call to System.exit() in the event of a specific exception.
