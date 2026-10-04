# CWE-491: Public cloneable() Method Without Final ('Object Hijack')

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/491.html  

## Description
A class has a cloneable() method that is not declared final, which allows an object to be created without calling the constructor. This can cause the object to be in an unexpected state.

## Related Weaknesses
- ChildOf: CWE-668

## Common Consequences
- Scope: Integrity, Other; Impact: Unexpected State, Varies by Context

## Potential Mitigations
- [Implementation] Make the cloneable() method final.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In this example, a public class "BankAccount" implements the cloneable() method which declares "Object clone(string accountnumber)":
- In the example below, a clone() method is defined without being declared final.
