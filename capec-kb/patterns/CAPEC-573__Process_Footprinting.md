# CAPEC-573: Process Footprinting

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/573.html  

## Description
An adversary exploits functionality meant to identify information about the currently running processes on the target system to an authorized user. By knowing what processes are running on the target system, the adversary can learn about the target environment as a means towards further malicious behavior.

## Related Attack Patterns
- ChildOf: CAPEC-169

## Prerequisites
- The adversary must have gained access to the target system via physical or logical means in order to carry out this attack.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Mitigations
- Identify programs that may be used to acquire process information and block them by using a software restriction policy or tools that restrict program execution by using a process allowlist.

## Related Weaknesses (CWE)
- CWE-200
