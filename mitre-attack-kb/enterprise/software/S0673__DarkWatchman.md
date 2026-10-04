# S0673: DarkWatchman

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0673  
**Aliases:** DarkWatchman  
**Platforms:** Windows  

## Description
[DarkWatchman](https://attack.mitre.org/software/S0673) is a lightweight JavaScript-based remote access tool (RAT) that avoids file operations; it was first observed in November 2021.(Citation: Prevailion DarkWatchman 2021)

## Techniques Used
- T1005: Data from Local System
- T1010: Application Window Discovery
- T1012: Query Registry
- T1027.004: Compile After Delivery
- T1027.010: Command Obfuscation
- T1027.011: Fileless Storage
- T1027.015: Compression
- T1033: System Owner/User Discovery
- T1036: Masquerading
- T1047: Windows Management Instrumentation
- T1053.005: Scheduled Task
- T1056.001: Keylogging
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.007: JavaScript
- T1070: Indicator Removal
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1074.001: Local Data Staging
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1112: Modify Registry
- T1120: Peripheral Device Discovery
- T1124: System Time Discovery
- T1129: Shared Modules
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1217: Browser Information Discovery
- T1490: Inhibit System Recovery
- T1518.001: Security Software Discovery
- T1566.001: Spearphishing Attachment
- T1568.002: Domain Generation Algorithms
- T1573.002: Asymmetric Cryptography
- T1614: System Location Discovery
