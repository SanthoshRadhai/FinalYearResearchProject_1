# G1054: MirrorFace

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G1054  
**Aliases:** MirrorFace, Earth Kasha  

## Description
[MirrorFace](https://attack.mitre.org/groups/G1054) is a People's Republic of China (PRC)-aligned cyberespionage actor believed to be a subgroup under the [menuPass](https://attack.mitre.org/groups/G0045) umbrella based on targeting, tools, and infrastructure overlaps. [MirrorFace](https://attack.mitre.org/groups/G1054) has been active since at least 2019, at first exclusively targeting Japanese organizations across the media, defense, diplomatic, financial, manufacturing, and academic sectors. Subsequent [MirrorFace](https://attack.mitre.org/groups/G1054) operations included targets in Central Europe and featured use of [LODEINFO](https://attack.mitre.org/software/S9020), [HiddenFace](https://attack.mitre.org/software/S9023), and [UPPERCUT](https://attack.mitre.org/software/S0275) malware.(Citation: Kaspersky LODEINFO OCT 2022)(Citation: Kaspersky LODEINFO Part II OCT 2022)(Citation: ESET MirrorFace DEC 2022)(Citation: JPCERT MirrorFace JUL 2024)(Citation: Trend Micro Earth Kasha NOV 2024)(Citation: Trend Micro Earth Kasha Updates APR 2025)

## Techniques Used
- T1003.001: LSASS Memory
- T1003.002: Security Account Manager
- T1003.003: NTDS
- T1005: Data from Local System
- T1007: System Service Discovery
- T1016: System Network Configuration Discovery
- T1018: Remote System Discovery
- T1021.001: Remote Desktop Protocol
- T1021.002: SMB/Windows Admin Shares
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1036.008: Masquerade File Type
- T1047: Windows Management Instrumentation
- T1048.002: Exfiltration Over Asymmetric Encrypted Non-C2 Protocol
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1070.004: File Deletion
- T1071.002: File Transfer Protocols
- T1074.002: Remote Data Staging
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087.002: Domain Account
- T1090: Proxy
- T1114.001: Local Email Collection
- T1190: Exploit Public-Facing Application
- T1204.002: Malicious File
- T1221: Template Injection
- T1482: Domain Trust Discovery
- T1553.002: Code Signing
- T1556.002: Password Filter DLL
- T1560.001: Archive via Utility
- T1566.001: Spearphishing Attachment
- T1566.002: Spearphishing Link
- T1574.001: DLL
- T1587.001: Malware
- T1588.002: Tool
- T1591: Gather Victim Org Information
- T1614.001: System Language Discovery
- T1684.001: Impersonation
- T1685: Disable or Modify Tools
- T1685.005: Clear Windows Event Logs
- T1686.003: Windows Host Firewall
