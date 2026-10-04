# S0603: Stuxnet

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0603  
**Aliases:** Stuxnet, W32.Stuxnet  
**Platforms:** Windows  

## Description
[Stuxnet](https://attack.mitre.org/software/S0603) was the first publicly reported malware to specifically target industrial control systems devices. [Stuxnet](https://attack.mitre.org/software/S0603) is a large and complex malware that utilized multiple behaviors, including numerous zero-day vulnerabilities, a sophisticated Windows rootkit, and network infection routines.(Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)(Citation: CISA ICS Advisory ICSA-10-272-01)(Citation: ESET Stuxnet Under the Microscope)(Citation: Langer Stuxnet) [Stuxnet](https://attack.mitre.org/software/S0603) was discovered in 2010, with some components being used as early as November 2008.(Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

## Techniques Used
- T1008: Fallback Channels
- T1012: Query Registry
- T1014: Rootkit
- T1016: System Network Configuration Discovery
- T1021: Remote Services
- T1021.002: SMB/Windows Admin Shares
- T1027.013: Encrypted/Encoded File
- T1041: Exfiltration Over C2 Channel
- T1047: Windows Management Instrumentation
- T1053.005: Scheduled Task
- T1055.001: Dynamic-link Library Injection
- T1068: Exploitation for Privilege Escalation
- T1070: Indicator Removal
- T1070.004: File Deletion
- T1070.006: Timestomp
- T1071.001: Web Protocols
- T1078.001: Default Accounts
- T1078.002: Domain Accounts
- T1080: Taint Shared Content
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087.001: Local Account
- T1087.002: Domain Account
- T1090.001: Internal Proxy
- T1091: Replication Through Removable Media
- T1106: Native API
- T1112: Modify Registry
- T1120: Peripheral Device Discovery
- T1124: System Time Discovery
- T1129: Shared Modules
- T1132.001: Standard Encoding
- T1134.001: Token Impersonation/Theft
- T1135: Network Share Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1210: Exploitation of Remote Services
- T1480: Execution Guardrails
- T1505.001: SQL Stored Procedures
- T1518.001: Security Software Discovery
- T1543.003: Windows Service
- T1553.002: Code Signing
- T1560.003: Archive via Custom Method
- T1570: Lateral Tool Transfer
- T1573.001: Symmetric Cryptography
- T1685: Disable or Modify Tools
