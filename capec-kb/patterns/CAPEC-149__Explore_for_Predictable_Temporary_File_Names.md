# CAPEC-149: Explore for Predictable Temporary File Names

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/149.html  

## Description
An attacker explores a target to identify the names and locations of predictable temporary files for the purpose of launching further attacks against the target. This involves analyzing naming conventions and storage locations of the temporary files created by a target application. If an attacker can predict the names of temporary files they can use this information to mount other attacks, such as information gathering and symlink attacks.

## Related Attack Patterns
- ChildOf: CAPEC-497
- CanPrecede: CAPEC-155

## Prerequisites
- The targeted application must create names for temporary files using a predictable procedure, e.g. using sequentially increasing numbers.
- The attacker must be able to see the names of the files the target is creating.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Related Weaknesses (CWE)
- CWE-377
