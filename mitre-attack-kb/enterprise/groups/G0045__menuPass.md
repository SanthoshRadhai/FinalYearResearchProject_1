# G0045: menuPass

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0045  
**Aliases:** menuPass, Cicada, POTASSIUM, Stone Panda, APT10, Red Apollo, CVNX, HOGFISH, BRONZE RIVERSIDE  

## Description
[menuPass](https://attack.mitre.org/groups/G0045) is a threat group that has been active since at least 2006. Individual members of [menuPass](https://attack.mitre.org/groups/G0045) are known to have acted in association with the Chinese Ministry of State Security's (MSS) Tianjin State Security Bureau and worked for the Huaying Haitai Science and Technology Development Company.(Citation: DOJ APT10 Dec 2018)(Citation: District Court of NY APT10 Indictment December 2018)

[menuPass](https://attack.mitre.org/groups/G0045) has targeted healthcare, defense, aerospace, finance, maritime, biotechnology, energy, and government sectors globally, with an emphasis on Japanese organizations. In 2016 and 2017, the group is known to have targeted managed IT service providers (MSPs), manufacturing and mining companies, and a university.(Citation: Palo Alto menuPass Feb 2017)(Citation: Crowdstrike CrowdCast Oct 2013)(Citation: FireEye Poison Ivy)(Citation: PWC Cloud Hopper April 2017)(Citation: FireEye APT10 April 2017)(Citation: DOJ APT10 Dec 2018)(Citation: District Court of NY APT10 Indictment December 2018)

## Techniques Used
- T1003.002: Security Account Manager
- T1003.003: NTDS
- T1003.004: LSA Secrets
- T1005: Data from Local System
- T1016: System Network Configuration Discovery
- T1018: Remote System Discovery
- T1021.001: Remote Desktop Protocol
- T1021.004: SSH
- T1027.013: Encrypted/Encoded File
- T1036: Masquerading
- T1036.003: Rename Legitimate Utilities
- T1036.005: Match Legitimate Resource Name or Location
- T1039: Data from Network Shared Drive
- T1046: Network Service Discovery
- T1047: Windows Management Instrumentation
- T1049: System Network Connections Discovery
- T1053.005: Scheduled Task
- T1055.012: Process Hollowing
- T1056.001: Keylogging
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1070.003: Clear Command History
- T1070.004: File Deletion
- T1074.001: Local Data Staging
- T1074.002: Remote Data Staging
- T1078: Valid Accounts
- T1083: File and Directory Discovery
- T1087.002: Domain Account
- T1090.002: External Proxy
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1119: Automated Collection
- T1140: Deobfuscate/Decode Files or Information
- T1190: Exploit Public-Facing Application
- T1199: Trusted Relationship
- T1204.002: Malicious File
- T1210: Exploitation of Remote Services
- T1218.004: InstallUtil
- T1553.002: Code Signing
- T1560: Archive Collected Data
- T1560.001: Archive via Utility
- T1566.001: Spearphishing Attachment
- T1568.001: Fast Flux DNS
- T1574.001: DLL
- T1583.001: Domains
- T1588.002: Tool
