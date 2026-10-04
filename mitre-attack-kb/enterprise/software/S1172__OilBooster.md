# S1172: OilBooster

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1172  
**Aliases:** OilBooster  
**Platforms:** Windows  

## Description
[OilBooster](https://attack.mitre.org/software/S1172) is a downloader written in Microsoft Visual C/C++ that has been used by [OilRig](https://attack.mitre.org/groups/G0049) since at least 2022 including against target organizations in Israel to download and execute files and for exfiltration.(Citation: ESET OilRig Downloaders DEC 2023)

## Techniques Used
- T1008: Fallback Channels
- T1033: System Owner/User Discovery
- T1041: Exfiltration Over C2 Channel
- T1059.003: Windows Command Shell
- T1071.001: Web Protocols
- T1074.001: Local Data Staging
- T1082: System Information Discovery
- T1102.002: Bidirectional Communication
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1140: Deobfuscate/Decode Files or Information
- T1559: Inter-Process Communication
- T1564.003: Hidden Window
- T1567.002: Exfiltration to Cloud Storage
- T1573.002: Asymmetric Cryptography
