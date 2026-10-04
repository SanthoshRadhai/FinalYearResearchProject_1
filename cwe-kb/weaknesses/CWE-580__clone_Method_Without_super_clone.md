# CWE-580: clone() Method Without super.clone()

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/580.html  

## Description
The product contains a clone() method that does not call super.clone() to obtain the new object.

## Extended Description
All implementations of clone() should obtain the new object by calling super.clone(). If a class does not follow this convention, a subclass's clone() method will return an object of the wrong type.

## Related Weaknesses
- ChildOf: CWE-664
- ChildOf: CWE-573

## Common Consequences
- Scope: Integrity, Other; Impact: Unexpected State, Quality Degradation

## Potential Mitigations
- [Implementation] Call super.clone() within your clone() method, when obtaining a new object.
- [Implementation] In some cases, you can eliminate the clone method altogether and use copy constructors.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following two classes demonstrate a bug introduced by not calling super.clone(). Because of the way Kibitzer implements clone(), FancyKibitzer's clone method will return an object of type Kibitzer instead of FancyKibitzer.
