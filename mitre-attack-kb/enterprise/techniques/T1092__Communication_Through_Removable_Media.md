# T1092: Communication Through Removable Media


**ATT&CK ID:** T1092  
**Domain:** Mitre Attack  
**Tactic(s):** Command And Control  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1092  

## Description
Adversaries can perform command and control between compromised hosts on potentially disconnected networks using removable media to transfer commands from system to system.(Citation: ESET Sednit USBStealer 2014) Both systems would need to be compromised, with the likelihood that an Internet-connected system was compromised first and the second through lateral movement by [Replication Through Removable Media](https://attack.mitre.org/techniques/T1091). Commands and files would be relayed from the disconnected system to the Internet-connected system to which the adversary has direct access.

## Mitigations
- M1028: Operating System Configuration
- M1042: Disable or Remove Feature or Program

## Known Threat Groups Using This Technique
- G0007: APT28

## Known Software Using This Technique
- S0023: CHOPSTICK
- S0136: USBStealer
