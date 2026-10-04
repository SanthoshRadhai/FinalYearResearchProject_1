# CAPEC-153: Input Data Manipulation

**Abstraction:** Meta  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/153.html  

## Description
An attacker exploits a weakness in input validation by controlling the format, structure, and composition of data to an input-processing interface. By supplying input of a non-standard or unexpected form an attacker can adversely impact the security of the target.

## Prerequisites
- The target must accept user data for processing and the manner in which this data is processed must depend on some aspect of the format or flags that the attacker can control.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Related Weaknesses (CWE)
- CWE-20
