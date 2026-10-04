# G0093: GALLIUM

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0093  
**Aliases:** GALLIUM, Granite Typhoon  

## Description
[GALLIUM](https://attack.mitre.org/groups/G0093) is a cyberespionage group that has been active since at least 2012, primarily targeting telecommunications companies, financial institutions, and government entities in Afghanistan, Australia, Belgium, Cambodia, Malaysia, Mozambique, the Philippines, Russia, and Vietnam. This group is particularly known for launching Operation Soft Cell, a long-term campaign targeting telecommunications providers.(Citation: Cybereason Soft Cell June 2019) Security researchers have identified [GALLIUM](https://attack.mitre.org/groups/G0093) as a likely Chinese state-sponsored group, based in part on tools used and TTPs commonly associated with Chinese threat actors.(Citation: Cybereason Soft Cell June 2019)(Citation: Microsoft GALLIUM December 2019)(Citation: Unit 42 PingPull Jun 2022)

## Techniques Used
- T1003.001: LSASS Memory
- T1003.002: Security Account Manager
- T1005: Data from Local System
- T1016: System Network Configuration Discovery
- T1018: Remote System Discovery
- T1027: Obfuscated Files or Information
- T1027.002: Software Packing
- T1027.005: Indicator Removal from Tools
- T1033: System Owner/User Discovery
- T1036.003: Rename Legitimate Utilities
- T1041: Exfiltration Over C2 Channel
- T1047: Windows Management Instrumentation
- T1049: System Network Connections Discovery
- T1053.005: Scheduled Task
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1074.001: Local Data Staging
- T1078: Valid Accounts
- T1090.002: External Proxy
- T1105: Ingress Tool Transfer
- T1133: External Remote Services
- T1136.002: Domain Account
- T1190: Exploit Public-Facing Application
- T1505.003: Web Shell
- T1550.002: Pass the Hash
- T1553.002: Code Signing
- T1560.001: Archive via Utility
- T1570: Lateral Tool Transfer
- T1574.001: DLL
- T1583.004: Server
- T1588.002: Tool
