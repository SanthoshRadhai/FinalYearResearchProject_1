# CWE-487: Reliance on Package-level Scope

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/487.html  

## Description
Java packages are not inherently closed; therefore, relying on them for code security is not a good practice.

## Extended Description
The purpose of package scope is to prevent accidental access by other parts of a program. This is an ease-of-software-development feature but not a security feature.

## Related Weaknesses
- ChildOf: CWE-664

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data — Any data in a Java package can be accessed outside of the Java framework if the package is distributed.
- Scope: Integrity; Impact: Modify Application Data — The data in a Java class can be modified by anyone outside of the Java framework if the package is distributed.

## Potential Mitigations
- [Architecture and Design, Implementation] Data should be private static and final whenever possible. This will assure that your code is protected by instantiating early, preventing access and tampering.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following example demonstrates the weakness.
