# CWE-482: Comparing instead of Assigning

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/482.html  

## Description
The code uses an operator for comparison when the intention was to perform an assignment.

## Extended Description
In many languages, the compare statement is very close in appearance to the assignment statement; they are often confused.

## Related Weaknesses
- ChildOf: CWE-480

## Common Consequences
- Scope: Availability, Integrity; Impact: Unexpected State — The assignment will not take place, which should cause obvious program execution problems.

## Potential Mitigations
- [Testing] Many IDEs and static analysis products will detect this problem.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
- [Automated Static Analysis - Source Code] An Integrated Development Environment (IDE) or linter can report or highlight this weaknesses.

## Demonstrative Examples (summary)
- The following example demonstrates the weakness.
- The following C/C++ example shows a simple implementation of a stack that includes methods for adding and removing integer values from the stack. The example uses pointers to add and remove integer values to the stack array variable.
