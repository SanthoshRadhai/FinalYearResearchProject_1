# S0428: PoetRAT

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0428  
**Aliases:** PoetRAT  
**Platforms:** Windows  

## Description
[PoetRAT](https://attack.mitre.org/software/S0428) is a remote access trojan (RAT) that was first identified in April 2020. [PoetRAT](https://attack.mitre.org/software/S0428) has been used in multiple campaigns against the private and public sectors in Azerbaijan, including ICS and SCADA systems in the energy sector. The STIBNITE activity group has been observed using the malware. [PoetRAT](https://attack.mitre.org/software/S0428) derived its name from references in the code to poet William Shakespeare. (Citation: Talos PoetRAT April 2020)(Citation: Talos PoetRAT October 2020)(Citation: Dragos Threat Report 2020)

## Techniques Used
- T1003.001: LSASS Memory
- T1018: Remote System Discovery
- T1027: Obfuscated Files or Information
- T1027.010: Command Obfuscation
- T1033: System Owner/User Discovery
- T1041: Exfiltration Over C2 Channel
- T1048: Exfiltration Over Alternative Protocol
- T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol
- T1056.001: Keylogging
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1059.006: Python
- T1059.011: Lua
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1071.002: File Transfer Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1112: Modify Registry
- T1113: Screen Capture
- T1119: Automated Collection
- T1125: Video Capture
- T1140: Deobfuscate/Decode Files or Information
- T1204.002: Malicious File
- T1497.001: System Checks
- T1547.001: Registry Run Keys / Startup Folder
- T1555.003: Credentials from Web Browsers
- T1559.002: Dynamic Data Exchange
- T1560.001: Archive via Utility
- T1564.001: Hidden Files and Directories
- T1566.001: Spearphishing Attachment
- T1571: Non-Standard Port
- T1573.002: Asymmetric Cryptography
