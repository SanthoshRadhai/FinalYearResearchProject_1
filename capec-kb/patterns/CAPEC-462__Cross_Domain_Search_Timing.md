# CAPEC-462: Cross-Domain Search Timing

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/462.html  

## Description
An attacker initiates cross domain HTTP / GET requests and times the server responses. The timing of these responses may leak important information on what is happening on the server. Browser's same origin policy prevents the attacker from directly reading the server responses (in the absence of any other weaknesses), but does not prevent the attacker from timing the responses to requests that the attacker issued cross domain.

## Related Attack Patterns
- ChildOf: CAPEC-54

## Prerequisites
- Ability to issue GET / POST requests cross domainJava Script is enabled in the victim's browserThe victim has an active session with the site from which the attacker would like to receive informationThe victim's site does not protect search functionality with cross site request forgery (CSRF) protection

## Skills Required
- [Low] Some knowledge of Java Script

## Resources Required
- Ability to issue GET / POST requests cross domain

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Design: The victim's site could protect all potentially sensitive functionality (e.g. search functions) with cross site request forgery (CSRF) protection and not perform any work on behalf of forged requests
- Design: The browser's security model could be fixed to not leak timing information for cross domain requests

## Related Weaknesses (CWE)
- CWE-385
- CWE-352
- CWE-208
