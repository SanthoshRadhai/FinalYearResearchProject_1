# CWE-397: Declaration of Throws for Generic Exception

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/397.html  

## Description
The product throws or raises an overly broad exceptions that can hide important details and produce inappropriate responses to certain conditions.

## Extended Description
Declaring a method to throw Exception or Throwable promotes generic error handling procedures that make it difficult for callers to perform proper error handling and error recovery. For example, Java's exception mechanism makes it easy for callers to anticipate what can go wrong and write code to handle each specific exceptional circumstance. Declaring that a method throws a generic form of exception defeats this system.

## Related Weaknesses
- ChildOf: CWE-705
- ChildOf: CWE-221
- ChildOf: CWE-703

## Common Consequences
- Scope: Non-Repudiation, Other; Impact: Hide Activities, Alter Execution Logic — Throwing a generic exception can hide details about unexpected adversary activities by making it difficult to properly troubleshoot error conditions during execution.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following method throws three types of exceptions.
- Early versions of C++ (C++98, C++03, C++11) included a feature known as Dynamic Exception Specification. This allowed functions to declare what type of exceptions it may throw. It is possible to declare a general class of exception to cover any derived exceptions that may be thrown.
