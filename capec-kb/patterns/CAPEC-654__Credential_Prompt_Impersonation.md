# CAPEC-654: Credential Prompt Impersonation

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/654.html  

## Description
An adversary, through a previously installed malicious application, impersonates a credential prompt in an attempt to steal a user's credentials.

## Related Attack Patterns
- ChildOf: CAPEC-504

## Prerequisites
- The adversary must already have access to the target system via some means.
- A legitimate task must exist that an adversary can impersonate to glean credentials.

## Skills Required
- [Low] Once an adversary has gained access to the target system, impersonating a credential prompt is not difficult.

## Resources Required
- Malware or some other means to initially comprise the target system.
- Additional malware to impersonate a legitimate credential prompt.

## Consequences
- Scope: Access Control, Authentication; Impact: Gain Privileges

## Mitigations
- The only known mitigation to this attack is to avoid installing the malicious application on the device. However, to impersonate a running task the malicious application does need the GET_TASKS permission to be able to query the task list, and being suspicious of applications with that permission can help.

## Related Weaknesses (CWE)
- CWE-1021
