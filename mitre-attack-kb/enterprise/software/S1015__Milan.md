# S1015: Milan

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1015  
**Aliases:** Milan, James  
**Platforms:** Windows  

## Description
[Milan](https://attack.mitre.org/software/S1015) is a backdoor implant based on [DanBot](https://attack.mitre.org/software/S1014) that was written in Visual C++ and .NET. [Milan](https://attack.mitre.org/software/S1015) has been used by [HEXANE](https://attack.mitre.org/groups/G1001) since at least June 2020.(Citation: ClearSky Siamesekitten August 2021)(Citation: Kaspersky Lyceum October 2021)

## Techniques Used
- T1005: Data from Local System
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1036: Masquerading
- T1036.007: Double File Extension
- T1053.005: Scheduled Task
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1071.004: DNS
- T1074.001: Local Data Staging
- T1082: System Information Discovery
- T1087.001: Local Account
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1559.001: Component Object Model
- T1568.002: Domain Generation Algorithms
- T1572: Protocol Tunneling
