# S0363: Empire

**Type:** tool  
**Reference:** https://attack.mitre.org/software/S0363  
**Aliases:** Empire, EmPyre, PowerShell Empire  
**Platforms:** Linux, macOS, Windows  

## Description
[Empire](https://attack.mitre.org/software/S0363) is an open-source, cross-platform remote administration and post-exploitation framework that is publicly available on GitHub. While the tool itself is primarily written in Python, the post-exploitation agents are written in pure [PowerShell](https://attack.mitre.org/techniques/T1059/001) for Windows and Python for Linux/macOS. [Empire](https://attack.mitre.org/software/S0363) was one of five tools singled out by a joint report on public hacking tools being widely used by adversaries.(Citation: NCSC Joint Report Public Tools)(Citation: Github PowerShell Empire)(Citation: GitHub ATTACK Empire)

## Techniques Used
- T1003.001: LSASS Memory
- T1016: System Network Configuration Discovery
- T1020: Automated Exfiltration
- T1021.003: Distributed Component Object Model
- T1021.004: SSH
- T1027.010: Command Obfuscation
- T1033: System Owner/User Discovery
- T1040: Network Sniffing
- T1041: Exfiltration Over C2 Channel
- T1046: Network Service Discovery
- T1047: Windows Management Instrumentation
- T1049: System Network Connections Discovery
- T1053.005: Scheduled Task
- T1055: Process Injection
- T1056.001: Keylogging
- T1056.004: Credential API Hooking
- T1057: Process Discovery
- T1059: Command and Scripting Interpreter
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1068: Exploitation for Privilege Escalation
- T1070.006: Timestomp
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087.001: Local Account
- T1087.002: Domain Account
- T1102.002: Bidirectional Communication
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1113: Screen Capture
- T1114.001: Local Email Collection
- T1115: Clipboard Data
- T1119: Automated Collection
- T1125: Video Capture
- T1127.001: MSBuild
- T1134: Access Token Manipulation
- T1134.002: Create Process with Token
- T1134.005: SID-History Injection
- T1135: Network Share Discovery
- T1136.001: Local Account
- T1136.002: Domain Account
- T1210: Exploitation of Remote Services
- T1217: Browser Information Discovery
- T1482: Domain Trust Discovery
- T1484.001: Group Policy Modification
- T1518.001: Security Software Discovery
- T1543.003: Windows Service
- T1546.008: Accessibility Features
- T1547.001: Registry Run Keys / Startup Folder
- T1547.005: Security Support Provider
- T1547.009: Shortcut Modification
- T1548.002: Bypass User Account Control
- T1550.002: Pass the Hash
- T1552.001: Credentials In Files
- T1552.004: Private Keys
- T1555.001: Keychain
- T1555.003: Credentials from Web Browsers
- T1557.001: Name Resolution Poisoning and SMB Relay
- T1558.001: Golden Ticket
- T1558.002: Silver Ticket
- T1558.003: Kerberoasting
- T1560: Archive Collected Data
- T1567.001: Exfiltration to Code Repository
- T1567.002: Exfiltration to Cloud Storage
- T1569.002: Service Execution
- T1573.002: Asymmetric Cryptography
- T1574.001: DLL
- T1574.004: Dylib Hijacking
- T1574.007: Path Interception by PATH Environment Variable
- T1574.008: Path Interception by Search Order Hijacking
- T1574.009: Path Interception by Unquoted Path
- T1615: Group Policy Discovery
