# T1617: Hooking


**ATT&CK ID:** T1617  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1617  

## Description
Adversaries may utilize hooking to hide the presence of artifacts associated with their behaviors to evade detection. Hooking can be used to modify return values or data structures of system APIs and function calls. This process typically involves using 3rd party root frameworks, such as Xposed or Magisk, with either a system exploit or pre-existing root access. By including custom modules for root frameworks, adversaries can hook system APIs and alter the return value and/or system data structures to alter functionality/visibility of various aspects of the system.

## Mitigations
- M1002: Attestation
- M1010: Deploy Compromised Device Detection Method

## Known Software Using This Technique
- S1208: FjordPhantom
- S1231: GodFather
- S0407: Monokle
