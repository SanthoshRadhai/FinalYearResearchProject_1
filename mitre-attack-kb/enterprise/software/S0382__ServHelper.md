# S0382: ServHelper

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0382  
**Aliases:** ServHelper  
**Platforms:** Windows  

## Description
[ServHelper](https://attack.mitre.org/software/S0382) is a backdoor first observed in late 2018. The backdoor is written in Delphi and is typically delivered as a DLL file.(Citation: Proofpoint TA505 Jan 2019)

## Techniques Used
- T1021.001: Remote Desktop Protocol
- T1033: System Owner/User Discovery
- T1036.010: Masquerade Account Name
- T1053.005: Scheduled Task
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1098.007: Additional Local or Domain Groups
- T1105: Ingress Tool Transfer
- T1136.001: Local Account
- T1218.011: Rundll32
- T1547.001: Registry Run Keys / Startup Folder
- T1573.002: Asymmetric Cryptography
