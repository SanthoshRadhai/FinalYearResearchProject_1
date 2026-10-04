# CAPEC-586: Object Injection

**Abstraction:** Meta  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/586.html  

## Description
An adversary attempts to exploit an application by injecting additional, malicious content during its processing of serialized objects. Developers leverage serialization in order to convert data or state into a static, binary format for saving to disk or transferring over a network. These objects are then deserialized when needed to recover the data/state. By injecting a malformed object into a vulnerable application, an adversary can potentially compromise the application by manipulating the deserialization process. This can result in a number of unwanted outcomes, including remote code execution.

## Prerequisites
- The target application must unserialize data before validation.

## Consequences
- Scope: Availability; Impact: Resource Consumption
- Scope: Integrity; Impact: Modify Data
- Scope: Authorization; Impact: Execute Unauthorized Commands

## Mitigations
- Implementation: Validate object before deserialization process
- Design: Limit which types can be deserialized.
- Implementation: Avoid having unnecessary types or gadgets available that can be leveraged for malicious ends. Use an allowlist of acceptable classes.
- Implementation: Keep session state on the server, when possible.

## Related Weaknesses (CWE)
- CWE-502
