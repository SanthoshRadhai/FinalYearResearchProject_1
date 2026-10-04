# S0154: Cobalt Strike

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0154  
**Aliases:** Cobalt Strike  
**Platforms:** Linux, macOS, Windows  

## Description
[Cobalt Strike](https://attack.mitre.org/software/S0154) is a commercial, full-featured, remote access tool that bills itself as “adversary simulation software designed to execute targeted attacks and emulate the post-exploitation actions of advanced threat actors”. Cobalt Strike’s interactive post-exploit capabilities cover the full range of ATT&CK tactics, all executed within a single, integrated system.(Citation: cobaltstrike manual)

In addition to its own capabilities, [Cobalt Strike](https://attack.mitre.org/software/S0154) leverages the capabilities of other well-known tools such as Metasploit and [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: cobaltstrike manual)

## Techniques Used
- T1001.003: Protocol or Service Impersonation
- T1003.001: LSASS Memory
- T1003.002: Security Account Manager
- T1005: Data from Local System
- T1007: System Service Discovery
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1018: Remote System Discovery
- T1021.001: Remote Desktop Protocol
- T1021.002: SMB/Windows Admin Shares
- T1021.003: Distributed Component Object Model
- T1021.004: SSH
- T1021.006: Windows Remote Management
- T1027: Obfuscated Files or Information
- T1027.005: Indicator Removal from Tools
- T1029: Scheduled Transfer
- T1030: Data Transfer Size Limits
- T1046: Network Service Discovery
- T1047: Windows Management Instrumentation
- T1049: System Network Connections Discovery
- T1055: Process Injection
- T1055.001: Dynamic-link Library Injection
- T1055.012: Process Hollowing
- T1056.001: Keylogging
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1059.006: Python
- T1059.007: JavaScript
- T1068: Exploitation for Privilege Escalation
- T1069.001: Local Groups
- T1069.002: Domain Groups
- T1070.006: Timestomp
- T1071.001: Web Protocols
- T1071.002: File Transfer Protocols
- T1071.004: DNS
- T1078.002: Domain Accounts
- T1078.003: Local Accounts
- T1083: File and Directory Discovery
- T1087.002: Domain Account
- T1090.001: Internal Proxy
- T1090.004: Domain Fronting
- T1095: Non-Application Layer Protocol
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1112: Modify Registry
- T1113: Screen Capture
- T1132.001: Standard Encoding
- T1134.001: Token Impersonation/Theft
- T1134.003: Make and Impersonate Token
- T1134.004: Parent PID Spoofing
- T1135: Network Share Discovery
- T1137.001: Office Template Macros
- T1140: Deobfuscate/Decode Files or Information
- T1185: Browser Session Hijacking
- T1197: BITS Jobs
- T1203: Exploitation for Client Execution
- T1218.011: Rundll32
- T1497.002: User Activity Based Checks
- T1518: Software Discovery
- T1543.003: Windows Service
- T1548.002: Bypass User Account Control
- T1548.003: Sudo and Sudo Caching
- T1550.002: Pass the Hash
- T1553.002: Code Signing
- T1564.010: Process Argument Spoofing
- T1569.002: Service Execution
- T1572: Protocol Tunneling
- T1573.001: Symmetric Cryptography
- T1573.002: Asymmetric Cryptography
- T1620: Reflective Code Loading
- T1685: Disable or Modify Tools
