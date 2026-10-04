# CWE-563: Assignment to Variable without Use

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/563.html  

## Description
The variable's value is assigned but never used, making it a dead store.

## Extended Description
After the assignment, the variable is either assigned another value or goes out of scope. It is likely that the variable is simply vestigial, but it is also possible that the unused variable points out a bug.

## Related Weaknesses
- ChildOf: CWE-1164

## Common Consequences
- Scope: Other; Impact: Quality Degradation, Varies by Context — This weakness could be an indication of a bug in the program or a deprecated variable that was not removed and is an indication of poor quality. This could lead to further bugs and the introduction of weaknesses.

## Potential Mitigations
- [Implementation] Remove unused variables from the code.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following code excerpt assigns to the variable r and then overwrites the value without using it.
