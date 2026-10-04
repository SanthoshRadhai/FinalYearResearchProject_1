# CWE-498: Cloneable Class Containing Sensitive Information

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/498.html  

## Description
The code contains a class with sensitive data, but the class is cloneable. The data can then be accessed by cloning the class.

## Extended Description
Cloneable classes are effectively open classes, since data cannot be hidden in them. Classes that do not explicitly deny cloning can be cloned by any other class without running the constructor.

## Related Weaknesses
- ChildOf: CWE-668
- CanPrecede: CWE-200

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism — A class that can be cloned can be produced without executing the constructor. This is dangerous since the constructor may perform security-related checks. By allowing the object to be cloned, those checks may be bypassed.

## Potential Mitigations
- [Implementation] If you do make your classes clonable, ensure that your clone method is final and throw super.clone().

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following example demonstrates the weakness.
