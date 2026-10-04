# S1019: Shark

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1019  
**Aliases:** Shark  
**Platforms:** Windows  

## Description
[Shark](https://attack.mitre.org/software/S1019) is a backdoor malware written in C# and .NET that is an updated version of [Milan](https://attack.mitre.org/software/S1015); it has been used by [HEXANE](https://attack.mitre.org/groups/G1001) since at least July 2021.(Citation: ClearSky Siamesekitten August 2021)(Citation: Accenture Lyceum Targets November 2021)

## Techniques Used
- T1005: Data from Local System
- T1008: Fallback Channels
- T1012: Query Registry
- T1027.013: Encrypted/Encoded File
- T1029: Scheduled Transfer
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1071.004: DNS
- T1074: Data Staged
- T1082: System Information Discovery
- T1105: Ingress Tool Transfer
- T1140: Deobfuscate/Decode Files or Information
- T1497.001: System Checks
- T1568.002: Domain Generation Algorithms
