# CWE-583: finalize() Method Declared Public

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/583.html  

## Description
The product violates secure coding principles for mobile code by declaring a finalize() method public.

## Extended Description
A product should never call finalize explicitly, except to call super.finalize() inside an implementation of finalize(). In mobile code situations, the otherwise error prone practice of manual garbage collection can become a security threat if an attacker can maliciously invoke a finalize() method because it is declared with public access.

## Related Weaknesses
- ChildOf: CWE-668

## Common Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Alter Execution Logic, Execute Unauthorized Code or Commands, Modify Application Data

## Potential Mitigations
- [Implementation] If you are using finalize() as it was designed, there is no reason to declare finalize() with anything other than protected access.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following Java Applet code mistakenly declares a public finalize() method.
