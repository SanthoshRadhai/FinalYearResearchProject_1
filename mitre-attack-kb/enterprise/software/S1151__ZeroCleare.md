# S1151: ZeroCleare

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1151  
**Aliases:** ZeroCleare, ZEROCLEAR  
**Platforms:** Windows  

## Description
[ZeroCleare](https://attack.mitre.org/software/S1151) is a wiper malware that has been used in conjunction with the [RawDisk](https://attack.mitre.org/software/S0364) driver since at least 2019 by suspected Iran-nexus threat actors including activity targeting the energy and industrial sectors in the Middle East and political targets in Albania.(Citation: Microsoft Albanian Government Attacks September 2022)(Citation: CISA Iran Albanian Attacks September 2022)(Citation: Mandiant ROADSWEEP August 2022)(Citation: IBM ZeroCleare Wiper December 2019)

## Techniques Used
- T1059: Command and Scripting Interpreter
- T1059.001: PowerShell
- T1068: Exploitation for Privilege Escalation
- T1070.004: File Deletion
- T1106: Native API
- T1553.002: Code Signing
- T1561.002: Disk Structure Wipe
- T1680: Local Storage Discovery
