# CWE-783: Operator Precedence Logic Error

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/783.html  

## Description
The product uses an expression in which operator precedence causes incorrect logic to be used.

## Extended Description
While often just a bug, operator precedence logic errors can have serious consequences if they are used in security-critical code, such as making an authentication decision.

## Related Weaknesses
- ChildOf: CWE-670

## Common Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Varies by Context, Unexpected State — The consequences will vary based on the context surrounding the incorrect precedence. In a security decision, integrity or confidentiality are the most likely results. Otherwise, a crash may occur due to the software reaching an unexpected state.

## Potential Mitigations
- [Implementation] Regularly wrap sub-expressions in parentheses, especially in security-critical code.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In the following example, the method validateUser makes a call to another method to authenticate a username and password for a user and returns a success or failure code.
- In this example, the method calculates the return on investment for an accounting/financial application. The return on investment is calculated by subtracting the initial investment costs from the current value and then dividing by the initial investment costs.
