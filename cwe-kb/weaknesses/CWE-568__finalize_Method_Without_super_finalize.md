# CWE-568: finalize() Method Without super.finalize()

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/568.html  

## Description
The product contains a finalize() method that does not call super.finalize().

## Extended Description
The Java Language Specification states that it is a good practice for a finalize() method to call super.finalize().

## Related Weaknesses
- ChildOf: CWE-573
- ChildOf: CWE-459

## Common Consequences
- Scope: Other; Impact: Quality Degradation

## Potential Mitigations
- [Implementation] Call the super.finalize() method.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following method omits the call to super.finalize().
