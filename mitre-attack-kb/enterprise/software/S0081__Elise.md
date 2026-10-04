# S0081: Elise

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0081  
**Aliases:** Elise, BKDR_ESILE, Page  
**Platforms:** Windows  

## Description
[Elise](https://attack.mitre.org/software/S0081) is a custom backdoor Trojan that appears to be used exclusively by [Lotus Blossom](https://attack.mitre.org/groups/G0030). It is part of a larger group of tools referred to as LStudio, ST Group, and APT0LSTU.(Citation: Lotus Blossom Jun 2015)(Citation: Accenture Dragonfish Jan 2018)

## Techniques Used
- T1007: System Service Discovery
- T1016: System Network Configuration Discovery
- T1027.013: Encrypted/Encoded File
- T1036.005: Match Legitimate Resource Name or Location
- T1055.001: Dynamic-link Library Injection
- T1057: Process Discovery
- T1070.004: File Deletion
- T1070.006: Timestomp
- T1071.001: Web Protocols
- T1074.001: Local Data Staging
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087.001: Local Account
- T1105: Ingress Tool Transfer
- T1132.001: Standard Encoding
- T1218.011: Rundll32
- T1543.003: Windows Service
- T1547.001: Registry Run Keys / Startup Folder
- T1573.001: Symmetric Cryptography
