# T0802: Automated Collection


**ATT&CK ID:** T0802  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Collection  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0802  

## Description
Adversaries may automate collection of industrial environment information using tools or scripts. This automated collection may leverage native control protocols and tools available in the control systems environment. For example, the OPC protocol may be used to enumerate and gather information. Access to a system or interface with these native protocols may allow collection and enumeration of other attached, communicating servers and devices.

## Mitigations
- M0807: Network Allowlists
- M0930: Network Segmentation

## Known Software Using This Technique
- S0093: Backdoor.Oldrea
- S0604: Industroyer
- S1072: Industroyer2
