# T1630: Indicator Removal on Host


**ATT&CK ID:** T1630  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** iOS, Android  
**Reference:** https://attack.mitre.org/techniques/T1630  

## Description
Adversaries may delete, alter, or hide generated artifacts on a device, including files, jailbreak status, or the malicious application itself. These actions may interfere with event collection, reporting, or other notifications used to detect intrusion activity. This may compromise the integrity of mobile security solutions by causing notable events or information to go unreported.

## Sub-techniques
- T1630.001: Uninstall Malicious Application
- T1630.002: File Deletion
- T1630.003: Disguise Root/Jailbreak Indicators

## Mitigations
- M1001: Security Updates
- M1002: Attestation
- M1011: User Guidance

## Known Software Using This Technique
- S1083: Chameleon
- S1231: GodFather
