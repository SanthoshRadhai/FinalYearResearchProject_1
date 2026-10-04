# S0356: KONNI

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0356  
**Aliases:** KONNI  
**Platforms:** Windows  

## Description
[KONNI](https://attack.mitre.org/software/S0356) is a remote access tool that security researchers assess has been used by North Korean cyber actors since at least 2014. [KONNI](https://attack.mitre.org/software/S0356) has significant code overlap with the [NOKKI](https://attack.mitre.org/software/S0353) malware family, and has been linked to several suspected North Korean campaigns targeting political organizations in Russia, East Asia, Europe and the Middle East; there is some evidence potentially linking [KONNI](https://attack.mitre.org/software/S0356) to [APT37](https://attack.mitre.org/groups/G0067).(Citation: Talos Konni May 2017)(Citation: Unit 42 NOKKI Sept 2018)(Citation: Unit 42 Nokki Oct 2018)(Citation: Medium KONNI Jan 2020)(Citation: Malwarebytes Konni Aug 2021)

## Techniques Used
- T1005: Data from Local System
- T1016: System Network Configuration Discovery
- T1027.002: Software Packing
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1036.004: Masquerade Task or Service
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol
- T1049: System Network Connections Discovery
- T1056.001: Keylogging
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.007: JavaScript
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1112: Modify Registry
- T1113: Screen Capture
- T1115: Clipboard Data
- T1132.001: Standard Encoding
- T1134.002: Create Process with Token
- T1134.004: Parent PID Spoofing
- T1140: Deobfuscate/Decode Files or Information
- T1204.002: Malicious File
- T1218.011: Rundll32
- T1543.003: Windows Service
- T1546.015: Component Object Model Hijacking
- T1547.001: Registry Run Keys / Startup Folder
- T1547.009: Shortcut Modification
- T1548.002: Bypass User Account Control
- T1555.003: Credentials from Web Browsers
- T1560: Archive Collected Data
- T1566.001: Spearphishing Attachment
- T1573.001: Symmetric Cryptography
- T1680: Local Storage Discovery
