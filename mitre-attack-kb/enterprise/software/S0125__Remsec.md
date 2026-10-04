# S0125: Remsec

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0125  
**Aliases:** Remsec, Backdoor.Remsec, ProjectSauron  
**Platforms:** Windows  

## Description
[Remsec](https://attack.mitre.org/software/S0125) is a modular backdoor that has been used by [Strider](https://attack.mitre.org/groups/G0041) and appears to have been designed primarily for espionage purposes. Many of its modules are written in Lua. (Citation: Symantec Strider Blog)

## Techniques Used
- T1003.002: Security Account Manager
- T1016: System Network Configuration Discovery
- T1018: Remote System Discovery
- T1025: Data from Removable Media
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1036.005: Match Legitimate Resource Name or Location
- T1046: Network Service Discovery
- T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol
- T1049: System Network Connections Discovery
- T1052.001: Exfiltration over USB
- T1053.005: Scheduled Task
- T1055.001: Dynamic-link Library Injection
- T1056.001: Keylogging
- T1057: Process Discovery
- T1059.011: Lua
- T1068: Exploitation for Privilege Escalation
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1071.003: Mail Protocols
- T1071.004: DNS
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087.001: Local Account
- T1095: Non-Application Layer Protocol
- T1105: Ingress Tool Transfer
- T1518.001: Security Software Discovery
- T1556.002: Password Filter DLL
- T1652: Device Driver Discovery
- T1686.003: Windows Host Firewall
