# S1089: SharpDisco

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1089  
**Aliases:** SharpDisco  
**Platforms:** Windows  

## Description
[SharpDisco](https://attack.mitre.org/software/S1089) is a dropper developed in C# that has been used by [MoustachedBouncer](https://attack.mitre.org/groups/G1019) since at least 2020 to load malicious plugins.(Citation: MoustachedBouncer ESET August 2023)

## Techniques Used
- T1005: Data from Local System
- T1041: Exfiltration Over C2 Channel
- T1053.005: Scheduled Task
- T1059.003: Windows Command Shell
- T1071.002: File Transfer Protocols
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1120: Peripheral Device Discovery
- T1564.003: Hidden Window
- T1680: Local Storage Discovery
