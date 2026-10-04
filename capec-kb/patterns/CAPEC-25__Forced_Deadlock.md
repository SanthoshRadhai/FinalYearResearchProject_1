# CAPEC-25: Forced Deadlock

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/25.html  

## Description
The adversary triggers and exploits a deadlock condition in the target software to cause a denial of service. A deadlock can occur when two or more competing actions are waiting for each other to finish, and thus neither ever does. Deadlock conditions can be difficult to detect.

## Prerequisites
- The target host has a deadlock condition. There are four conditions for a deadlock to occur, known as the Coffman conditions. [REF-101]
- The target host exposes an API to the user.

## Skills Required
- [Medium] This type of attack may be sophisticated and require knowledge about the system's resources and APIs.

## Consequences
- Scope: Availability; Impact: Resource Consumption

## Mitigations
- Use known algorithm to avoid deadlock condition (for instance non-blocking synchronization algorithms).
- For competing actions, use well-known libraries which implement synchronization.

## Related Weaknesses (CWE)
- CWE-412
- CWE-567
- CWE-662
- CWE-667
- CWE-833
- CWE-1322
