# S0378: PoshC2

**Type:** tool  
**Reference:** https://attack.mitre.org/software/S0378  
**Aliases:** PoshC2  
**Platforms:** Windows, Linux, macOS  

## Description
[PoshC2](https://attack.mitre.org/software/S0378) is an open source remote administration and post-exploitation framework that is publicly available on GitHub. The server-side components of the tool are primarily written in Python, while the implants are written in [PowerShell](https://attack.mitre.org/techniques/T1059/001). Although [PoshC2](https://attack.mitre.org/software/S0378) is primarily focused on Windows implantation, it does contain a basic Python dropper for Linux/macOS.(Citation: GitHub PoshC2)

## Techniques Used
- T1003.001: LSASS Memory
- T1007: System Service Discovery
- T1016: System Network Configuration Discovery
- T1040: Network Sniffing
- T1046: Network Service Discovery
- T1047: Windows Management Instrumentation
- T1049: System Network Connections Discovery
- T1055: Process Injection
- T1056.001: Keylogging
- T1068: Exploitation for Privilege Escalation
- T1069.001: Local Groups
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087.001: Local Account
- T1087.002: Domain Account
- T1090: Proxy
- T1110: Brute Force
- T1119: Automated Collection
- T1134: Access Token Manipulation
- T1134.002: Create Process with Token
- T1201: Password Policy Discovery
- T1210: Exploitation of Remote Services
- T1482: Domain Trust Discovery
- T1546.003: Windows Management Instrumentation Event Subscription
- T1548.002: Bypass User Account Control
- T1550.002: Pass the Hash
- T1552.001: Credentials In Files
- T1555: Credentials from Password Stores
- T1557.001: Name Resolution Poisoning and SMB Relay
- T1560.001: Archive via Utility
- T1569.002: Service Execution
