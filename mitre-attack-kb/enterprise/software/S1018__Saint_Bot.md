# S1018: Saint Bot

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1018  
**Aliases:** Saint Bot  
**Platforms:** Windows  

## Description
[Saint Bot](https://attack.mitre.org/software/S1018) is a .NET downloader that has been used by [Saint Bear](https://attack.mitre.org/groups/G1031) since at least March 2021.(Citation: Malwarebytes Saint Bot April 2021)(Citation: Palo Alto Unit 42 OutSteel SaintBot February 2022 )

## Techniques Used
- T1005: Data from Local System
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1027: Obfuscated Files or Information
- T1027.002: Software Packing
- T1033: System Owner/User Discovery
- T1036: Masquerading
- T1036.005: Match Legitimate Resource Name or Location
- T1053.005: Scheduled Task
- T1055.001: Dynamic-link Library Injection
- T1055.004: Asynchronous Procedure Call
- T1055.012: Process Hollowing
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1204.001: Malicious Link
- T1204.002: Malicious File
- T1218.004: InstallUtil
- T1218.010: Regsvr32
- T1497.001: System Checks
- T1497.003: Time Based Checks
- T1547.001: Registry Run Keys / Startup Folder
- T1548.002: Bypass User Account Control
- T1566.001: Spearphishing Attachment
- T1566.002: Spearphishing Link
- T1574: Hijack Execution Flow
- T1614: System Location Discovery
- T1622: Debugger Evasion
