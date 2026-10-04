# S1182: MagicRAT

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1182  
**Aliases:** MagicRAT  
**Platforms:** Windows  

## Description
[MagicRAT](https://attack.mitre.org/software/S1182) is a remote access tool developed in C++ and exclusively used by the [Lazarus Group](https://attack.mitre.org/groups/G0032) threat actor in operations. [MagicRAT](https://attack.mitre.org/software/S1182) allows for arbitrary command execution on victim machines and provides basic remote access functionality.(Citation: Cisco MagicRAT 2022)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1027.013: Encrypted/Encoded File
- T1036.005: Match Legitimate Resource Name or Location
- T1036.008: Masquerade File Type
- T1041: Exfiltration Over C2 Channel
- T1053.005: Scheduled Task
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1105: Ingress Tool Transfer
- T1140: Deobfuscate/Decode Files or Information
- T1547.001: Registry Run Keys / Startup Folder
