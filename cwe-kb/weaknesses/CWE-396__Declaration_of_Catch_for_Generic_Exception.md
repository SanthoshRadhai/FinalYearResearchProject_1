# CWE-396: Declaration of Catch for Generic Exception

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/396.html  

## Description
Catching overly broad exceptions promotes complex error handling code that is more likely to contain security vulnerabilities.

## Extended Description
Multiple catch blocks can get ugly and repetitive, but "condensing" catch blocks by catching a high-level class like Exception can obscure exceptions that deserve special treatment or that should not be caught at this point in the program. Catching an overly broad exception essentially defeats the purpose of a language's typed exceptions, and can become particularly dangerous if the program grows and begins to throw new types of exceptions. The new exception types will not receive any attention.

## Related Weaknesses
- ChildOf: CWE-705
- ChildOf: CWE-755
- ChildOf: CWE-221

## Common Consequences
- Scope: Non-Repudiation, Other; Impact: Hide Activities — A generic exception can hide details about unexpected adversary activities by making it difficult to properly troubleshoot error conditions during execution.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following code excerpt handles three types of exceptions in an identical fashion.
