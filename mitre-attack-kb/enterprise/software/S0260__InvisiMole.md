# S0260: InvisiMole

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0260  
**Aliases:** InvisiMole  
**Platforms:** Windows  

## Description
[InvisiMole](https://attack.mitre.org/software/S0260) is a modular spyware program that has been used by the InvisiMole Group since at least 2013. [InvisiMole](https://attack.mitre.org/software/S0260) has two backdoor modules called RC2FM and RC2CL that are used to perform post-exploitation activities. It has been discovered on compromised victims in the Ukraine and Russia. [Gamaredon Group](https://attack.mitre.org/groups/G0047) infrastructure has been used to download and execute [InvisiMole](https://attack.mitre.org/software/S0260) against a small number of victims.(Citation: ESET InvisiMole June 2018)(Citation: ESET InvisiMole June 2020)

## Techniques Used
- T1001.003: Protocol or Service Impersonation
- T1005: Data from Local System
- T1007: System Service Discovery
- T1008: Fallback Channels
- T1010: Application Window Discovery
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1025: Data from Removable Media
- T1027: Obfuscated Files or Information
- T1027.005: Indicator Removal from Tools
- T1033: System Owner/User Discovery
- T1036.004: Masquerade Task or Service
- T1036.005: Match Legitimate Resource Name or Location
- T1046: Network Service Discovery
- T1053.005: Scheduled Task
- T1055: Process Injection
- T1055.002: Portable Executable Injection
- T1055.004: Asynchronous Procedure Call
- T1055.015: ListPlanting
- T1056.001: Keylogging
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1059.007: JavaScript
- T1068: Exploitation for Privilege Escalation
- T1070.004: File Deletion
- T1070.005: Network Share Connection Removal
- T1070.006: Timestomp
- T1071.001: Web Protocols
- T1071.004: DNS
- T1074.001: Local Data Staging
- T1080: Taint Shared Content
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087.001: Local Account
- T1090.001: Internal Proxy
- T1090.002: External Proxy
- T1095: Non-Application Layer Protocol
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1112: Modify Registry
- T1113: Screen Capture
- T1119: Automated Collection
- T1123: Audio Capture
- T1124: System Time Discovery
- T1125: Video Capture
- T1132.002: Non-Standard Encoding
- T1135: Network Share Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1203: Exploitation for Client Execution
- T1204.002: Malicious File
- T1210: Exploitation of Remote Services
- T1218.002: Control Panel
- T1218.011: Rundll32
- T1480.001: Environmental Keying
- T1490: Inhibit System Recovery
- T1497.001: System Checks
- T1518: Software Discovery
- T1518.001: Security Software Discovery
- T1543.003: Windows Service
- T1547.001: Registry Run Keys / Startup Folder
- T1547.009: Shortcut Modification
- T1548.002: Bypass User Account Control
- T1559.001: Component Object Model
- T1560.001: Archive via Utility
- T1560.002: Archive via Library
- T1560.003: Archive via Custom Method
- T1564.001: Hidden Files and Directories
- T1564.003: Hidden Window
- T1569.002: Service Execution
- T1573.001: Symmetric Cryptography
- T1574.001: DLL
- T1680: Local Storage Discovery
- T1686: Disable or Modify System Firewall
