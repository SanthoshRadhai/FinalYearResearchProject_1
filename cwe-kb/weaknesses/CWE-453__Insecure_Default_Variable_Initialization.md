# CWE-453: Insecure Default Variable Initialization

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/453.html  

## Description
The product, by default, initializes an internal variable with an insecure or less secure value than is possible.

## Related Weaknesses
- ChildOf: CWE-1188

## Common Consequences
- Scope: Integrity; Impact: Modify Application Data — An attacker could gain access to and modify sensitive data or system information.

## Potential Mitigations
- [System Configuration] Disable or change default settings when they can be used to abuse the system. Since those default settings are shipped with the product they are likely to be known by a potential attacker who is familiar with the product. For instance, default credentials should be changed or the associated accounts should be disabled.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- This code attempts to login a user using credentials from a POST request:
