# CAPEC-104: Cross Zone Scripting

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/104.html  

## Description
An attacker is able to cause a victim to load content into their web-browser that bypasses security zone controls and gain access to increased privileges to execute scripting code or other web objects such as unsigned ActiveX controls or applets. This is a privilege elevation attack targeted at zone-based web-browser security.

## Related Attack Patterns
- ChildOf: CAPEC-233

## Prerequisites
- The target must be using a zone-aware browser.

## Skills Required
- [Medium] Ability to craft malicious scripts or find them elsewhere and ability to identify functionality that is running web controls in the local zone and to find an injection vector into that functionality

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- Disable script execution.
- Ensure that sufficient input validation is performed for any potentially untrusted data before it is used in any privileged context or zone
- Limit the flow of untrusted data into the privileged areas of the system that run in the higher trust zone
- Limit the sites that are being added to the local machine zone and restrict the privileges of the code running in that zone to the bare minimum
- Ensure proper HTML output encoding before writing user supplied data to the page

## Related Weaknesses (CWE)
- CWE-250
- CWE-638
- CWE-285
- CWE-116
- CWE-20
