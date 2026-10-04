# S0493: GoldenSpy

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0493  
**Aliases:** GoldenSpy  
**Platforms:** Windows  

## Description
[GoldenSpy](https://attack.mitre.org/software/S0493) is a backdoor malware which has been packaged with legitimate tax preparation software. [GoldenSpy](https://attack.mitre.org/software/S0493) was discovered targeting organizations in China, being delivered with the "Intelligent Tax" software suite which is produced by the Golden Tax Department of Aisino Credit Information Co. and required to pay local taxes.(Citation: Trustwave GoldenSpy June 2020)

## Techniques Used
- T1027.013: Encrypted/Encoded File
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1136.001: Local Account
- T1195.002: Compromise Software Supply Chain
- T1497.003: Time Based Checks
- T1543.003: Windows Service
- T1571: Non-Standard Port
