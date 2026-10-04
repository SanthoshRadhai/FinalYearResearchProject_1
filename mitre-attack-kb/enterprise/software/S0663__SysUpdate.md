# S0663: SysUpdate

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0663  
**Aliases:** SysUpdate, HyperSSL, Soldier, FOCUSFJORD  
**Platforms:** Windows, Linux  

## Description
[SysUpdate](https://attack.mitre.org/software/S0663) is a backdoor written in C++ that has been used by [Threat Group-3390](https://attack.mitre.org/groups/G0027) since at least 2020.(Citation: Trend Micro Iron Tiger April 2021)

## Techniques Used
- T1005: Data from Local System
- T1007: System Service Discovery
- T1016: System Network Configuration Discovery
- T1016.001: Internet Connection Discovery
- T1027.002: Software Packing
- T1027.011: Fileless Storage
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1036.004: Masquerade Task or Service
- T1041: Exfiltration Over C2 Channel
- T1047: Windows Management Instrumentation
- T1057: Process Discovery
- T1070.004: File Deletion
- T1071.004: DNS
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1112: Modify Registry
- T1113: Screen Capture
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1543.002: Systemd Service
- T1543.003: Windows Service
- T1547.001: Registry Run Keys / Startup Folder
- T1553.002: Code Signing
- T1564.001: Hidden Files and Directories
- T1569.002: Service Execution
- T1573.001: Symmetric Cryptography
- T1574.001: DLL
- T1680: Local Storage Discovery
