# S0504: Anchor

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0504  
**Aliases:** Anchor, Anchor_DNS  
**Platforms:** Linux, Windows  

## Description
[Anchor](https://attack.mitre.org/software/S0504) is one of a family of backdoor malware that has been used in conjunction with [TrickBot](https://attack.mitre.org/software/S0266) on selected high profile targets since at least 2018.(Citation: Cyberreason Anchor December 2019)(Citation: Medium Anchor DNS July 2020)

## Techniques Used
- T1008: Fallback Channels
- T1016: System Network Configuration Discovery
- T1021.002: SMB/Windows Admin Shares
- T1027: Obfuscated Files or Information
- T1027.002: Software Packing
- T1053.003: Cron
- T1053.005: Scheduled Task
- T1059.003: Windows Command Shell
- T1059.004: Unix Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1071.004: DNS
- T1082: System Information Discovery
- T1095: Non-Application Layer Protocol
- T1105: Ingress Tool Transfer
- T1480: Execution Guardrails
- T1543.003: Windows Service
- T1553.002: Code Signing
- T1564.004: NTFS File Attributes
- T1569.002: Service Execution
