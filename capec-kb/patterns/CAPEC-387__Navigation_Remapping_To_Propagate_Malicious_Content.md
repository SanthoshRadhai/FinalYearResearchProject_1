# CAPEC-387: Navigation Remapping To Propagate Malicious Content

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/387.html  

## Description
An adversary manipulates either egress or ingress data from a client within an application framework in order to change the content of messages and thereby circumvent the expected application logic.

## Related Attack Patterns
- ChildOf: CAPEC-386

## Prerequisites
- Targeted software is utilizing application framework APIs

## Resources Required
- A software program that allows the use of adversary-in-the-middle communications between the client and server, such as a man-in-the-middle proxy.

## Related Weaknesses (CWE)
- CWE-471
- CWE-345
- CWE-346
- CWE-602
- CWE-311
