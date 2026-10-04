# CAPEC-464: Evercookie

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/464.html  

## Description
An attacker creates a very persistent cookie that stays present even after the user thinks it has been removed. The cookie is stored on the victim's machine in over ten places. When the victim clears the cookie cache via traditional means inside the browser, that operation removes the cookie from certain places but not others. The malicious code then replicates the cookie from all of the places where it was not deleted to all of the possible storage locations once again. So the victim again has the cookie in all of the original storage locations. In other words, failure to delete the cookie in even one location will result in the cookie's resurrection everywhere. The evercookie will also persist across different browsers because certain stores (e.g., Local Shared Objects) are shared between different browsers.

## Related Attack Patterns
- ChildOf: CAPEC-554

## Prerequisites
- The victim's browser is not configured to reject all cookiesThe victim visits a website that serves the attackers' evercookie

## Resources Required
- Evercookie source code

## Mitigations
- Design: Browser's design needs to be changed to limit where cookies can be stored on the client side and provide an option to clear these cookies in all places, as well as another option to stop these cookies from being written in the first place.
- Design: Safari browser's private browsing mode is currently effective against evercookies.

## Related Weaknesses (CWE)
- CWE-359
