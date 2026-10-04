# CAPEC-497: File Discovery

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very Low  
**Reference:** https://capec.mitre.org/data/definitions/497.html  

## Description
An adversary engages in probing and exploration activities to determine if common key files exists. Such files often contain configuration and security parameters of the targeted application, system or network. Using this knowledge may often pave the way for more damaging attacks.

## Related Attack Patterns
- ChildOf: CAPEC-169

## Prerequisites
- The adversary must know the location of these common key files.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Leverage file protection mechanisms to render these files accessible only to authorized parties.

## Related Weaknesses (CWE)
- CWE-200
