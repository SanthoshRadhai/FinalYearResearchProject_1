# CAPEC-272: Protocol Manipulation

**Abstraction:** Meta  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/272.html  

## Description
An adversary subverts a communications protocol to perform an attack. This type of attack can allow an adversary to impersonate others, discover sensitive information, control the outcome of a session, or perform other attacks. This type of attack targets invalid assumptions that may be inherent in implementers of the protocol, incorrect implementations of the protocol, or vulnerabilities in the protocol itself.

## Prerequisites
- The protocol or implementations thereof must contain bugs that an adversary can exploit.

## Resources Required
- In some variants of this attack the adversary must be able to intercept communications using the protocol. This means they need to be able to receive the communications from one participant and prevent the other participant from receiving these communications.
