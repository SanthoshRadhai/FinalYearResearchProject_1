# S1032: PyDCrypt

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1032  
**Aliases:** PyDCrypt  
**Platforms:** Windows  

## Description
[PyDCrypt](https://attack.mitre.org/software/S1032) is malware written in Python designed to deliver [DCSrv](https://attack.mitre.org/software/S1033). It has been used by [Moses Staff](https://attack.mitre.org/groups/G1009) since at least September 2021, with each sample tailored for its intended victim organization.(Citation: Checkpoint MosesStaff Nov 2021)

## Techniques Used
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1036.005: Match Legitimate Resource Name or Location
- T1047: Windows Management Instrumentation
- T1049: System Network Connections Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.006: Python
- T1070.004: File Deletion
- T1140: Deobfuscate/Decode Files or Information
- T1686: Disable or Modify System Firewall
