# S1242: Qilin

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1242  
**Aliases:** Qilin, Agenda  
**Platforms:** ESXi, Windows, Linux  

## Description
[Qilin](https://attack.mitre.org/software/S1242) is a ransomware family operated as a ransomware-as-a-service (RaaS) that has been active since at least 2022. It includes variants written in Go and Rust capable of targeting Windows, Linux, and VMware ESXi environments. [Qilin](https://attack.mitre.org/software/S1242) shares functionality overlaps with [Black Basta](https://attack.mitre.org/software/S1070), [REvil](https://attack.mitre.org/software/S0496), and [BlackCat](https://attack.mitre.org/software/S1068) ransomware. [Qilin](https://attack.mitre.org/software/S1242) affiliates have targeted multiple entities worldwide with the majority of victims in the US, France, Canada, and the UK, primarily in the manufacturing, technology, financial services, and healthcare sectors.(Citation: Trend Micro Agenda Ransomware AUG 2022)(Citation: SentinelOne Qilin NOV 2022)(Citation: BushidoToken Qilin RaaS JUN 2024)(Citation: Sophos Qilin MSP APR 2025)(Citation: Trend Micro Agenda Ransomware OCT 2025)

## Techniques Used
- T1003.001: LSASS Memory
- T1007: System Service Discovery
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1018: Remote System Discovery
- T1021.002: SMB/Windows Admin Shares
- T1021.004: SSH
- T1027.013: Encrypted/Encoded File
- T1036.004: Masquerade Task or Service
- T1036.005: Match Legitimate Resource Name or Location
- T1047: Windows Management Instrumentation
- T1053.005: Scheduled Task
- T1055.001: Dynamic-link Library Injection
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1069.002: Domain Groups
- T1070.004: File Deletion
- T1071.002: File Transfer Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087.001: Local Account
- T1087.002: Domain Account
- T1106: Native API
- T1112: Modify Registry
- T1134: Access Token Manipulation
- T1135: Network Share Discovery
- T1190: Exploit Public-Facing Application
- T1204.001: Malicious Link
- T1204.002: Malicious File
- T1219.002: Remote Desktop Software
- T1222: File and Directory Permissions Modification
- T1480: Execution Guardrails
- T1480.002: Mutual Exclusion
- T1484.001: Group Policy Modification
- T1486: Data Encrypted for Impact
- T1489: Service Stop
- T1490: Inhibit System Recovery
- T1491.001: Internal Defacement
- T1529: System Shutdown/Reboot
- T1547.001: Registry Run Keys / Startup Folder
- T1547.004: Winlogon Helper DLL
- T1548.002: Bypass User Account Control
- T1566.001: Spearphishing Attachment
- T1566.002: Spearphishing Link
- T1570: Lateral Tool Transfer
- T1673: Virtual Machine Discovery
- T1678: Delay Execution
- T1680: Local Storage Discovery
- T1685: Disable or Modify Tools
- T1685.005: Clear Windows Event Logs
- T1688: Safe Mode Boot
