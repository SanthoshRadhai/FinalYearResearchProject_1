# S1179: Exbyte

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1179  
**Aliases:** Exbyte  
**Platforms:** Windows  

## Description
[Exbyte](https://attack.mitre.org/software/S1179) is an exfiltration tool written in Go that is uniquely associated with [BlackByte](https://attack.mitre.org/groups/G1043) operations. Observed since 2022, [Exbyte](https://attack.mitre.org/software/S1179) transfers collected files to online file sharing and hosting services.(Citation: Symantec BlackByte 2022)

## Techniques Used
- T1069.001: Local Groups
- T1070.004: File Deletion
- T1083: File and Directory Discovery
- T1106: Native API
- T1140: Deobfuscate/Decode Files or Information
- T1480: Execution Guardrails
- T1497.001: System Checks
- T1518.001: Security Software Discovery
- T1567: Exfiltration Over Web Service
