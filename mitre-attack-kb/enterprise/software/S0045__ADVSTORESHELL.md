# S0045: ADVSTORESHELL

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0045  
**Aliases:** ADVSTORESHELL, AZZY, EVILTOSS, NETUI, Sedreco  
**Platforms:** Windows  

## Description
[ADVSTORESHELL](https://attack.mitre.org/software/S0045) is a spying backdoor that has been used by [APT28](https://attack.mitre.org/groups/G0007) from at least 2012 to 2016. It is generally used for long-term espionage and is deployed on targets deemed interesting after a reconnaissance phase. (Citation: Kaspersky Sofacy) (Citation: ESET Sednit Part 2)

## Techniques Used
- T1012: Query Registry
- T1027: Obfuscated Files or Information
- T1029: Scheduled Transfer
- T1041: Exfiltration Over C2 Channel
- T1056.001: Keylogging
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1074.001: Local Data Staging
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1106: Native API
- T1112: Modify Registry
- T1120: Peripheral Device Discovery
- T1132.001: Standard Encoding
- T1218.011: Rundll32
- T1546.015: Component Object Model Hijacking
- T1547.001: Registry Run Keys / Startup Folder
- T1560: Archive Collected Data
- T1560.003: Archive via Custom Method
- T1573.001: Symmetric Cryptography
- T1573.002: Asymmetric Cryptography
