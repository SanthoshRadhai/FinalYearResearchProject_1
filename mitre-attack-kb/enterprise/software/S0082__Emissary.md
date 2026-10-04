# S0082: Emissary

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0082  
**Aliases:** Emissary  
**Platforms:** Windows  

## Description
[Emissary](https://attack.mitre.org/software/S0082) is a Trojan that has been used by [Lotus Blossom](https://attack.mitre.org/groups/G0030). It shares code with [Elise](https://attack.mitre.org/software/S0081), with both Trojans being part of a malware group referred to as LStudio.(Citation: Lotus Blossom Dec 2015)

## Techniques Used
- T1007: System Service Discovery
- T1016: System Network Configuration Discovery
- T1027.001: Binary Padding
- T1027.013: Encrypted/Encoded File
- T1055.001: Dynamic-link Library Injection
- T1059.003: Windows Command Shell
- T1069.001: Local Groups
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1105: Ingress Tool Transfer
- T1218.011: Rundll32
- T1543.003: Windows Service
- T1547.001: Registry Run Keys / Startup Folder
- T1573.001: Symmetric Cryptography
- T1615: Group Policy Discovery
