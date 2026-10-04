# S1141: LunarWeb

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1141  
**Aliases:** LunarWeb  
**Platforms:** Windows  

## Description
[LunarWeb](https://attack.mitre.org/software/S1141) is a backdoor that has been used by [Turla](https://attack.mitre.org/groups/G0010) since at least 2020 including in a compromise of a European ministry of foreign affairs (MFA) together with [LunarLoader](https://attack.mitre.org/software/S1143) and [LunarMail](https://attack.mitre.org/software/S1142). [LunarWeb](https://attack.mitre.org/software/S1141) has only been observed deployed against servers and can use [Steganography](https://attack.mitre.org/techniques/T1001/002) to obfuscate command and control.(Citation: ESET Turla Lunar toolset May 2024)

## Techniques Used
- T1001.002: Steganography
- T1016: System Network Configuration Discovery
- T1027.013: Encrypted/Encoded File
- T1030: Data Transfer Size Limits
- T1033: System Owner/User Discovery
- T1047: Windows Management Instrumentation
- T1049: System Network Connections Discovery
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1069.001: Local Groups
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1090: Proxy
- T1104: Multi-Stage Channels
- T1132.001: Standard Encoding
- T1135: Network Share Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1497.003: Time Based Checks
- T1518: Software Discovery
- T1518.001: Security Software Discovery
- T1559: Inter-Process Communication
- T1560.001: Archive via Utility
- T1560.002: Archive via Library
- T1572: Protocol Tunneling
- T1573.001: Symmetric Cryptography
- T1573.002: Asymmetric Cryptography
- T1615: Group Policy Discovery
