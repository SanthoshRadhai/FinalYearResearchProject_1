# CAPEC-2: Inducing Account Lockout

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/2.html  

## Description
An attacker leverages the security functionality of the system aimed at thwarting potential attacks to launch a denial of service attack against a legitimate system user. Many systems, for instance, implement a password throttling mechanism that locks an account after a certain number of incorrect log in attempts. An attacker can leverage this throttling mechanism to lock a legitimate user out of their own account. The weakness that is being leveraged by an attacker is the very security feature that has been put in place to counteract attacks.

## Related Attack Patterns
- ChildOf: CAPEC-212

## Prerequisites
- The system has a lockout mechanism.
- An attacker must be able to reproduce behavior that would result in an account being locked.

## Skills Required
- [Low] No programming skills or computer knowledge is needed. An attacker can easily use this attack pattern following the Execution Flow above.

## Resources Required
- Computer with access to the login portion of the target system

## Consequences
- Scope: Availability; Impact: Resource Consumption

## Mitigations
- Implement intelligent password throttling mechanisms such as those which take IP address into account, in addition to the login name.
- When implementing security features, consider how they can be misused and made to turn on themselves.

## Related Weaknesses (CWE)
- CWE-645
