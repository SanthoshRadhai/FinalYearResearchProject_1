# S0192: Pupy

**Type:** tool  
**Reference:** https://attack.mitre.org/software/S0192  
**Aliases:** Pupy  
**Platforms:** Linux, Windows, macOS, Android  

## Description
[Pupy](https://attack.mitre.org/software/S0192) is an open source, cross-platform (Windows, Linux, OSX, Android) remote administration and post-exploitation tool. (Citation: GitHub Pupy) It is written in Python and can be generated as a payload in several different ways (Windows exe, Python file, PowerShell oneliner/file, Linux elf, APK, Rubber Ducky, etc.). (Citation: GitHub Pupy) [Pupy](https://attack.mitre.org/software/S0192) is publicly available on GitHub. (Citation: GitHub Pupy)

## Techniques Used
- T1003.001: LSASS Memory
- T1003.004: LSA Secrets
- T1003.005: Cached Domain Credentials
- T1016: System Network Configuration Discovery
- T1021.001: Remote Desktop Protocol
- T1033: System Owner/User Discovery
- T1041: Exfiltration Over C2 Channel
- T1046: Network Service Discovery
- T1049: System Network Connections Discovery
- T1055.001: Dynamic-link Library Injection
- T1056.001: Keylogging
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.006: Python
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087.001: Local Account
- T1105: Ingress Tool Transfer
- T1113: Screen Capture
- T1114.001: Local Email Collection
- T1123: Audio Capture
- T1125: Video Capture
- T1134.001: Token Impersonation/Theft
- T1135: Network Share Discovery
- T1136.001: Local Account
- T1136.002: Domain Account
- T1497.001: System Checks
- T1543.002: Systemd Service
- T1547.001: Registry Run Keys / Startup Folder
- T1547.013: XDG Autostart Entries
- T1548.002: Bypass User Account Control
- T1550.003: Pass the Ticket
- T1552.001: Credentials In Files
- T1555: Credentials from Password Stores
- T1555.003: Credentials from Web Browsers
- T1557.001: Name Resolution Poisoning and SMB Relay
- T1560.001: Archive via Utility
- T1569.002: Service Execution
- T1573.002: Asymmetric Cryptography
- T1685.005: Clear Windows Event Logs
