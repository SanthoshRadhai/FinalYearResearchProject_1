# G1039: RedCurl

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G1039  
**Aliases:** RedCurl  

## Description
[RedCurl](https://attack.mitre.org/groups/G1039) is a threat actor active since 2018 notable for corporate espionage targeting a variety of locations, including Ukraine, Canada and the United Kingdom, and a variety of industries, including but not limited to travel agencies, insurance companies, and banks.(Citation: group-ib_redcurl1) [RedCurl](https://attack.mitre.org/groups/G1039) is allegedly a Russian-speaking threat actor.(Citation: group-ib_redcurl1)(Citation: group-ib_redcurl2) The group’s operations typically start with spearphishing emails to gain initial access, then the group executes discovery and collection commands and scripts to find corporate data. The group concludes operations by exfiltrating files to the C2 servers.

## Techniques Used
- T1003.001: LSASS Memory
- T1005: Data from Local System
- T1020: Automated Exfiltration
- T1027: Obfuscated Files or Information
- T1036.005: Match Legitimate Resource Name or Location
- T1039: Data from Network Shared Drive
- T1046: Network Service Discovery
- T1053.005: Scheduled Task
- T1056.002: GUI Input Capture
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1059.006: Python
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1080: Taint Shared Content
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087.001: Local Account
- T1087.002: Domain Account
- T1087.003: Email Account
- T1102: Web Service
- T1114.001: Local Email Collection
- T1119: Automated Collection
- T1199: Trusted Relationship
- T1202: Indirect Command Execution
- T1204.001: Malicious Link
- T1204.002: Malicious File
- T1218.011: Rundll32
- T1537: Transfer Data to Cloud Account
- T1547.001: Registry Run Keys / Startup Folder
- T1552.001: Credentials In Files
- T1552.002: Credentials in Registry
- T1555.003: Credentials from Web Browsers
- T1560.001: Archive via Utility
- T1564.001: Hidden Files and Directories
- T1566.001: Spearphishing Attachment
- T1566.002: Spearphishing Link
- T1573.001: Symmetric Cryptography
- T1573.002: Asymmetric Cryptography
- T1587.001: Malware
