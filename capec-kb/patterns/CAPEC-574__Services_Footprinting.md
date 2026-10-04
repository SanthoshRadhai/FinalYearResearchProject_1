# CAPEC-574: Services Footprinting

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/574.html  

## Description
An adversary exploits functionality meant to identify information about the services on the target system to an authorized user. By knowing what services are registered on the target system, the adversary can learn about the target environment as a means towards further malicious behavior. Depending on the operating system, commands that can obtain services information include "sc" and "tasklist/svc" using Tasklist, and "net start" using Net.

## Related Attack Patterns
- ChildOf: CAPEC-169

## Prerequisites
- The adversary must have gained access to the target system via physical or logical means in order to carry out this attack.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Mitigations
- Identify programs that may be used to acquire service information and block them by using a software restriction policy or tools that restrict program execution by uaing a process allowlist.

## Related Weaknesses (CWE)
- CWE-200
