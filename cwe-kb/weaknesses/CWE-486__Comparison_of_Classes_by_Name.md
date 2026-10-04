# CWE-486: Comparison of Classes by Name

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/486.html  

## Description
The product compares classes by name, which can cause it to use the wrong class when multiple classes can have the same name.

## Extended Description
If the decision to trust the methods and data of an object is based on the name of a class, it is possible for malicious users to send objects of the same name as trusted classes and thereby gain the trust afforded to known classes and types.

## Related Weaknesses
- ChildOf: CWE-1025

## Common Consequences
- Scope: Integrity, Confidentiality, Availability; Impact: Execute Unauthorized Code or Commands — If a product relies solely on the name of an object to determine identity, it may execute the incorrect or unintended code.

## Potential Mitigations
- [Implementation] Use class equivalency to determine type. Rather than use the class name to determine if an object is of a given type, use the getClass() method, and == operator.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In this example, the expression in the if statement compares the class of the inputClass object to a trusted class by comparing the class names.
- In this example, the Java class, TrustedClass, overrides the equals method of the parent class Object to determine equivalence of objects of the class. The overridden equals method first determines if the object, obj, is the same class as the TrustedClass object and then compares the object's fields to determine if the objects are equivalent.
