# T0845: Program Upload


**ATT&CK ID:** T0845  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Collection  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0845  

## Description
Adversaries may attempt to upload a program from a PLC to gather information about an industrial process. Uploading a program may allow them to acquire and study the underlying logic. Methods of program upload include vendor software, which enables the user to upload and read a program running on a PLC. This software can be used to upload the target program to a workstation, jump box, or an interfacing device.

## Mitigations
- M0800: Authorization Enforcement
- M0801: Access Management
- M0802: Communication Authenticity
- M0804: Human User Authentication
- M0807: Network Allowlists
- M0813: Software Process and Device Authentication
- M0930: Network Segmentation
- M0937: Filter Network Traffic

## Known Software Using This Technique
- S1045: INCONTROLLER
- S1009: Triton
