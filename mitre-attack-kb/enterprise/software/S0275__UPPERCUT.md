# S0275: UPPERCUT

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0275  
**Aliases:** UPPERCUT, ANEL  
**Platforms:** Windows  

## Description
[UPPERCUT](https://attack.mitre.org/software/S0275) is a 32-bit HTTP-based backdoor that has been used by [menuPass](https://attack.mitre.org/groups/G0045) since at least 2017.(Citation: FireEye APT10 Sept 2018) Once thought to be exclusive to [menuPass](https://attack.mitre.org/groups/G0045), [UPPERCUT](https://attack.mitre.org/software/S0275) was also observed being used by [menuPass](https://attack.mitre.org/groups/G0045)-associated [MirrorFace](https://attack.mitre.org/groups/G1054) during [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060).(Citation: Trend Micro Earth Kasha Anel NOV 2024)

## Techniques Used
- T1005: Data from Local System
- T1016: System Network Configuration Discovery
- T1033: System Owner/User Discovery
- T1059.003: Windows Command Shell
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1113: Screen Capture
- T1124: System Time Discovery
- T1132.001: Standard Encoding
- T1548.002: Bypass User Account Control
- T1573.001: Symmetric Cryptography
- T1574.001: DLL
- T1678: Delay Execution
