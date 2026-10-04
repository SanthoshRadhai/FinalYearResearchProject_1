# S1149: CHIMNEYSWEEP

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1149  
**Aliases:** CHIMNEYSWEEP  
**Platforms:** Windows  

## Description
[CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) is a backdoor malware that was deployed during [HomeLand Justice](https://attack.mitre.org/campaigns/C0038) along with [ROADSWEEP](https://attack.mitre.org/software/S1150) ransomware, and has been used to target Farsi and Arabic speakers since at least 2012.(Citation: Mandiant ROADSWEEP August 2022)

## Techniques Used
- T1005: Data from Local System
- T1027: Obfuscated Files or Information
- T1027.001: Binary Padding
- T1027.007: Dynamic API Resolution
- T1027.009: Embedded Payloads
- T1033: System Owner/User Discovery
- T1041: Exfiltration Over C2 Channel
- T1053.005: Scheduled Task
- T1056.001: Keylogging
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.005: Visual Basic
- T1070.006: Timestomp
- T1071.001: Web Protocols
- T1074.001: Local Data Staging
- T1083: File and Directory Discovery
- T1102: Web Service
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1112: Modify Registry
- T1113: Screen Capture
- T1115: Clipboard Data
- T1120: Peripheral Device Discovery
- T1132.002: Non-Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1218.003: CMSTP
- T1480: Execution Guardrails
- T1518.001: Security Software Discovery
- T1529: System Shutdown/Reboot
- T1548.002: Bypass User Account Control
- T1553.002: Code Signing
