# CAPEC-590: IP Address Blocking

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/590.html  

## Description
An adversary performing this type of attack drops packets destined for a target IP address. The aim is to prevent access to the service hosted at the target IP address.

## Related Attack Patterns
- ChildOf: CAPEC-603

## Prerequisites
- This attack requires the ability to conduct deep packet inspection with an In-Path device that can drop the targeted traffic and/or connection.

## Consequences
- Scope: Availability; Impact: Other

## Mitigations
- Have a large pool of backup IPs built into the application and support proxy capability in the application.

## Related Weaknesses (CWE)
- CWE-300
