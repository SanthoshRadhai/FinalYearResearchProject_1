# S0674: CharmPower

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0674  
**Aliases:** CharmPower  
**Platforms:** Windows  

## Description
[CharmPower](https://attack.mitre.org/software/S0674) is a PowerShell-based, modular backdoor that has been used by [Magic Hound](https://attack.mitre.org/groups/G0059) since at least 2022.(Citation: Check Point APT35 CharmPower January 2022)

## Techniques Used
- T1005: Data from Local System
- T1008: Fallback Channels
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1016.002: Wi-Fi Discovery
- T1041: Exfiltration Over C2 Channel
- T1047: Windows Management Instrumentation
- T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1102: Web Service
- T1102.001: Dead Drop Resolver
- T1105: Ingress Tool Transfer
- T1112: Modify Registry
- T1113: Screen Capture
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1518: Software Discovery
- T1573.001: Symmetric Cryptography
