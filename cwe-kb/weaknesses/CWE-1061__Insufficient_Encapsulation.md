# CWE-1061: Insufficient Encapsulation

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1061.html  

## Description
The product does not sufficiently hide the internal representation and implementation details of data or methods, which might allow external components or modules to modify data unexpectedly, invoke unexpected functionality, or introduce dependencies that the programmer did not intend.

## Related Weaknesses
- ChildOf: CWE-710

## Common Consequences
- Scope: Access Control; Impact: Varies by Context, Bypass Protection Mechanism — An attacker can access data or methods that were not intended to be accessible.
- Scope: Other; Impact: Reduce Maintainability, Increase Analytical Complexity — This issue makes it more difficult to maintain the product, which indirectly affects security by making it more difficult or time-consuming to find and/or fix vulnerabilities. It also might make it easier to introduce vulnerabilities.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following example shows a basic user account class that includes member variables for the username and password as well as a public constructor for the class and a public method to authorize access to the user account.
