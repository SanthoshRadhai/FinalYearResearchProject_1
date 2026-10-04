# CAPEC-578: Disable Security Software

**Abstraction:** Standard  
**Status:** Usable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/578.html  

## Description
An adversary exploits a weakness in access control to disable security tools so that detection does not occur. This can take the form of killing processes, deleting registry keys so that tools do not start at run time, deleting log files, or other methods.

## Related Attack Patterns
- ChildOf: CAPEC-176

## Prerequisites
- The adversary must have the capability to interact with the configuration of the targeted system.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Availability; Impact: Hide Activities

## Mitigations
- Ensure proper permissions are in place to prevent adversaries from altering the execution status of security tools.

## Related Weaknesses (CWE)
- CWE-284
