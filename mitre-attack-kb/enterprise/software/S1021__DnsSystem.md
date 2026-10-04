# S1021: DnsSystem

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1021  
**Aliases:** DnsSystem  
**Platforms:** Windows  

## Description
[DnsSystem](https://attack.mitre.org/software/S1021) is a .NET based DNS backdoor, which is a customized version of the open source tool DIG.net, that has been used by [HEXANE](https://attack.mitre.org/groups/G1001) since at least June 2022.(Citation: Zscaler Lyceum DnsSystem June 2022)

## Techniques Used
- T1005: Data from Local System
- T1033: System Owner/User Discovery
- T1041: Exfiltration Over C2 Channel
- T1059.003: Windows Command Shell
- T1071.004: DNS
- T1105: Ingress Tool Transfer
- T1132.001: Standard Encoding
- T1204.002: Malicious File
- T1547.001: Registry Run Keys / Startup Folder
