# T1398: Boot or Logon Initialization Scripts


**ATT&CK ID:** T1398  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Persistence  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1398  

## Description
Adversaries may use scripts automatically executed at boot or logon initialization to establish persistence. Initialization scripts are part of the underlying operating system and are not accessible to the user unless the device has been rooted or jailbroken.

## Mitigations
- M1001: Security Updates
- M1002: Attestation
- M1003: Lock Bootloader
- M1004: System Partition Integrity

## Known Software Using This Technique
- S1095: AhRat
- S1079: BOULDSPY
- S1185: LightSpy
- S0285: OldBoot
