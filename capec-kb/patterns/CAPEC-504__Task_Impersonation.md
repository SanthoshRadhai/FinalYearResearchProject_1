# CAPEC-504: Task Impersonation

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/504.html  

## Description
An adversary, through a previously installed malicious application, impersonates an expected or routine task in an attempt to steal sensitive information or leverage a user's privileges.

## Related Attack Patterns
- ChildOf: CAPEC-173

## Prerequisites
- The adversary must already have access to the target system via some means.
- A legitimate task must exist that an adversary can impersonate to glean credentials.
- The user's privileges allow them to execute certain tasks with elevated privileges.

## Skills Required
- [Low] Once an adversary has gained access to the target system, impersonating a task is trivial.

## Resources Required
- Malware or some other means to initially comprise the target system.
- Additional malware to impersonate a legitimate task.

## Consequences
- Scope: Access Control, Authentication; Impact: Gain Privileges

## Mitigations
- The only known mitigation to this attack is to avoid installing the malicious application on the device. However, to impersonate a running task the malicious application does need the GET_TASKS permission to be able to query the task list, and being suspicious of applications with that permission can help.

## Related Weaknesses (CWE)
- CWE-1021
