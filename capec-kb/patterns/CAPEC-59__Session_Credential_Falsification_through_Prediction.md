# CAPEC-59: Session Credential Falsification through Prediction

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/59.html  

## Description
This attack targets predictable session ID in order to gain privileges. The attacker can predict the session ID used during a transaction to perform spoofing and session hijacking.

## Related Attack Patterns
- ChildOf: CAPEC-196

## Prerequisites
- The target host uses session IDs to keep track of the users.
- Session IDs are used to control access to resources.
- The session IDs used by the target host are predictable. For example, the session IDs are generated using predictable information (e.g., time).

## Skills Required
- [Low] There are tools to brute force session ID. Those tools require a low level of knowledge.
- [Medium] Predicting Session ID may require more computation work which uses advanced analysis such as statistical analysis.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Use a strong source of randomness to generate a session ID.
- Use adequate length session IDs
- Do not use information available to the user in order to generate session ID (e.g., time).
- Ideas for creating random numbers are offered by Eastlake [RFC1750]
- Encrypt the session ID if you expose it to the user. For instance session ID can be stored in a cookie in encrypted format.

## Related Weaknesses (CWE)
- CWE-290
- CWE-330
- CWE-331
- CWE-346
- CWE-488
- CWE-539
- CWE-200
- CWE-6
- CWE-285
- CWE-384
- CWE-693
