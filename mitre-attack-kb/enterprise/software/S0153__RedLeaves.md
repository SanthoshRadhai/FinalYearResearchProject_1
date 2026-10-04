# S0153: RedLeaves

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0153  
**Aliases:** RedLeaves, BUGJUICE  
**Platforms:** Windows  

## Description
[RedLeaves](https://attack.mitre.org/software/S0153) is a malware family used by [menuPass](https://attack.mitre.org/groups/G0045). The code overlaps with [PlugX](https://attack.mitre.org/software/S0013) and may be based upon the open source tool Trochilus. (Citation: PWC Cloud Hopper Technical Annex April 2017) (Citation: FireEye APT10 April 2017)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1049: System Network Connections Discovery
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1113: Screen Capture
- T1547.001: Registry Run Keys / Startup Folder
- T1547.009: Shortcut Modification
- T1555.003: Credentials from Web Browsers
- T1571: Non-Standard Port
- T1573.001: Symmetric Cryptography
- T1574.001: DLL
