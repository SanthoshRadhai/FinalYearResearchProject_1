# S1178: ShrinkLocker

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1178  
**Aliases:** ShrinkLocker  
**Platforms:** Windows  

## Description
[ShrinkLocker](https://attack.mitre.org/software/S1178) is a VBS-based malicious script that leverages the legitimate Bitlocker application to encrypt files on victim systems for ransom. [ShrinkLocker](https://attack.mitre.org/software/S1178) functions by using Bitlocker to encrypt files, then renames impacted drives to the adversary’s contact email address to facilitate communication for the ransom payment.(Citation: Kaspersky ShrinkLocker 2024)(Citation: Splunk ShrinkLocker 2024)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1041: Exfiltration Over C2 Channel
- T1047: Windows Management Instrumentation
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.005: Visual Basic
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1102: Web Service
- T1112: Modify Registry
- T1124: System Time Discovery
- T1480: Execution Guardrails
- T1485: Data Destruction
- T1486: Data Encrypted for Impact
- T1491.001: Internal Defacement
- T1529: System Shutdown/Reboot
- T1561.002: Disk Structure Wipe
- T1685: Disable or Modify Tools
- T1685.005: Clear Windows Event Logs
- T1686: Disable or Modify System Firewall
