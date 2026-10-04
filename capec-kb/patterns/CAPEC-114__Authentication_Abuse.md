# CAPEC-114: Authentication Abuse

**Abstraction:** Meta  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/114.html  

## Description
An attacker obtains unauthorized access to an application, service or device either through knowledge of the inherent weaknesses of an authentication mechanism, or by exploiting a flaw in the authentication scheme's implementation. In such an attack an authentication mechanism is functioning but a carefully controlled sequence of events causes the mechanism to grant access to the attacker.

## Prerequisites
- An authentication mechanism or subsystem implementing some form of authentication such as passwords, digest authentication, security certificates, etc. which is flawed in some way.

## Resources Required
- A client application, command-line access to a binary, or scripting language capable of interacting with the authentication mechanism.

## Related Weaknesses (CWE)
- CWE-287
- CWE-1244
