# G0102: Wizard Spider

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0102  
**Aliases:** Wizard Spider, UNC1878, TEMP.MixMaster, Grim Spider, FIN12, GOLD BLACKBURN, ITG23, Periwinkle Tempest, DEV-0193, Pistachio Tempest, DEV-0237  

## Description
[Wizard Spider](https://attack.mitre.org/groups/G0102) is a Russia-based financially motivated threat group originally known for the creation and deployment of [TrickBot](https://attack.mitre.org/software/S0266) since at least 2016. [Wizard Spider](https://attack.mitre.org/groups/G0102) possesses a diverse arsenal of tools and has conducted ransomware campaigns against a variety of organizations, ranging from major corporations to hospitals.(Citation: CrowdStrike Ryuk January 2019)(Citation: DHS/CISA Ransomware Targeting Healthcare October 2020)(Citation: CrowdStrike Wizard Spider October 2020)

## Techniques Used
- T1003.001: LSASS Memory
- T1003.002: Security Account Manager
- T1003.003: NTDS
- T1005: Data from Local System
- T1016: System Network Configuration Discovery
- T1018: Remote System Discovery
- T1021: Remote Services
- T1021.001: Remote Desktop Protocol
- T1021.002: SMB/Windows Admin Shares
- T1021.006: Windows Remote Management
- T1027.010: Command Obfuscation
- T1033: System Owner/User Discovery
- T1036.004: Masquerade Task or Service
- T1041: Exfiltration Over C2 Channel
- T1047: Windows Management Instrumentation
- T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol
- T1053.005: Scheduled Task
- T1055: Process Injection
- T1055.001: Dynamic-link Library Injection
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1074: Data Staged
- T1074.001: Local Data Staging
- T1078: Valid Accounts
- T1078.002: Domain Accounts
- T1082: System Information Discovery
- T1087.002: Domain Account
- T1105: Ingress Tool Transfer
- T1112: Modify Registry
- T1133: External Remote Services
- T1135: Network Share Discovery
- T1136.001: Local Account
- T1136.002: Domain Account
- T1197: BITS Jobs
- T1204.001: Malicious Link
- T1204.002: Malicious File
- T1210: Exploitation of Remote Services
- T1218.011: Rundll32
- T1222.001: Windows Permissions
- T1489: Service Stop
- T1490: Inhibit System Recovery
- T1518.001: Security Software Discovery
- T1518.002: Backup Software Discovery
- T1543.003: Windows Service
- T1547.001: Registry Run Keys / Startup Folder
- T1547.004: Winlogon Helper DLL
- T1550.002: Pass the Hash
- T1552.006: Group Policy Preferences
- T1553.002: Code Signing
- T1555.004: Windows Credential Manager
- T1557.001: Name Resolution Poisoning and SMB Relay
- T1558.003: Kerberoasting
- T1560.001: Archive via Utility
- T1566.001: Spearphishing Attachment
- T1566.002: Spearphishing Link
- T1567.002: Exfiltration to Cloud Storage
- T1569.002: Service Execution
- T1570: Lateral Tool Transfer
- T1585.002: Email Accounts
- T1588.002: Tool
- T1588.003: Code Signing Certificates
- T1685: Disable or Modify Tools
