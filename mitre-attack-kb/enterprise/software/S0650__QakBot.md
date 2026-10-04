# S0650: QakBot

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0650  
**Aliases:** QakBot, Pinkslipbot, QuackBot, QBot  
**Platforms:** Windows  

## Description
[QakBot](https://attack.mitre.org/software/S0650) is a modular banking trojan that has been used primarily by financially-motivated actors since at least 2007. [QakBot](https://attack.mitre.org/software/S0650) is continuously maintained and developed and has evolved from an information stealer into a delivery agent for ransomware, most notably [ProLock](https://attack.mitre.org/software/S0654) and [Egregor](https://attack.mitre.org/software/S0554).(Citation: Trend Micro Qakbot December 2020)(Citation: Red Canary Qbot)(Citation: Kaspersky QakBot September 2021)(Citation: ATT QakBot April 2021)

## Techniques Used
- T1005: Data from Local System
- T1010: Application Window Discovery
- T1016: System Network Configuration Discovery
- T1016.001: Internet Connection Discovery
- T1018: Remote System Discovery
- T1027: Obfuscated Files or Information
- T1027.001: Binary Padding
- T1027.002: Software Packing
- T1027.005: Indicator Removal from Tools
- T1027.006: HTML Smuggling
- T1027.010: Command Obfuscation
- T1027.011: Fileless Storage
- T1033: System Owner/User Discovery
- T1036.008: Masquerade File Type
- T1041: Exfiltration Over C2 Channel
- T1047: Windows Management Instrumentation
- T1049: System Network Connections Discovery
- T1053.005: Scheduled Task
- T1055: Process Injection
- T1055.012: Process Hollowing
- T1056.001: Keylogging
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1059.007: JavaScript
- T1069.001: Local Groups
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1074.001: Local Data Staging
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1090.002: External Proxy
- T1091: Replication Through Removable Media
- T1095: Non-Application Layer Protocol
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1110: Brute Force
- T1112: Modify Registry
- T1114.001: Local Email Collection
- T1120: Peripheral Device Discovery
- T1124: System Time Discovery
- T1132.001: Standard Encoding
- T1135: Network Share Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1185: Browser Session Hijacking
- T1204.001: Malicious Link
- T1204.002: Malicious File
- T1210: Exploitation of Remote Services
- T1218.007: Msiexec
- T1218.010: Regsvr32
- T1218.011: Rundll32
- T1482: Domain Trust Discovery
- T1497.001: System Checks
- T1497.003: Time Based Checks
- T1518: Software Discovery
- T1518.001: Security Software Discovery
- T1539: Steal Web Session Cookie
- T1543.003: Windows Service
- T1547.001: Registry Run Keys / Startup Folder
- T1553.002: Code Signing
- T1553.005: Mark-of-the-Web Bypass
- T1555.003: Credentials from Web Browsers
- T1564.001: Hidden Files and Directories
- T1566.001: Spearphishing Attachment
- T1566.002: Spearphishing Link
- T1568.002: Domain Generation Algorithms
- T1572: Protocol Tunneling
- T1573.001: Symmetric Cryptography
- T1574.001: DLL
- T1685: Disable or Modify Tools
