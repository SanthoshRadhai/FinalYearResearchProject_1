# CWE-499: Serializable Class Containing Sensitive Data

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/499.html  

## Description
The code contains a class with sensitive data, but the class does not explicitly deny serialization. The data can be accessed by serializing the class through another class.

## Extended Description
Serializable classes are effectively open classes since data cannot be hidden in them. Classes that do not explicitly deny serialization can be serialized by any other class, which can then in turn use the data stored inside it.

## Related Weaknesses
- ChildOf: CWE-668
- CanPrecede: CWE-200

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data — an attacker can write out the class to a byte stream, then extract the important data from it.

## Potential Mitigations
- [Implementation] In Java, explicitly define final writeObject() to prevent serialization. This is the recommended solution. Define the writeObject() function to throw an exception explicitly denying serialization.
- [Implementation] Make sure to prevent serialization of your objects.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- This code creates a new record for a medical patient:
