# CAPEC-176: Configuration/Environment Manipulation

**Abstraction:** Meta  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/176.html  

## Description
An attacker manipulates files or settings external to a target application which affect the behavior of that application. For example, many applications use external configuration files and libraries - modification of these entities or otherwise affecting the application's ability to use them would constitute a configuration/environment manipulation attack.

## Prerequisites
- The target application must consult external files or configuration controls to control its execution. All but the very simplest applications meet this requirement.

## Resources Required
- The attacker must have the access necessary to affect the files or other environment items the targeted application uses for its operations.

## Related Weaknesses (CWE)
- CWE-15
- CWE-1233
- CWE-1234
- CWE-1304
- CWE-1328
