# CAPEC-115: Authentication Bypass

**Abstraction:** Meta  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/115.html  

## Description
An attacker gains access to application, service, or device with the privileges of an authorized or privileged user by evading or circumventing an authentication mechanism. The attacker is therefore able to access protected data without authentication ever having taken place.

## Prerequisites
- An authentication mechanism or subsystem implementing some form of authentication such as passwords, digest authentication, security certificates, etc.

## Resources Required
- A client application, such as a web browser, or a scripting language capable of interacting with the target.

## Related Weaknesses (CWE)
- CWE-287
