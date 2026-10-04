# CWE-253: Incorrect Check of Function Return Value

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/253.html  

## Description
The product incorrectly checks a return value from a function, which prevents it from detecting errors or exceptional conditions.

## Extended Description
Important and common functions will return some value about the success of its actions. This will alert the program whether or not to handle any errors caused by that function.

## Related Weaknesses
- ChildOf: CWE-573
- ChildOf: CWE-754

## Common Consequences
- Scope: Availability, Integrity; Impact: Unexpected State, DoS: Crash, Exit, or Restart — An unexpected return value could place the system in a state that could lead to a crash or other unintended behaviors.

## Potential Mitigations
- [Architecture and Design] Use a language or compiler that uses exceptions and requires the catching of those exceptions.
- [Implementation] Properly check all functions which return a value.
- [Implementation] When designing any function make sure you return a value or throw an exception in case of an error.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- This code attempts to allocate memory for 4 integers and checks if the allocation succeeds.
