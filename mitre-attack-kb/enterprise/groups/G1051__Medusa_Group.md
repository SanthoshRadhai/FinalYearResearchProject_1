# G1051: Medusa Group

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G1051  
**Aliases:** Medusa Group  

## Description
[Medusa Group](https://attack.mitre.org/groups/G1051) has been active since at least 2021 and was initially operated as a closed ransomware group before evolving into a Ransomware-as-a-Service (RaaS) operation. Some reporting indicates that certain attacks may still be conducted directly by the ransomware’s core developers. Public sources have also referred to the group as “Spearwing” or “Medusa Actors.” (Citation: CISA Medusa Group Medusa Ransomware March 2025) (Citation: Broadcom Medusa Ransomware Medusa Group March 2025) [Medusa Group](https://attack.mitre.org/groups/G1051) employs living-off-the-land techniques, frequently leveraging publicly available tools and common remote management software to conduct operations. The group engages in double extortion tactics, exfiltrating data prior to encryption and threatening to publish stolen information if ransom demands are not met. (Citation: Security Scorecard Medusa Ransomware January 2024) For initial access, [Medusa Group](https://attack.mitre.org/groups/G1051) has exploited publicly known vulnerabilities, conducted phishing campaigns, and used credentials or access purchased from Initial Access Brokers (IABs). The group is opportunistic and has targeted a wide range of sectors globally. (Citation: Intel471 Medusa Ransomware May 2025)

## Techniques Used
- T1003.001: LSASS Memory
- T1003.003: NTDS
- T1016: System Network Configuration Discovery
- T1018: Remote System Discovery
- T1021.001: Remote Desktop Protocol
- T1027.002: Software Packing
- T1027.010: Command Obfuscation
- T1033: System Owner/User Discovery
- T1046: Network Service Discovery
- T1047: Windows Management Instrumentation
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1069.002: Domain Groups
- T1070.003: Clear Command History
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1072: Software Deployment Tools
- T1078: Valid Accounts
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087.001: Local Account
- T1090.003: Multi-hop Proxy
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1112: Modify Registry
- T1135: Network Share Discovery
- T1136.002: Domain Account
- T1190: Exploit Public-Facing Application
- T1218.014: MMC
- T1219: Remote Access Tools
- T1486: Data Encrypted for Impact
- T1489: Service Stop
- T1490: Inhibit System Recovery
- T1505.003: Web Shell
- T1518.001: Security Software Discovery
- T1529: System Shutdown/Reboot
- T1543.003: Windows Service
- T1548.002: Bypass User Account Control
- T1553.002: Code Signing
- T1559.001: Component Object Model
- T1564.003: Hidden Window
- T1567.002: Exfiltration to Cloud Storage
- T1569.002: Service Execution
- T1570: Lateral Tool Transfer
- T1573.002: Asymmetric Cryptography
- T1583.006: Web Services
- T1585.001: Social Media Accounts
- T1585.002: Email Accounts
- T1588.002: Tool
- T1608.002: Upload Tool
- T1650: Acquire Access
- T1652: Device Driver Discovery
- T1657: Financial Theft
- T1685: Disable or Modify Tools
- T1686: Disable or Modify System Firewall
- T1690: Prevent Command History Logging
