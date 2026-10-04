# S0126: ComRAT

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0126  
**Aliases:** ComRAT  
**Platforms:** Windows  

## Description
[ComRAT](https://attack.mitre.org/software/S0126) is a second stage implant suspected of being a descendant of [Agent.btz](https://attack.mitre.org/software/S0092) and used by [Turla](https://attack.mitre.org/groups/G0010). The first version of [ComRAT](https://attack.mitre.org/software/S0126) was identified in 2007, but the tool has undergone substantial development for many years since.(Citation: Symantec Waterbug)(Citation: NorthSec 2015 GData Uroburos Tools)(Citation: ESET ComRAT May 2020)

## Techniques Used
- T1012: Query Registry
- T1027: Obfuscated Files or Information
- T1027.009: Embedded Payloads
- T1027.010: Command Obfuscation
- T1027.011: Fileless Storage
- T1029: Scheduled Transfer
- T1036.004: Masquerade Task or Service
- T1053.005: Scheduled Task
- T1055.001: Dynamic-link Library Injection
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1071.001: Web Protocols
- T1071.003: Mail Protocols
- T1102.002: Bidirectional Communication
- T1106: Native API
- T1112: Modify Registry
- T1124: System Time Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1518: Software Discovery
- T1546.015: Component Object Model Hijacking
- T1564.005: Hidden File System
- T1573.002: Asymmetric Cryptography
