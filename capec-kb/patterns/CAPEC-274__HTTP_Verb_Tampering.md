# CAPEC-274: HTTP Verb Tampering

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/274.html  

## Description
An attacker modifies the HTTP Verb (e.g. GET, PUT, TRACE, etc.) in order to bypass access restrictions. Some web environments allow administrators to restrict access based on the HTTP Verb used with requests. However, attackers can often provide a different HTTP Verb, or even provide a random string as a verb in order to bypass these protections. This allows the attacker to access data that should otherwise be protected.

## Related Attack Patterns
- ChildOf: CAPEC-220

## Prerequisites
- The targeted system must attempt to filter access based on the HTTP verb used in requests.

## Resources Required
- The attacker requires a tool that allows them to manually control the HTTP verb used to send messages to the targeted server.

## Mitigations
- Design: Ensure that only legitimate HTTP verbs are allowed.
- Design: Do not use HTTP verbs as factors in access decisions.

## Related Weaknesses (CWE)
- CWE-302
- CWE-654
