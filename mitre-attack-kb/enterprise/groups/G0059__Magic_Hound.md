# G0059: Magic Hound

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0059  
**Aliases:** Magic Hound, TA453, COBALT ILLUSION, Charming Kitten, ITG18, Phosphorus, Newscaster, APT35, Mint Sandstorm  

## Description
[Magic Hound](https://attack.mitre.org/groups/G0059) is an Iranian-sponsored threat group that conducts long term, resource-intensive cyber espionage operations, likely on behalf of the Islamic Revolutionary Guard Corps. They have targeted European, U.S., and Middle Eastern government and military personnel, academics, journalists, and organizations such as the World Health Organization (WHO), via complex social engineering campaigns since at least 2014.(Citation: FireEye APT35 2018)(Citation: ClearSky Kittens Back 3 August 2020)(Citation: Certfa Charming Kitten January 2021)(Citation: Secureworks COBALT ILLUSION Threat Profile)(Citation: Proofpoint TA453 July2021)

## Techniques Used
- T1003.001: LSASS Memory
- T1005: Data from Local System
- T1016: System Network Configuration Discovery
- T1016.001: Internet Connection Discovery
- T1016.002: Wi-Fi Discovery
- T1018: Remote System Discovery
- T1021.001: Remote Desktop Protocol
- T1027.010: Command Obfuscation
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1036.004: Masquerade Task or Service
- T1036.005: Match Legitimate Resource Name or Location
- T1036.010: Masquerade Account Name
- T1046: Network Service Discovery
- T1047: Windows Management Instrumentation
- T1049: System Network Connections Discovery
- T1053.005: Scheduled Task
- T1056.001: Keylogging
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1070.003: Clear Command History
- T1070.004: File Deletion
- T1071: Application Layer Protocol
- T1071.001: Web Protocols
- T1078.001: Default Accounts
- T1078.002: Domain Accounts
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087.003: Email Account
- T1090: Proxy
- T1098.002: Additional Email Delegate Permissions
- T1098.007: Additional Local or Domain Groups
- T1102.002: Bidirectional Communication
- T1105: Ingress Tool Transfer
- T1112: Modify Registry
- T1113: Screen Capture
- T1114: Email Collection
- T1114.001: Local Email Collection
- T1114.002: Remote Email Collection
- T1136.001: Local Account
- T1189: Drive-by Compromise
- T1190: Exploit Public-Facing Application
- T1204.001: Malicious Link
- T1204.002: Malicious File
- T1218.011: Rundll32
- T1482: Domain Trust Discovery
- T1486: Data Encrypted for Impact
- T1505.003: Web Shell
- T1547.001: Registry Run Keys / Startup Folder
- T1560.001: Archive via Utility
- T1564.003: Hidden Window
- T1566.002: Spearphishing Link
- T1566.003: Spearphishing via Service
- T1567: Exfiltration Over Web Service
- T1570: Lateral Tool Transfer
- T1571: Non-Standard Port
- T1572: Protocol Tunneling
- T1573: Encrypted Channel
- T1583.001: Domains
- T1583.006: Web Services
- T1584.001: Domains
- T1585.001: Social Media Accounts
- T1585.002: Email Accounts
- T1586.002: Email Accounts
- T1588.002: Tool
- T1589: Gather Victim Identity Information
- T1589.001: Credentials
- T1589.002: Email Addresses
- T1590.005: IP Addresses
- T1591.001: Determine Physical Locations
- T1592.002: Software
- T1595.002: Vulnerability Scanning
- T1598.003: Spearphishing Link
- T1685: Disable or Modify Tools
- T1685.001: Disable or Modify Windows Event Log
- T1686.003: Windows Host Firewall
