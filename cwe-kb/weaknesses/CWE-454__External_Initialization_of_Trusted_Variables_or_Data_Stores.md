# CWE-454: External Initialization of Trusted Variables or Data Stores

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/454.html  

## Description
The product initializes critical internal variables or data stores using inputs that can be modified by untrusted actors.

## Extended Description
A product system should be reluctant to trust variables that have been initialized outside of its trust boundary, especially if they are initialized by users. The variables may have been initialized incorrectly. If an attacker can initialize the variable, then they can influence what the vulnerable system will do.

## Related Weaknesses
- ChildOf: CWE-1419
- CanAlsoBe: CWE-456

## Common Consequences
- Scope: Integrity; Impact: Modify Application Data — An attacker could gain access to and modify sensitive data or system information.

## Potential Mitigations
- [Implementation] A product system should be reluctant to trust variables that have been initialized outside of its trust boundary. Ensure adequate checking (e.g. input validation) is performed when relying on input from outside a trust boundary.
- [Architecture and Design] Avoid any external control of variables. If necessary, restrict the variables that can be modified using an allowlist, and use a different namespace or naming convention if possible.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In the Java example below, a system property controls the debug level of the application.
- This code checks the HTTP POST request for a debug switch, and enables a debug mode if the switch is set.
