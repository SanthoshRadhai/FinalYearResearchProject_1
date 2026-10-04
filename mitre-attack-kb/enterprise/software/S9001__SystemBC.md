# S9001: SystemBC

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9001  
**Aliases:** SystemBC, Coroxy  
**Platforms:** Linux, Windows  

## Description
[SystemBC](https://attack.mitre.org/software/S9001) is a malware family offered as a malware-as-a-service (MaaS) that is used to establish command and control and facilitate follow-on activity, including ransomware deployment.[SystemBC](https://attack.mitre.org/software/S9001) executes a variety of tasks including setting up SOCKS5 proxies, maintaining persistence, ingesting malicious files, and handing C2 communication. [SystemBC](https://attack.mitre.org/software/S9001) was first detected in 2018, and has been used by [Wizard Spider](https://attack.mitre.org/groups/G0102) since at least 2020, and by [FIN7](https://attack.mitre.org/groups/G0046) since at least 2022.(Citation: TrumanKroll_SYSTEMBCServer_Jan2024)(Citation: SophosGnGal_SystemBC_Dec2020)(Citation: BlackBasta)(Citation: AhnLab_SystemBC_Apr2022)(Citation: Lumen_SystemBC_Sept2025)

## Techniques Used
- T1001: Data Obfuscation
- T1053.005: Scheduled Task
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1071.004: DNS
- T1082: System Information Discovery
- T1087.001: Local Account
- T1090.003: Multi-hop Proxy
- T1095: Non-Application Layer Protocol
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1124: System Time Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1480: Execution Guardrails
- T1564.003: Hidden Window
- T1571: Non-Standard Port
- T1573.001: Symmetric Cryptography
- T1620: Reflective Code Loading
- T1678: Delay Execution
