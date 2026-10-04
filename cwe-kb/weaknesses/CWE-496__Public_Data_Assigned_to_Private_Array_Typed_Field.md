# CWE-496: Public Data Assigned to Private Array-Typed Field

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/496.html  

## Description
Assigning public data to a private array is equivalent to giving public access to the array.

## Related Weaknesses
- ChildOf: CWE-664

## Common Consequences
- Scope: Integrity; Impact: Modify Application Data — The contents of the array can be modified from outside the intended scope.

## Potential Mitigations
- [Implementation] Do not allow objects to modify private members of a class.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In the example below, the setRoles() method assigns a publically-controllable array to a private field, thus allowing the caller to modify the private array directly by virtue of the fact that arrays in Java are mutable.
