# CAPEC-51: Poison Web Service Registry

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/51.html  

## Description
SOA and Web Services often use a registry to perform look up, get schema information, and metadata about services. A poisoned registry can redirect (think phishing for servers) the service requester to a malicious service provider, provide incorrect information in schema or metadata, and delete information about service provider interfaces.

## Related Attack Patterns
- ChildOf: CAPEC-203

## Prerequisites
- The attacker must be able to write to resources or redirect access to the service registry.

## Skills Required
- [Low] To identify and execute against an over-privileged system interface

## Resources Required
- Capability to directly or indirectly modify registry resources

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Design: Enforce principle of least privilege
- Design: Harden registry server and file access permissions
- Implementation: Implement communications to and from the registry using secure protocols

## Related Weaknesses (CWE)
- CWE-285
- CWE-74
- CWE-693
