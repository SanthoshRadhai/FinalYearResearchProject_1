# CWE-588: Attempt to Access Child of a Non-structure Pointer

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/588.html  

## Description
Casting a non-structure type to a structure type and accessing a field can lead to memory access errors or data corruption.

## Related Weaknesses
- ChildOf: CWE-704
- ChildOf: CWE-758

## Common Consequences
- Scope: Integrity; Impact: Modify Memory — Adjacent variables in memory may be corrupted by assignments performed on fields after the cast.
- Scope: Availability; Impact: DoS: Crash, Exit, or Restart — Execution may end due to a memory access error.

## Potential Mitigations
- [Requirements] The choice could be made to use a language that is not susceptible to these issues.
- [Implementation] Review of type casting operations can identify locations where incompatible types are cast.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following example demonstrates the weakness.
