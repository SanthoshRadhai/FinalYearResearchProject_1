# S1228: PUBLOAD

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1228  
**Aliases:** PUBLOAD  
**Platforms:** Windows  

## Description
[PUBLOAD](https://attack.mitre.org/software/S1228) is a stager malware that has been observed installing itself in existing directories such as `C:\Users\Public` or creating new directories to stage the malware and its components.(Citation: 2022 November_TrendMicro_Earth Preta_Toneshell_Pubload)  [PUBLOAD](https://attack.mitre.org/software/S1228) malware collects details of the victim host, establishes persistence, encrypts victim details using RC4 and communicates victim details back to C2.  [PUBLOAD](https://attack.mitre.org/software/S1228) malware has previously been leveraged by China-affiliated actors identified as [Mustang Panda](https://attack.mitre.org/groups/G0129).   [PUBLOAD](https://attack.mitre.org/software/S1228) is also known as “NoFive” and some public reporting identifies the loader component as [CLAIMLOADER](https://attack.mitre.org/software/S1236).(Citation: 2025_IBM_PUBLOAD_TONESHELL_HIUPAN_CLAIMLOADER_MUSTANG PANDA)

## Techniques Used
- T1001.003: Protocol or Service Impersonation
- T1007: System Service Discovery
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1016.001: Internet Connection Discovery
- T1016.002: Wi-Fi Discovery
- T1027: Obfuscated Files or Information
- T1027.015: Compression
- T1033: System Owner/User Discovery
- T1036.005: Match Legitimate Resource Name or Location
- T1047: Windows Management Instrumentation
- T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol
- T1049: System Network Connections Discovery
- T1053.005: Scheduled Task
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1071.001: Web Protocols
- T1071.002: File Transfer Protocols
- T1082: System Information Discovery
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1124: System Time Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1205: Traffic Signaling
- T1480.001: Environmental Keying
- T1518: Software Discovery
- T1518.001: Security Software Discovery
- T1547.001: Registry Run Keys / Startup Folder
- T1553.002: Code Signing
- T1560.001: Archive via Utility
- T1573.001: Symmetric Cryptography
- T1574.001: DLL
- T1614.001: System Language Discovery
- T1622: Debugger Evasion
- T1680: Local Storage Discovery
