# G1017: Volt Typhoon

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G1017  
**Aliases:** Volt Typhoon, BRONZE SILHOUETTE, Vanguard Panda, DEV-0391, UNC3236, Voltzite, Insidious Taurus, DazedToad  

## Description
[Volt Typhoon](https://attack.mitre.org/groups/G1017) is a People's Republic of China (PRC) state-sponsored actor that has been active since at least 2021, primarily targeting critical infrastructure organizations in the US and its territories including Guam. [Volt Typhoon](https://attack.mitre.org/groups/G1017)'s targeting and pattern of behavior have been assessed as pre-positioning to enable lateral movement to operational technology (OT) assets for potential destructive or disruptive attacks. [Volt Typhoon](https://attack.mitre.org/groups/G1017) has emphasized stealth in operations using web shells, living-off-the-land (LOTL) binaries, hands on keyboard activities, and stolen credentials.(Citation: CISA AA24-038A PRC Critical Infrastructure February 2024)(Citation: Microsoft Volt Typhoon May 2023)(Citation: Joint Cybersecurity Advisory Volt Typhoon June 2023)(Citation: Secureworks BRONZE SILHOUETTE May 2023). The group has leveraged compromised SOHO routers to proxy command and control traffic and obscure its infrastructure, activity associated with the KV botnet.(Citation: DOJ KVBotnet 2024). 

Reporting indicates a separate initial access cluster, SYLVANITE, has been observed exploiting internet-facing edge devices and transferring access to [Volt Typhoon](https://attack.mitre.org/groups/G1017), also tracked as VOLTZITE, for follow-on operations. (Citation: Dragos 2025 Year in Review)

## Techniques Used
- T1003.001: LSASS Memory
- T1003.003: NTDS
- T1005: Data from Local System
- T1006: Direct Volume Access
- T1007: System Service Discovery
- T1010: Application Window Discovery
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1016.001: Internet Connection Discovery
- T1018: Remote System Discovery
- T1021.001: Remote Desktop Protocol
- T1027.002: Software Packing
- T1033: System Owner/User Discovery
- T1036.005: Match Legitimate Resource Name or Location
- T1036.008: Masquerade File Type
- T1046: Network Service Discovery
- T1047: Windows Management Instrumentation
- T1049: System Network Connections Discovery
- T1056.001: Keylogging
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.004: Unix Shell
- T1068: Exploitation for Privilege Escalation
- T1069: Permission Groups Discovery
- T1069.001: Local Groups
- T1069.002: Domain Groups
- T1070.004: File Deletion
- T1070.007: Clear Network Connection History and Configurations
- T1074: Data Staged
- T1074.001: Local Data Staging
- T1078: Valid Accounts
- T1078.002: Domain Accounts
- T1083: File and Directory Discovery
- T1087.001: Local Account
- T1087.002: Domain Account
- T1090: Proxy
- T1090.001: Internal Proxy
- T1090.003: Multi-hop Proxy
- T1105: Ingress Tool Transfer
- T1112: Modify Registry
- T1113: Screen Capture
- T1120: Peripheral Device Discovery
- T1124: System Time Discovery
- T1133: External Remote Services
- T1140: Deobfuscate/Decode Files or Information
- T1190: Exploit Public-Facing Application
- T1217: Browser Information Discovery
- T1218: System Binary Proxy Execution
- T1497.001: System Checks
- T1505.003: Web Shell
- T1518: Software Discovery
- T1552: Unsecured Credentials
- T1552.004: Private Keys
- T1555: Credentials from Password Stores
- T1555.003: Credentials from Web Browsers
- T1560.001: Archive via Utility
- T1570: Lateral Tool Transfer
- T1573.001: Symmetric Cryptography
- T1584.003: Virtual Private Server
- T1584.004: Server
- T1584.005: Botnet
- T1584.008: Network Devices
- T1587.004: Exploits
- T1588.002: Tool
- T1588.006: Vulnerabilities
- T1589: Gather Victim Identity Information
- T1589.002: Email Addresses
- T1590: Gather Victim Network Information
- T1590.004: Network Topology
- T1590.006: Network Security Appliances
- T1591: Gather Victim Org Information
- T1591.004: Identify Roles
- T1592: Gather Victim Host Information
- T1593: Search Open Websites/Domains
- T1594: Search Victim-Owned Websites
- T1596.005: Scan Databases
- T1614: System Location Discovery
- T1654: Log Enumeration
- T1680: Local Storage Discovery
- T1685.005: Clear Windows Event Logs
