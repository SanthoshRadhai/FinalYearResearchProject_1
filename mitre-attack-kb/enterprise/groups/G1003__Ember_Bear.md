# G1003: Ember Bear

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G1003  
**Aliases:** Ember Bear, UNC2589, Bleeding Bear, DEV-0586, Cadet Blizzard, Frozenvista, UAC-0056  

## Description
[Ember Bear](https://attack.mitre.org/groups/G1003) is a Russian state-sponsored cyber espionage group that has been active since at least 2020, linked to Russia's General Staff Main Intelligence Directorate (GRU) 161st Specialist Training Center (Unit 29155).(Citation: CISA GRU29155 2024) [Ember Bear](https://attack.mitre.org/groups/G1003) has primarily focused operations against Ukrainian government and telecommunication entities, but has also operated against critical infrastructure entities in Europe and the Americas.(Citation: Cadet Blizzard emerges as novel threat actor) [Ember Bear](https://attack.mitre.org/groups/G1003) conducted the [WhisperGate](https://attack.mitre.org/software/S0689) destructive wiper attacks against Ukraine in early 2022.(Citation: CrowdStrike Ember Bear Profile March 2022)(Citation: Mandiant UNC2589 March 2022)(Citation: CISA GRU29155 2024) There is some confusion as to whether [Ember Bear](https://attack.mitre.org/groups/G1003) overlaps with another Russian-linked entity referred to as [Saint Bear](https://attack.mitre.org/groups/G1031). At present available evidence strongly suggests these are distinct activities with different behavioral profiles.(Citation: Cadet Blizzard emerges as novel threat actor)(Citation: Palo Alto Unit 42 OutSteel SaintBot February 2022 )

## Techniques Used
- T1003: OS Credential Dumping
- T1003.001: LSASS Memory
- T1003.002: Security Account Manager
- T1003.004: LSA Secrets
- T1005: Data from Local System
- T1018: Remote System Discovery
- T1021: Remote Services
- T1036: Masquerading
- T1036.005: Match Legitimate Resource Name or Location
- T1046: Network Service Discovery
- T1047: Windows Management Instrumentation
- T1053.005: Scheduled Task
- T1059.001: PowerShell
- T1070.004: File Deletion
- T1071.004: DNS
- T1078.001: Default Accounts
- T1090.003: Multi-hop Proxy
- T1095: Non-Application Layer Protocol
- T1110: Brute Force
- T1110.003: Password Spraying
- T1112: Modify Registry
- T1114: Email Collection
- T1119: Automated Collection
- T1125: Video Capture
- T1133: External Remote Services
- T1190: Exploit Public-Facing Application
- T1195: Supply Chain Compromise
- T1203: Exploitation for Client Execution
- T1210: Exploitation of Remote Services
- T1491.002: External Defacement
- T1505.003: Web Shell
- T1550.002: Pass the Hash
- T1552.001: Credentials In Files
- T1560: Archive Collected Data
- T1561.002: Disk Structure Wipe
- T1567.002: Exfiltration to Cloud Storage
- T1570: Lateral Tool Transfer
- T1571: Non-Standard Port
- T1572: Protocol Tunneling
- T1583: Acquire Infrastructure
- T1583.003: Virtual Private Server
- T1585: Establish Accounts
- T1588.001: Malware
- T1588.005: Exploits
- T1595.001: Scanning IP Blocks
- T1595.002: Vulnerability Scanning
- T1654: Log Enumeration
