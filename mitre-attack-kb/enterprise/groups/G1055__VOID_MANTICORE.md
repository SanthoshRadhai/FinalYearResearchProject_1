# G1055: VOID MANTICORE

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G1055  
**Aliases:** VOID MANTICORE, COBALT MYSTIQUE, Handala Hack, Homeland Justice, Karma, Karmabelow80, BANISHED KITTEN, Red Sandstorm  

## Description
[VOID MANTICORE](https://attack.mitre.org/groups/G1055) is a threat group assessed to operate on behalf of Iran’s Ministry of Intelligence and Security (MOIS).(Citation: Check Point VOID MANTICORE Handala Hack March 2026) Active since at least mid-2022, VOID MANTICORE has targeted government entities, critical infrastructure, and private sector organizations across Albania, Israel, and the United States.(Citation: Check Point VOID MANTICORE Handala Hack March 2026)(Citation: Palo Alto VOID MANTICORE Iran Cyber Threats March 2026) [VOID MANTICORE](https://attack.mitre.org/groups/G1055) conducts destructive cyber operations, combining wiper attacks with hack-and-leak campaigns. The group has operated under multiple public-facing personas, including [HomeLand Justice](https://attack.mitre.org/campaigns/C0038) in operations against Albania, Karma and Karma Below in campaigns targeting Israeli organizations, and Handala Hack, its current primary persona, which has claimed activity against Israeli and U.S. entities, including a March 2026 attack against Stryker Corporation.(Citation: Check Point VOID MANTICORE Handala Hack March 2026)(Citation: DOJ FBI Handala Hack March 2026)  [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has been observed collaborating with Scarred Manticore, which has been linked to initial access operations preceding VOID MANTICORE’s activity.(Citation: Domain Tools Handala Hack Karma Homeland Justice MOIS April 2026)

## Techniques Used
- T1003.001: LSASS Memory
- T1005: Data from Local System
- T1021.001: Remote Desktop Protocol
- T1027.015: Compression
- T1036.004: Masquerade Task or Service
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1047: Windows Management Instrumentation
- T1059.001: PowerShell
- T1059.006: Python
- T1071.001: Web Protocols
- T1072: Software Deployment Tools
- T1074: Data Staged
- T1078: Valid Accounts
- T1078.002: Domain Accounts
- T1078.004: Cloud Accounts
- T1082: System Information Discovery
- T1087.002: Domain Account
- T1098: Account Manipulation
- T1102: Web Service
- T1105: Ingress Tool Transfer
- T1110: Brute Force
- T1110.001: Password Guessing
- T1110.004: Credential Stuffing
- T1113: Screen Capture
- T1114.002: Remote Email Collection
- T1119: Automated Collection
- T1123: Audio Capture
- T1125: Video Capture
- T1133: External Remote Services
- T1190: Exploit Public-Facing Application
- T1199: Trusted Relationship
- T1204.002: Malicious File
- T1213.002: Sharepoint
- T1219.002: Remote Desktop Software
- T1484.001: Group Policy Modification
- T1485: Data Destruction
- T1486: Data Encrypted for Impact
- T1490: Inhibit System Recovery
- T1547.001: Registry Run Keys / Startup Folder
- T1552.002: Credentials in Registry
- T1560.001: Archive via Utility
- T1561.001: Disk Content Wipe
- T1561.002: Disk Structure Wipe
- T1564.003: Hidden Window
- T1566: Phishing
- T1572: Protocol Tunneling
- T1583.001: Domains
- T1583.003: Virtual Private Server
- T1583.004: Server
- T1583.006: Web Services
- T1585.001: Social Media Accounts
- T1585.002: Email Accounts
- T1587.001: Malware
- T1588.001: Malware
- T1588.002: Tool
- T1589: Gather Victim Identity Information
- T1595.002: Vulnerability Scanning
- T1651: Cloud Administration Command
- T1657: Financial Theft
- T1679: Selective Exclusion
- T1684.001: Impersonation
- T1686.003: Windows Host Firewall
