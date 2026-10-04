# G0010: Turla

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0010  
**Aliases:** Turla, IRON HUNTER, Group 88, Waterbug, WhiteBear, Snake, Krypton, Venomous Bear, Secret Blizzard, BELUGASTURGEON  

## Description
[Turla](https://attack.mitre.org/groups/G0010) is a cyber espionage threat group that has been attributed to Russia's Federal Security Service (FSB).  They have compromised victims in over 50 countries since at least 2004, spanning a range of industries including government, embassies, military, education, research and pharmaceutical companies. [Turla](https://attack.mitre.org/groups/G0010) is known for conducting watering hole and spearphishing campaigns, and leveraging in-house tools and malware, such as [Uroburos](https://attack.mitre.org/software/S0022).(Citation: Kaspersky Turla)(Citation: ESET Gazer Aug 2017)(Citation: CrowdStrike VENOMOUS BEAR)(Citation: ESET Turla Mosquito Jan 2018)(Citation: Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023)

## Techniques Used
- T1005: Data from Local System
- T1007: System Service Discovery
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1016.001: Internet Connection Discovery
- T1018: Remote System Discovery
- T1021.002: SMB/Windows Admin Shares
- T1025: Data from Removable Media
- T1027.005: Indicator Removal from Tools
- T1027.010: Command Obfuscation
- T1027.011: Fileless Storage
- T1036.005: Match Legitimate Resource Name or Location
- T1049: System Network Connections Discovery
- T1055: Process Injection
- T1055.001: Dynamic-link Library Injection
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1059.006: Python
- T1059.007: JavaScript
- T1068: Exploitation for Privilege Escalation
- T1069.001: Local Groups
- T1069.002: Domain Groups
- T1071.001: Web Protocols
- T1071.003: Mail Protocols
- T1078.003: Local Accounts
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087.001: Local Account
- T1087.002: Domain Account
- T1090: Proxy
- T1090.001: Internal Proxy
- T1102: Web Service
- T1102.002: Bidirectional Communication
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1110: Brute Force
- T1112: Modify Registry
- T1120: Peripheral Device Discovery
- T1124: System Time Discovery
- T1134.002: Create Process with Token
- T1140: Deobfuscate/Decode Files or Information
- T1189: Drive-by Compromise
- T1201: Password Policy Discovery
- T1204.001: Malicious Link
- T1213.006: Databases
- T1518.001: Security Software Discovery
- T1546.003: Windows Management Instrumentation Event Subscription
- T1546.013: PowerShell Profile
- T1547.001: Registry Run Keys / Startup Folder
- T1547.004: Winlogon Helper DLL
- T1553.006: Code Signing Policy Modification
- T1555.004: Windows Credential Manager
- T1560.001: Archive via Utility
- T1564.012: File/Path Exclusions
- T1566.002: Spearphishing Link
- T1567.002: Exfiltration to Cloud Storage
- T1570: Lateral Tool Transfer
- T1583.006: Web Services
- T1584.003: Virtual Private Server
- T1584.004: Server
- T1584.006: Web Services
- T1587.001: Malware
- T1588.001: Malware
- T1588.002: Tool
- T1615: Group Policy Discovery
- T1685: Disable or Modify Tools
