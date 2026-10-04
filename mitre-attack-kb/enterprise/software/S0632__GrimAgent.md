# S0632: GrimAgent

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0632  
**Aliases:** GrimAgent  
**Platforms:** Windows  

## Description
[GrimAgent](https://attack.mitre.org/software/S0632) is a backdoor that has been used before the deployment of [Ryuk](https://attack.mitre.org/software/S0446) ransomware since at least 2020; it is likely used by [FIN6](https://attack.mitre.org/groups/G0037) and [Wizard Spider](https://attack.mitre.org/groups/G0102).(Citation: Group IB GrimAgent July 2021)

## Techniques Used
- T1001.001: Junk Data
- T1005: Data from Local System
- T1016: System Network Configuration Discovery
- T1027: Obfuscated Files or Information
- T1027.001: Binary Padding
- T1033: System Owner/User Discovery
- T1041: Exfiltration Over C2 Channel
- T1053.005: Scheduled Task
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1070.009: Clear Persistence
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1480.002: Mutual Exclusion
- T1497.003: Time Based Checks
- T1547.001: Registry Run Keys / Startup Folder
- T1573.001: Symmetric Cryptography
- T1573.002: Asymmetric Cryptography
- T1614: System Location Discovery
- T1614.001: System Language Discovery
