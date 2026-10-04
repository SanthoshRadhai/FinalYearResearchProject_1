# CAPEC-151: Identity Spoofing

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/151.html  

## Description
Identity Spoofing refers to the action of assuming (i.e., taking on) the identity of some other entity (human or non-human) and then using that identity to accomplish a goal. An adversary may craft messages that appear to come from a different principle or use stolen / spoofed authentication credentials.

## Prerequisites
- The identity associated with the message or resource must be removable or modifiable in an undetectable way.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality, Integrity, Authentication, Access Control; Impact: Gain Privileges

## Mitigations
- Employ robust authentication processes (e.g., multi-factor authentication).

## Related Weaknesses (CWE)
- CWE-287
