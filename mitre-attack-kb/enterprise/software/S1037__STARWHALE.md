# S1037: STARWHALE

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1037  
**Aliases:** STARWHALE, CANOPY  
**Platforms:** Windows  

## Description
[STARWHALE](https://attack.mitre.org/software/S1037) is Windows Script File (WSF) backdoor that has been used by [MuddyWater](https://attack.mitre.org/groups/G0069), possibly since at least November 2021; there is also a [STARWHALE](https://attack.mitre.org/software/S1037) variant written in Golang with similar capabilities. Security researchers have also noted the use of [STARWHALE](https://attack.mitre.org/software/S1037) by UNC3313, which may be associated with [MuddyWater](https://attack.mitre.org/groups/G0069).(Citation: Mandiant UNC3313 Feb 2022)(Citation: DHS CISA AA22-055A MuddyWater February 2022)

## Techniques Used
- T1005: Data from Local System
- T1016: System Network Configuration Discovery
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1041: Exfiltration Over C2 Channel
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1071.001: Web Protocols
- T1074.001: Local Data Staging
- T1082: System Information Discovery
- T1132.001: Standard Encoding
- T1204.002: Malicious File
- T1543.003: Windows Service
- T1547.001: Registry Run Keys / Startup Folder
