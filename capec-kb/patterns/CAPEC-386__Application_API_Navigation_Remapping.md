# CAPEC-386: Application API Navigation Remapping

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/386.html  

## Description
An attacker manipulates either egress or ingress data from a client within an application framework in order to change the destination and/or content of links/buttons displayed to a user within API messages. Performing this attack allows the attacker to manipulate content in such a way as to produce messages or content that looks authentic but contains links/buttons that point to an attacker controlled destination. Some applications make navigation remapping more difficult to detect because the actual HREF values of images, profile elements, and links/buttons are masked. One example would be to place an image in a user's photo gallery that when clicked upon redirected the user to an off-site location. Also, traditional web vulnerabilities (such as CSRF) can be constructed with remapped buttons or links. In some cases navigation remapping can be used for Phishing attacks or even means to artificially boost the page view, user site reputation, or click-fraud.

## Related Attack Patterns
- ChildOf: CAPEC-94

## Prerequisites
- Targeted software is utilizing application framework APIs

## Resources Required
- A software program that allows the use of adversary-in-the-middle (CAPEC-94) communications between the client and server, such as a man-in-the-middle proxy.

## Related Weaknesses (CWE)
- CWE-471
- CWE-345
- CWE-346
- CWE-602
- CWE-311
