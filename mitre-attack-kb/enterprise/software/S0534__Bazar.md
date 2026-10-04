# S0534: Bazar

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0534  
**Aliases:** Bazar, KEGTAP, Team9, Bazaloader  
**Platforms:** Windows  

## Description
[Bazar](https://attack.mitre.org/software/S0534) is a downloader and backdoor that has been used since at least April 2020, with infections primarily against professional services, healthcare, manufacturing, IT, logistics and travel companies across the US and Europe. [Bazar](https://attack.mitre.org/software/S0534) reportedly has ties to [TrickBot](https://attack.mitre.org/software/S0266) campaigns and can be used to deploy additional malware, including ransomware, and to steal sensitive data.(Citation: Cybereason Bazar July 2020)

## Techniques Used
- T1005: Data from Local System
- T1008: Fallback Channels
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1018: Remote System Discovery
- T1027.002: Software Packing
- T1027.007: Dynamic API Resolution
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1036.004: Masquerade Task or Service
- T1036.005: Match Legitimate Resource Name or Location
- T1036.007: Double File Extension
- T1047: Windows Management Instrumentation
- T1053.005: Scheduled Task
- T1055: Process Injection
- T1055.012: Process Hollowing
- T1055.013: Process Doppelgänging
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1070.009: Clear Persistence
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087.001: Local Account
- T1087.002: Domain Account
- T1102: Web Service
- T1104: Multi-Stage Channels
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1124: System Time Discovery
- T1135: Network Share Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1197: BITS Jobs
- T1204.001: Malicious Link
- T1482: Domain Trust Discovery
- T1497: Virtualization/Sandbox Evasion
- T1497.003: Time Based Checks
- T1518: Software Discovery
- T1518.001: Security Software Discovery
- T1547.001: Registry Run Keys / Startup Folder
- T1547.004: Winlogon Helper DLL
- T1547.009: Shortcut Modification
- T1553.002: Code Signing
- T1566.002: Spearphishing Link
- T1568.002: Domain Generation Algorithms
- T1573.001: Symmetric Cryptography
- T1573.002: Asymmetric Cryptography
- T1614.001: System Language Discovery
- T1685: Disable or Modify Tools
