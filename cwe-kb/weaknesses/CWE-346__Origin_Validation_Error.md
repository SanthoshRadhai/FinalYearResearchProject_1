# CWE-346: Origin Validation Error

**Abstraction:** Class  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/346.html  

## Description
The product does not properly verify that the source of data or communication is valid.

## Related Weaknesses
- ChildOf: CWE-345
- ChildOf: CWE-345
- ChildOf: CWE-284

## Common Consequences
- Scope: Access Control, Other; Impact: Gain Privileges or Assume Identity, Varies by Context — An attacker can access any functionality that is inadvertently accessible to the source.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- This Android application will remove a user account when it receives an intent to do so:
- These Android and iOS applications intercept URL loading within a WebView and perform special actions if a particular URL scheme is used, thus allowing the Javascript within the WebView to communicate with the application:
