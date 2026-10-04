# CWE-582: Array Declared Public, Final, and Static

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/582.html  

## Description
The product declares an array public, final, and static, which is not sufficient to prevent the array's contents from being modified.

## Extended Description
Because arrays are mutable objects, the final constraint requires that the array object itself be assigned only once, but makes no guarantees about the values of the array elements. Since the array is public, a malicious program can change the values stored in the array. As such, in most cases an array declared public, final and static is a bug.

## Related Weaknesses
- ChildOf: CWE-668

## Common Consequences
- Scope: Integrity; Impact: Modify Application Data

## Potential Mitigations
- [Implementation] In most situations the array should be made private.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following Java Applet code mistakenly declares an array public, final and static.
