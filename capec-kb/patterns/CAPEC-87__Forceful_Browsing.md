# CAPEC-87: Forceful Browsing

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/87.html  

## Description
An attacker employs forceful browsing (direct URL entry) to access portions of a website that are otherwise unreachable. Usually, a front controller or similar design pattern is employed to protect access to portions of a web application. Forceful browsing enables an attacker to access information, perform privileged operations and otherwise reach sections of the web application that have been improperly protected.

## Related Attack Patterns
- ChildOf: CAPEC-115

## Prerequisites
- The forcibly browseable pages or accessible resources must be discoverable and improperly protected.

## Skills Required
- [Low] Forcibly browseable pages can be discovered by using a number of automated tools. Doing the same manually is tedious but by no means difficult.

## Resources Required
- None: No specialized resources are required to execute this type of attack. A directory listing is helpful, but not a requirement.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism

## Mitigations
- Authenticate request to every resource. In addition, every page or resource must ensure that the request it is handling has been made in an authorized context.
- Forceful browsing can also be made difficult to a large extent by not hard-coding names of application pages or resources. This way, the attacker cannot figure out, from the application alone, the resources available from the present context.

## Related Weaknesses (CWE)
- CWE-425
- CWE-285
- CWE-693
