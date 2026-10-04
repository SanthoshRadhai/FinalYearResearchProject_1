# CAPEC-467: Cross Site Identification

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/467.html  

## Description
An attacker harvests identifying information about a victim via an active session that the victim's browser has with a social networking site. A victim may have the social networking site open in one tab or perhaps is simply using the "remember me" feature to keep their session with the social networking site active. An attacker induces a payload to execute in the victim's browser that transparently to the victim initiates a request to the social networking site (e.g., via available social network site APIs) to retrieve identifying information about a victim. While some of this information may be public, the attacker is able to harvest this information in context and may use it for further attacks on the user (e.g., spear phishing).

## Related Attack Patterns
- ChildOf: CAPEC-62

## Prerequisites
- The victim has an active session with the social networking site.

## Skills Required
- [High] An attacker should be able to create a payload and deliver it to the victim's browser.
- [Medium] An attacker needs to know how to interact with various social networking sites (e.g., via available APIs) to request information and how to send the harvested data back to the attacker.

## Mitigations
- Usage: Users should always explicitly log out from the social networking sites when done using them.
- Usage: Users should not open other tabs in the browser when using a social networking site.

## Related Weaknesses (CWE)
- CWE-352
- CWE-359
