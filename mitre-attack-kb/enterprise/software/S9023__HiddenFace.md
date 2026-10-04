# S9023: HiddenFace

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9023  
**Aliases:** HiddenFace, NOOPDOOR  
**Platforms:** Windows  

## Description
[HiddenFace](https://attack.mitre.org/software/S9023) is a modular backdoor developed and used exclusively by [MirrorFace](https://attack.mitre.org/groups/G1054) since at least 2021. [HiddenFace](https://attack.mitre.org/software/S9023) can communicate both actively and passively and has been used against political and academic targets.(Citation: JPCERT MirrorFace JUL 2024)(Citation: Trend Micro Earth Kasha NOV 2024)(Citation: Trend Micro Earth Kasha Updates APR 2025)

## Techniques Used
- T1005: Data from Local System
- T1008: Fallback Channels
- T1027.007: Dynamic API Resolution
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1053.005: Scheduled Task
- T1055: Process Injection
- T1057: Process Discovery
- T1070.006: Timestomp
- T1082: System Information Discovery
- T1090.001: Internal Proxy
- T1095: Non-Application Layer Protocol
- T1105: Ingress Tool Transfer
- T1112: Modify Registry
- T1140: Deobfuscate/Decode Files or Information
- T1480: Execution Guardrails
- T1480.002: Mutual Exclusion
- T1497.003: Time Based Checks
- T1518.001: Security Software Discovery
- T1568.002: Domain Generation Algorithms
- T1571: Non-Standard Port
- T1572: Protocol Tunneling
- T1573.001: Symmetric Cryptography
- T1573.002: Asymmetric Cryptography
- T1686.003: Windows Host Firewall
