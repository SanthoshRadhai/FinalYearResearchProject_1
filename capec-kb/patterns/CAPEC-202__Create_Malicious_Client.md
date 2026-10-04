# CAPEC-202: Create Malicious Client

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/202.html  

## Description
An adversary creates a client application to interface with a target service where the client violates assumptions the service makes about clients. Services that have designated client applications (as opposed to services that use general client applications, such as IMAP or POP mail servers which can interact with any IMAP or POP client) may assume that the client will follow specific procedures.

## Related Attack Patterns
- ChildOf: CAPEC-22

## Prerequisites
- The targeted service must make assumptions about the behavior of the client application that interacts with it, which can be abused by an adversary.

## Resources Required
- The adversary must be able to reverse engineer a client of the targeted service. However, the adversary does not need to reverse engineer all client functionality - they only need to recreate enough of the functionality to access the desired server functionality.

## Related Weaknesses (CWE)
- CWE-602
