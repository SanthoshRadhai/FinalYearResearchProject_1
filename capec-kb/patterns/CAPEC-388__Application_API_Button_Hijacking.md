# CAPEC-388: Application API Button Hijacking

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/388.html  

## Description
An attacker manipulates either egress or ingress data from a client within an application framework in order to change the destination and/or content of buttons displayed to a user within API messages. Performing this attack allows the attacker to manipulate content in such a way as to produce messages or content that looks authentic but contains buttons that point to an attacker controlled destination.

## Related Attack Patterns
- ChildOf: CAPEC-386

## Prerequisites
- Targeted software is utilizing application framework APIs

## Resources Required
- A software program that allows the use of adversary-in-the-middle (CAPEC-94) communications between the client and server, such as a adversary-in-the-middle (CAPEC-94) proxy.

## Related Weaknesses (CWE)
- CWE-471
- CWE-345
- CWE-346
- CWE-602
- CWE-311
