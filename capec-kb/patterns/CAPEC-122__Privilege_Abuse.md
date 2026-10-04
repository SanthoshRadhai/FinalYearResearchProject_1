# CAPEC-122: Privilege Abuse

**Abstraction:** Meta  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/122.html  

## Description
An adversary is able to exploit features of the target that should be reserved for privileged users or administrators but are exposed to use by lower or non-privileged accounts. Access to sensitive information and functionality must be controlled to ensure that only authorized users are able to access these resources.

## Related Attack Patterns
- CanPrecede: CAPEC-664

## Prerequisites
- The target must have misconfigured their access control mechanisms such that sensitive information, which should only be accessible to more trusted users, remains accessible to less trusted users.
- The adversary must have access to the target, albeit with an account that is less privileged than would be appropriate for the targeted resources.

## Skills Required
- [Low] Adversary can leverage privileged features they already have access to without additional effort or skill. Adversary is only required to have access to an account with improper priveleges.

## Resources Required
- None: No specialized resources are required to execute this type of attack. The ability to access the target is required.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Authorization; Impact: Gain Privileges
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism

## Mitigations
- Configure account privileges such privileged/administrator functionality is not exposed to non-privileged/lower accounts.

## Related Weaknesses (CWE)
- CWE-269
- CWE-732
- CWE-1317
