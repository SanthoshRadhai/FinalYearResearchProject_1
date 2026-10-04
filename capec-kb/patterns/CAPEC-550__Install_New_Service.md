# CAPEC-550: Install New Service

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/550.html  

## Description
When an operating system starts, it also starts programs called services or daemons. Adversaries may install a new service which will be executed at startup (on a Windows system, by modifying the registry). The service name may be disguised by using a name from a related operating system or benign software. Services are usually run with elevated privileges.

## Related Attack Patterns
- ChildOf: CAPEC-542

## Mitigations
- Limit privileges of user accounts so new service creation can only be performed by authorized administrators.

## Related Weaknesses (CWE)
- CWE-284
