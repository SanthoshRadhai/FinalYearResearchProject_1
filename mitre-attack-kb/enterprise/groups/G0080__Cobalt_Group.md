# G0080: Cobalt Group

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0080  
**Aliases:** Cobalt Group, GOLD KINGSWOOD, Cobalt Gang, Cobalt Spider  

## Description
[Cobalt Group](https://attack.mitre.org/groups/G0080) is a financially motivated threat group that has primarily targeted financial institutions since at least 2016. The group has conducted intrusions to steal money via targeting ATM systems, card processing, payment systems and SWIFT systems. [Cobalt Group](https://attack.mitre.org/groups/G0080) has mainly targeted banks in Eastern Europe, Central Asia, and Southeast Asia. One of the alleged leaders was arrested in Spain in early 2018, but the group still appears to be active. The group has been known to target organizations in order to use their access to then compromise additional victims.(Citation: Talos Cobalt Group July 2018)(Citation: PTSecurity Cobalt Group Aug 2017)(Citation: PTSecurity Cobalt Dec 2016)(Citation: Group IB Cobalt Aug 2017)(Citation: Proofpoint Cobalt June 2017)(Citation: RiskIQ Cobalt Nov 2017)(Citation: RiskIQ Cobalt Jan 2018) Reporting indicates there may be links between [Cobalt Group](https://attack.mitre.org/groups/G0080) and both the malware [Carbanak](https://attack.mitre.org/software/S0030) and the group [Carbanak](https://attack.mitre.org/groups/G0008).(Citation: Europol Cobalt Mar 2018)

## Techniques Used
- T1021.001: Remote Desktop Protocol
- T1027.010: Command Obfuscation
- T1037.001: Logon Script (Windows)
- T1046: Network Service Discovery
- T1053.005: Scheduled Task
- T1055: Process Injection
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1059.007: JavaScript
- T1068: Exploitation for Privilege Escalation
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1071.004: DNS
- T1105: Ingress Tool Transfer
- T1195.002: Compromise Software Supply Chain
- T1203: Exploitation for Client Execution
- T1204.001: Malicious Link
- T1204.002: Malicious File
- T1218.003: CMSTP
- T1218.008: Odbcconf
- T1218.010: Regsvr32
- T1219: Remote Access Tools
- T1220: XSL Script Processing
- T1518.001: Security Software Discovery
- T1543.003: Windows Service
- T1547.001: Registry Run Keys / Startup Folder
- T1548.002: Bypass User Account Control
- T1559.002: Dynamic Data Exchange
- T1566.001: Spearphishing Attachment
- T1566.002: Spearphishing Link
- T1572: Protocol Tunneling
- T1573.002: Asymmetric Cryptography
- T1588.002: Tool
