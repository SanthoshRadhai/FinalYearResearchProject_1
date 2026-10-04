# CWE-618: Exposed Unsafe ActiveX Method

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/618.html  

## Description
An ActiveX control is intended for use in a web browser, but it exposes dangerous methods that perform actions that are outside of the browser's security model (e.g. the zone or domain).

## Extended Description
ActiveX controls can exercise far greater control over the operating system than typical Java or javascript. Exposed methods can be subject to various vulnerabilities, depending on the implemented behaviors of those methods, and whether input validation is performed on the provided arguments. If there is no integrity checking or origin validation, this method could be invoked by attackers.

## Related Weaknesses
- ChildOf: CWE-749

## Common Consequences
- Scope: Other; Impact: Other

## Potential Mitigations
- [Implementation] If you must expose a method, make sure to perform input validation on all arguments, and protect against all possible vulnerabilities.
- [Architecture and Design] Use code signing, although this does not protect against any weaknesses that are already in the control.
- [Architecture and Design, System Configuration] Where possible, avoid marking the control as safe for scripting.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
