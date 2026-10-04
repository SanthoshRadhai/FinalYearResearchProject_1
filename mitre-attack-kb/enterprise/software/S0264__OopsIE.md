# S0264: OopsIE

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0264  
**Aliases:** OopsIE  
**Platforms:** Windows  

## Description
[OopsIE](https://attack.mitre.org/software/S0264) is a Trojan used by [OilRig](https://attack.mitre.org/groups/G0049) to remotely execute commands as well as upload/download files to/from victims. (Citation: Unit 42 OopsIE! Feb 2018)

## Techniques Used
- T1027: Obfuscated Files or Information
- T1027.002: Software Packing
- T1030: Data Transfer Size Limits
- T1041: Exfiltration Over C2 Channel
- T1047: Windows Management Instrumentation
- T1053.005: Scheduled Task
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1074.001: Local Data Staging
- T1082: System Information Discovery
- T1105: Ingress Tool Transfer
- T1124: System Time Discovery
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1497.001: System Checks
- T1560.001: Archive via Utility
- T1560.003: Archive via Custom Method
