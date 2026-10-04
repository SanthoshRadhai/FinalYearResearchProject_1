# S1152: IMAPLoader

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1152  
**Aliases:** IMAPLoader  
**Platforms:** Windows  

## Description
[IMAPLoader](https://attack.mitre.org/software/S1152) is a .NET-based loader malware exclusively associated with [CURIUM](https://attack.mitre.org/groups/G1012) operations since at least 2022. [IMAPLoader](https://attack.mitre.org/software/S1152) leverages email protocols for command and control and payload delivery.(Citation: PWC Yellow Liderc 2023)

## Techniques Used
- T1047: Windows Management Instrumentation
- T1053.005: Scheduled Task
- T1071.003: Mail Protocols
- T1082: System Information Discovery
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1543: Create or Modify System Process
- T1564.003: Hidden Window
- T1574.014: AppDomainManager
