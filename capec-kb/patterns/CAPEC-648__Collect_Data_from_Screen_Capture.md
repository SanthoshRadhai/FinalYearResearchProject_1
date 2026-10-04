# CAPEC-648: Collect Data from Screen Capture

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/648.html  

## Description
An adversary gathers sensitive information by exploiting the system's screen capture functionality. Through screenshots, the adversary aims to see what happens on the screen over the course of an operation. The adversary can leverage information gathered in order to carry out further attacks.

## Related Attack Patterns
- ChildOf: CAPEC-150

## Prerequisites
- The adversary must have obtained logical access to the system by some means (e.g., via obtained credentials or planting malware on the system).

## Skills Required
- [Low] Once the adversary has logical access (which can potentially require high knowledge and skill level), the adversary needs only to leverage the relevant command for screen capture.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Identify potentially malicious software that may have functionality to acquire screen captures, and audit and/or block it by using allowlist tools.
- While screen capture is a legitimate and practical function, certain situations and context may require the disabling of this feature.

## Related Weaknesses (CWE)
- CWE-267
