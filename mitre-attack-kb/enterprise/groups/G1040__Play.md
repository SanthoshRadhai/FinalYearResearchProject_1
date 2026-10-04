# G1040: Play

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G1040  
**Aliases:** Play  

## Description
[Play](https://attack.mitre.org/groups/G1040) is a ransomware group that has been active since at least 2022 deploying  [Playcrypt](https://attack.mitre.org/software/S1162) ransomware against the business, government, critical infrastructure, healthcare, and media sectors in North America, South America, and Europe. [Play](https://attack.mitre.org/groups/G1040) actors employ a double-extortion model, encrypting systems after exfiltrating data, and are presumed by security researchers to operate as a closed group.(Citation: CISA Play Ransomware Advisory December 2023)(Citation: Trend Micro Ransomware Spotlight Play July 2023)

## Techniques Used
- T1003.001: LSASS Memory
- T1016: System Network Configuration Discovery
- T1018: Remote System Discovery
- T1021.002: SMB/Windows Admin Shares
- T1027.010: Command Obfuscation
- T1030: Data Transfer Size Limits
- T1048: Exfiltration Over Alternative Protocol
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1078: Valid Accounts
- T1078.002: Domain Accounts
- T1078.003: Local Accounts
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1133: External Remote Services
- T1190: Exploit Public-Facing Application
- T1518.001: Security Software Discovery
- T1560.001: Archive via Utility
- T1587.001: Malware
- T1588.002: Tool
- T1657: Financial Theft
- T1685: Disable or Modify Tools
- T1685.005: Clear Windows Event Logs
