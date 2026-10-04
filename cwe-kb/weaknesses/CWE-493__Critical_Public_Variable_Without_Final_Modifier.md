# CWE-493: Critical Public Variable Without Final Modifier

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/493.html  

## Description
The product has a critical public variable that is not final, which allows the variable to be modified to contain unexpected values.

## Extended Description
If a field is non-final and public, it can be changed once the value is set by any function that has access to the class which contains the field. This could lead to a vulnerability if other parts of the program make assumptions about the contents of that field.

## Related Weaknesses
- ChildOf: CWE-668

## Common Consequences
- Scope: Integrity; Impact: Modify Application Data — The object could potentially be tampered with.
- Scope: Confidentiality; Impact: Read Application Data — The object could potentially allow the object to be read.

## Potential Mitigations
- [Implementation] Declare all public fields as final when possible, especially if it is used to maintain internal state of an Applet or of classes used by an Applet. If a field must be public, then perform all appropriate sanity checks before accessing the field from your code.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- Suppose this WidgetData class is used for an e-commerce web site. The programmer attempts to prevent price-tampering attacks by setting the price of the widget using the constructor.
- Assume the following code is intended to provide the location of a configuration file that controls execution of the application.
