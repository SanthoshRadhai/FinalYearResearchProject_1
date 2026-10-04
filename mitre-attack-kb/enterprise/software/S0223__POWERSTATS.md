# S0223: POWERSTATS

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0223  
**Aliases:** POWERSTATS, Powermud  
**Platforms:** Windows  

## Description
[POWERSTATS](https://attack.mitre.org/software/S0223) is a PowerShell-based first stage backdoor used by [MuddyWater](https://attack.mitre.org/groups/G0069). (Citation: Unit 42 MuddyWater Nov 2017)

## Techniques Used
- T1005: Data from Local System
- T1016: System Network Configuration Discovery
- T1027.010: Command Obfuscation
- T1027.016: Junk Code Insertion
- T1029: Scheduled Transfer
- T1033: System Owner/User Discovery
- T1036.004: Masquerade Task or Service
- T1047: Windows Management Instrumentation
- T1053.005: Scheduled Task
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.005: Visual Basic
- T1059.007: JavaScript
- T1070.004: File Deletion
- T1082: System Information Discovery
- T1087.001: Local Account
- T1090.002: External Proxy
- T1105: Ingress Tool Transfer
- T1113: Screen Capture
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1218.005: Mshta
- T1518.001: Security Software Discovery
- T1559.001: Component Object Model
- T1559.002: Dynamic Data Exchange
- T1573.002: Asymmetric Cryptography
- T1685: Disable or Modify Tools
