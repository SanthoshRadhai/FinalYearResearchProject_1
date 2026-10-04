# S0476: Valak

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0476  
**Aliases:** Valak  
**Platforms:** Windows  

## Description
[Valak](https://attack.mitre.org/software/S0476) is a multi-stage modular malware that can function as a standalone information stealer or downloader, first observed in 2019 targeting enterprises in the US and Germany.(Citation: Cybereason Valak May 2020)(Citation: Unit 42 Valak July 2020)

## Techniques Used
- T1008: Fallback Channels
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1027: Obfuscated Files or Information
- T1027.002: Software Packing
- T1027.011: Fileless Storage
- T1033: System Owner/User Discovery
- T1041: Exfiltration Over C2 Channel
- T1047: Windows Management Instrumentation
- T1053.005: Scheduled Task
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.007: JavaScript
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1087.001: Local Account
- T1087.002: Domain Account
- T1104: Multi-Stage Channels
- T1105: Ingress Tool Transfer
- T1112: Modify Registry
- T1113: Screen Capture
- T1114.002: Remote Email Collection
- T1119: Automated Collection
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1204.002: Malicious File
- T1218.010: Regsvr32
- T1518.001: Security Software Discovery
- T1552.002: Credentials in Registry
- T1555.004: Windows Credential Manager
- T1559.002: Dynamic Data Exchange
- T1564.004: NTFS File Attributes
- T1566.001: Spearphishing Attachment
- T1566.002: Spearphishing Link
