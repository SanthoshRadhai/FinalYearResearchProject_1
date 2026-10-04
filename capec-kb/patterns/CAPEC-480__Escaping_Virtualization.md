# CAPEC-480: Escaping Virtualization

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/480.html  

## Description
An adversary gains access to an application, service, or device with the privileges of an authorized or privileged user by escaping the confines of a virtualized environment. The adversary is then able to access resources or execute unauthorized code within the host environment, generally with the privileges of the user running the virtualized process. Successfully executing an attack of this type is often the first step in executing more complex attacks.

## Related Attack Patterns
- ChildOf: CAPEC-115

## Consequences
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Accountability, Authentication, Authorization, Non-Repudiation; Impact: Gain Privileges

## Mitigations
- Ensure virtualization software is current and up-to-date.
- Abide by the least privilege principle to avoid assigning users more privileges than necessary.

## Related Weaknesses (CWE)
- CWE-693
