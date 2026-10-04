# S0615: SombRAT

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0615  
**Aliases:** SombRAT  
**Platforms:** Windows  

## Description
[SombRAT](https://attack.mitre.org/software/S0615) is a modular backdoor written in C++ that has been used since at least 2019 to download and execute malicious payloads, including [FIVEHANDS](https://attack.mitre.org/software/S0618) ransomware.(Citation: BlackBerry CostaRicto November 2020)(Citation: FireEye FiveHands April 2021)(Citation: CISA AR21-126A FIVEHANDS May 2021)

## Techniques Used
- T1005: Data from Local System
- T1007: System Service Discovery
- T1027: Obfuscated Files or Information
- T1033: System Owner/User Discovery
- T1036: Masquerading
- T1041: Exfiltration Over C2 Channel
- T1055.001: Dynamic-link Library Injection
- T1057: Process Discovery
- T1070.004: File Deletion
- T1071.004: DNS
- T1074.001: Local Data Staging
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1090: Proxy
- T1095: Non-Application Layer Protocol
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1124: System Time Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1560.003: Archive via Custom Method
- T1564.010: Process Argument Spoofing
- T1568.002: Domain Generation Algorithms
- T1573.001: Symmetric Cryptography
- T1573.002: Asymmetric Cryptography
