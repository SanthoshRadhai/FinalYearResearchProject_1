# CAPEC-593: Session Hijacking

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/593.html  

## Description
This type of attack involves an adversary that exploits weaknesses in an application's use of sessions in performing authentication. The adversary is able to steal or manipulate an active session and use it to gain unathorized access to the application.

## Related Attack Patterns
- ChildOf: CAPEC-21

## Prerequisites
- An application that leverages sessions to perform authentication.

## Skills Required
- [Low] Exploiting a poorly protected identity token is a well understood attack with many helpful resources available.

## Resources Required
- The adversary must have the ability to communicate with the application over the network.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Gain Privileges

## Mitigations
- Properly encrypt and sign identity tokens in transit, and use industry standard session key generation mechanisms that utilize high amount of entropy to generate the session key. Many standard web and application servers will perform this task on your behalf. Utilize a session timeout for all sessions. If the user does not explicitly logout, terminate their session after this period of inactivity. If the user logs back in then a new session key should be generated.

## Related Weaknesses (CWE)
- CWE-287
