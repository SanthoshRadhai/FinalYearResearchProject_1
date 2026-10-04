# S0458: Ramsay

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0458  
**Aliases:** Ramsay  
**Platforms:** Windows  

## Description
[Ramsay](https://attack.mitre.org/software/S0458) is an information stealing malware framework designed to collect and exfiltrate sensitive documents, including from air-gapped systems. Researchers have identified overlaps between [Ramsay](https://attack.mitre.org/software/S0458) and the [Darkhotel](https://attack.mitre.org/groups/G0012)-associated Retro malware.(Citation: Eset Ramsay May 2020)(Citation: Antiy CERT Ramsay April 2020)

## Techniques Used
- T1005: Data from Local System
- T1014: Rootkit
- T1016: System Network Configuration Discovery
- T1025: Data from Removable Media
- T1027: Obfuscated Files or Information
- T1027.003: Steganography
- T1036: Masquerading
- T1036.005: Match Legitimate Resource Name or Location
- T1039: Data from Network Shared Drive
- T1046: Network Service Discovery
- T1049: System Network Connections Discovery
- T1053.005: Scheduled Task
- T1055.001: Dynamic-link Library Injection
- T1057: Process Discovery
- T1059.005: Visual Basic
- T1071.001: Web Protocols
- T1074.001: Local Data Staging
- T1080: Taint Shared Content
- T1083: File and Directory Discovery
- T1091: Replication Through Removable Media
- T1106: Native API
- T1113: Screen Capture
- T1119: Automated Collection
- T1120: Peripheral Device Discovery
- T1132.001: Standard Encoding
- T1135: Network Share Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1203: Exploitation for Client Execution
- T1204.002: Malicious File
- T1546.010: AppInit DLLs
- T1547.001: Registry Run Keys / Startup Folder
- T1548.002: Bypass User Account Control
- T1559.001: Component Object Model
- T1559.002: Dynamic Data Exchange
- T1560.001: Archive via Utility
- T1560.003: Archive via Custom Method
- T1566.001: Spearphishing Attachment
- T1574.001: DLL
- T1680: Local Storage Discovery
