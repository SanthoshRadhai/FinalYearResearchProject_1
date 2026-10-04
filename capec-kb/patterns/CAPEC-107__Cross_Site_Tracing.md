# CAPEC-107: Cross Site Tracing

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/107.html  

## Description
Cross Site Tracing (XST) enables an adversary to steal the victim's session cookie and possibly other authentication credentials transmitted in the header of the HTTP request when the victim's browser communicates to a destination system's web server.

## Related Attack Patterns
- ChildOf: CAPEC-593

## Prerequisites
- HTTP TRACE is enabled on the web server
- The destination system is susceptible to XSS or an adversary can leverage some other weakness to bypass the same origin policy
- Scripting is enabled in the client's browser
- HTTP is used as the communication protocol between the server and the client

## Skills Required
- [Medium] Understanding of the HTTP protocol and an ability to craft a malicious script

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Administrators should disable support for HTTP TRACE at the destination's web server. Vendors should disable TRACE by default.
- Patch web browser against known security origin policy bypass exploits.

## Related Weaknesses (CWE)
- CWE-693
- CWE-648
