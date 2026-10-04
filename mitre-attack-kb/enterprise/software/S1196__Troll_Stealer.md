# S1196: Troll Stealer

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1196  
**Aliases:** Troll Stealer  
**Platforms:** Windows  

## Description
[Troll Stealer](https://attack.mitre.org/software/S1196) is an information stealer written in Go associated with [Kimsuky](https://attack.mitre.org/groups/G0094) operations. [Troll Stealer](https://attack.mitre.org/software/S1196) has typically been delivered through a dropper disguised as a legitimate security program installation file. [Troll Stealer](https://attack.mitre.org/software/S1196) features code similar to [AppleSeed](https://attack.mitre.org/software/S0622), also uniquely associated with [Kimsuky](https://attack.mitre.org/groups/G0094) operations.(Citation: S2W Troll Stealer 2024)(Citation: Symantec Troll Stealer 2024)

## Techniques Used
- T1005: Data from Local System
- T1016: System Network Configuration Discovery
- T1027.002: Software Packing
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1074.001: Local Data Staging
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1113: Screen Capture
- T1132.001: Standard Encoding
- T1213: Data from Information Repositories
- T1217: Browser Information Discovery
- T1218.011: Rundll32
- T1480.002: Mutual Exclusion
- T1552.004: Private Keys
- T1553.002: Code Signing
- T1560: Archive Collected Data
- T1573.001: Symmetric Cryptography
