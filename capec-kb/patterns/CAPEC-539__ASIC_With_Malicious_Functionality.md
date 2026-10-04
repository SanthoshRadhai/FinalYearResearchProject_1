# CAPEC-539: ASIC With Malicious Functionality

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/539.html  

## Description
An attacker with access to the development environment process of an application-specific integrated circuit (ASIC) for a victim system being developed or maintained after initial deployment can insert malicious functionality into the system for the purpose of disruption or further compromise.

## Related Attack Patterns
- ChildOf: CAPEC-444

## Prerequisites
- The attacker must have working knowledge of some if not all of the components involved in the target system as well as the infrastructure and development environment of the manufacturer.
- Advanced knowledge about the ASIC installed within the target system.

## Skills Required
- [High] Able to develop and manufacture malicious subroutines for an ASIC environment without degradation of existing functions and processes.
