# S0441: PowerShower

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0441  
**Aliases:** PowerShower  
**Platforms:** Windows  

## Description
[PowerShower](https://attack.mitre.org/software/S0441) is a PowerShell backdoor used by [Inception](https://attack.mitre.org/groups/G0100) for initial reconnaissance and to download and execute second stage payloads.(Citation: Unit 42 Inception November 2018)(Citation: Kaspersky Cloud Atlas August 2019)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1033: System Owner/User Discovery
- T1041: Exfiltration Over C2 Channel
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.005: Visual Basic
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1112: Modify Registry
- T1132.001: Standard Encoding
- T1547.001: Registry Run Keys / Startup Folder
- T1560.001: Archive via Utility
- T1564.003: Hidden Window
