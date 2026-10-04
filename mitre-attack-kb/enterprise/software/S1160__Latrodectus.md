# S1160: Latrodectus

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1160  
**Aliases:** Latrodectus, IceNova, Unidentified 111  
**Platforms:** Windows  

## Description
[Latrodectus](https://attack.mitre.org/software/S1160) is a Windows malware downloader that has been used since at least 2023 to download and execute additional payloads and modules. [Latrodectus](https://attack.mitre.org/software/S1160) has most often been distributed through email campaigns, primarily by [TA577](https://attack.mitre.org/groups/G1037) and [TA578](https://attack.mitre.org/groups/G1038), and has infrastructure overlaps with historic [IcedID](https://attack.mitre.org/software/S0483) operations.(Citation: Latrodectus APR 2024)(Citation: Bleeping Computer Latrodectus April 2024)(Citation: Bitsight Latrodectus June 2024)

## Techniques Used
- T1005: Data from Local System
- T1016: System Network Configuration Discovery
- T1021.005: VNC
- T1027.001: Binary Padding
- T1027.002: Software Packing
- T1027.007: Dynamic API Resolution
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1047: Windows Management Instrumentation
- T1053.005: Scheduled Task
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1059.007: JavaScript
- T1069.002: Domain Groups
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087.002: Domain Account
- T1102: Web Service
- T1104: Multi-Stage Channels
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1132.001: Standard Encoding
- T1135: Network Share Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1204.001: Malicious Link
- T1204.002: Malicious File
- T1218.007: Msiexec
- T1218.011: Rundll32
- T1482: Domain Trust Discovery
- T1497.001: System Checks
- T1518.001: Security Software Discovery
- T1529: System Shutdown/Reboot
- T1547.001: Registry Run Keys / Startup Folder
- T1559.001: Component Object Model
- T1564.004: NTFS File Attributes
- T1566.001: Spearphishing Attachment
- T1566.002: Spearphishing Link
- T1573.001: Symmetric Cryptography
- T1622: Debugger Evasion
