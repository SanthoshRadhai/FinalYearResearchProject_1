# CWE-495: Private Data Structure Returned From A Public Method

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/495.html  

## Description
The product has a method that is declared public, but returns a reference to a private data structure, which could then be modified in unexpected ways.

## Related Weaknesses
- ChildOf: CWE-664

## Common Consequences
- Scope: Integrity; Impact: Modify Application Data — The contents of the data structure can be modified from outside the intended scope.

## Potential Mitigations
- [Implementation] Declare the method private.
- [Implementation] Clone the member data and keep an unmodified version of the data private to the object.
- [Implementation] Use public setter methods that govern how a private member can be modified.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- Here, a public method in a Java class returns a reference to a private array. Given that arrays in Java are mutable, any modifications made to the returned reference would be reflected in the original private array.
- In this example, the Color class defines functions that return non-const references to private members (an array type and an integer type), which are then arbitrarily altered from outside the control of the class.
