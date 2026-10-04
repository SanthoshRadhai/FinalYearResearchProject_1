# CWE-607: Public Static Final Field References Mutable Object

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/607.html  

## Description
A public or protected static final field references a mutable object, which allows the object to be changed by malicious code, or accidentally from another package.

## Related Weaknesses
- ChildOf: CWE-471

## Common Consequences
- Scope: Integrity; Impact: Modify Application Data

## Potential Mitigations
- [Implementation] Protect mutable objects by making them private. Restrict access to the getter and setter as well.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- Here, an array (which is inherently mutable) is labeled public static final.
