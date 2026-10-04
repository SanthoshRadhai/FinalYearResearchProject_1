# S0030: Carbanak

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0030  
**Aliases:** Carbanak, Anunak  
**Platforms:** Windows  

## Description
[Carbanak](https://attack.mitre.org/software/S0030) is a full-featured, remote backdoor used by a group of the same name ([Carbanak](https://attack.mitre.org/groups/G0008)). It is intended for espionage, data exfiltration, and providing remote access to infected machines. (Citation: Kaspersky Carbanak) (Citation: FireEye CARBANAK June 2017)

## Techniques Used
- T1003: OS Credential Dumping
- T1012: Query Registry
- T1021.001: Remote Desktop Protocol
- T1027: Obfuscated Files or Information
- T1030: Data Transfer Size Limits
- T1055.002: Portable Executable Injection
- T1056.001: Keylogging
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1113: Screen Capture
- T1114.001: Local Email Collection
- T1132.001: Standard Encoding
- T1136.001: Local Account
- T1219: Remote Access Tools
- T1547.001: Registry Run Keys / Startup Folder
- T1573.001: Symmetric Cryptography
