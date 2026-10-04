# S0251: Zebrocy

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0251  
**Aliases:** Zebrocy, Zekapab  
**Platforms:** Windows  

## Description
[Zebrocy](https://attack.mitre.org/software/S0251) is a Trojan that has been used by [APT28](https://attack.mitre.org/groups/G0007) since at least November 2015. The malware comes in several programming language variants, including C++, Delphi, AutoIt, C#, VB.NET, and Golang. (Citation: Palo Alto Sofacy 06-2018)(Citation: Unit42 Cannon Nov 2018)(Citation: Unit42 Sofacy Dec 2018)(Citation: CISA Zebrocy Oct 2020)

## Techniques Used
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1027.002: Software Packing
- T1033: System Owner/User Discovery
- T1037.001: Logon Script (Windows)
- T1041: Exfiltration Over C2 Channel
- T1047: Windows Management Instrumentation
- T1049: System Network Connections Discovery
- T1053.005: Scheduled Task
- T1056.004: Credential API Hooking
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1071.003: Mail Protocols
- T1074.001: Local Data Staging
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1113: Screen Capture
- T1119: Automated Collection
- T1120: Peripheral Device Discovery
- T1124: System Time Discovery
- T1132.001: Standard Encoding
- T1135: Network Share Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1547.001: Registry Run Keys / Startup Folder
- T1555.003: Credentials from Web Browsers
- T1560: Archive Collected Data
- T1573.002: Asymmetric Cryptography
- T1680: Local Storage Discovery
