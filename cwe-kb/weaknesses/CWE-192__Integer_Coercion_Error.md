# CWE-192: Integer Coercion Error

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/192.html  

## Description
Integer coercion refers to a set of flaws pertaining to the type casting, extension, or truncation of primitive data types.

## Extended Description
Several flaws fall under the category of integer coercion errors. For the most part, these errors in and of themselves result only in availability and data integrity issues. However, in some circumstances, they may result in other, more complicated security related flaws, such as buffer overflow conditions.

## Related Weaknesses
- ChildOf: CWE-681

## Common Consequences
- Scope: Availability; Impact: DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory), DoS: Crash, Exit, or Restart — Integer coercion often leads to undefined states of execution resulting in infinite loops or crashes.
- Scope: Integrity, Confidentiality, Availability; Impact: Execute Unauthorized Code or Commands — In some cases, integer coercion errors can lead to exploitable buffer overflow conditions, resulting in the execution of arbitrary code.
- Scope: Integrity, Other; Impact: Other — Integer coercion errors result in an incorrect value being stored for the variable in question.

## Potential Mitigations
- [Requirements] A language which throws exceptions on ambiguous data casts might be chosen.
- [Architecture and Design] Design objects and program flow such that multiple or complex casts are unnecessary
- [Implementation] Ensure that any data type casting that you must used is entirely understood in order to reduce the plausibility of error in use.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following code is intended to read an incoming packet from a socket and extract one or more headers.
- The following code reads a maximum size and performs validation on that size. It then performs a strncpy, assuming it will not exceed the boundaries of the array. While the use of "short s" is forced in this particular example, short int's are frequently used within real-world code, such as code that processes structured data.
