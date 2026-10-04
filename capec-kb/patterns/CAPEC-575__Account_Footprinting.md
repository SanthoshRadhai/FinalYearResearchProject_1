# CAPEC-575: Account Footprinting

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/575.html  

## Description
An adversary exploits functionality meant to identify information about the domain accounts and their permissions on the target system to an authorized user. By knowing what accounts are registered on the target system, the adversary can inform further and more targeted malicious behavior. Example Windows commands which can acquire this information are: "net user" and "dsquery".

## Related Attack Patterns
- ChildOf: CAPEC-169

## Prerequisites
- The adversary must have gained access to the target system via physical or logical means in order to carry out this attack.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Mitigations
- Identify programs that may be used to acquire account information and block them by using a software restriction policy or tools that restrict program execution by uysing a process allowlist.

## Related Weaknesses (CWE)
- CWE-200
