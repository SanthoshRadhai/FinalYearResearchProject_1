# CAPEC-166: Force the System to Reset Values

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/166.html  

## Description
An attacker forces the target into a previous state in order to leverage potential weaknesses in the target dependent upon a prior configuration or state-dependent factors. Even in cases where an attacker may not be able to directly control the configuration of the targeted application, they may be able to reset the configuration to a prior state since many applications implement reset functions.

## Related Attack Patterns
- ChildOf: CAPEC-161

## Prerequisites
- The targeted application must have a reset function that returns the configuration of the application to an earlier state.
- The reset functionality must be inadequately protected against use.

## Resources Required
- None: No specialized resources are required to execute this type of attack. In some cases, the attacker may need special client applications in order to execute the reset functionality.

## Related Weaknesses (CWE)
- CWE-306
- CWE-1221
- CWE-1232
