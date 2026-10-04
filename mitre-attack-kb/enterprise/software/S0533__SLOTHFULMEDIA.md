# S0533: SLOTHFULMEDIA

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0533  
**Aliases:** SLOTHFULMEDIA, JackOfHearts, QueenOfClubs  
**Platforms:** Windows  

## Description
[SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) is a remote access Trojan written in C++ that has been used by an unidentified "sophisticated cyber actor" since at least January 2017.(Citation: CISA MAR SLOTHFULMEDIA October 2020)(Citation: Costin Raiu IAmTheKing October 2020) It has been used to target government organizations, defense contractors, universities, and energy companies in Russia, India, Kazakhstan, Kyrgyzstan, Malaysia, Ukraine, and Eastern Europe.(Citation: USCYBERCOM SLOTHFULMEDIA October 2020)(Citation: Kaspersky IAmTheKing October 2020)  

In October 2020, Kaspersky Labs assessed [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) is part of an activity cluster it refers to as "IAmTheKing".(Citation: Kaspersky IAmTheKing October 2020) ESET also noted code similarity between [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) and droppers used by a group it refers to as "PowerPool".(Citation: ESET PowerPool Code October 2020)

## Techniques Used
- T1001: Data Obfuscation
- T1005: Data from Local System
- T1007: System Service Discovery
- T1033: System Owner/User Discovery
- T1036.004: Masquerade Task or Service
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1049: System Network Connections Discovery
- T1055: Process Injection
- T1056.001: Keylogging
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1112: Modify Registry
- T1113: Screen Capture
- T1489: Service Stop
- T1543.003: Windows Service
- T1564.001: Hidden Files and Directories
- T1569.002: Service Execution
- T1680: Local Storage Discovery
