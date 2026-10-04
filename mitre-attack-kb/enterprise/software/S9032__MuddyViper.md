# S9032: MuddyViper

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9032  
**Aliases:** MuddyViper  
**Platforms:** Windows  

## Description
[MuddyViper](https://attack.mitre.org/software/S9032) is custom backdoor written in C and C++ used by [MuddyWater](https://attack.mitre.org/groups/G0069) for command and control (C2) communications and persistence. [MuddyViper](https://attack.mitre.org/software/S9032) is loaded by [Fooder](https://attack.mitre.org/software/S9033) and sends frequent messages to the C2 server.(Citation: ESET_MuddyWater_Dec2025)

## Techniques Used
- T1041: Exfiltration Over C2 Channel
- T1053.005: Scheduled Task
- T1056.002: GUI Input Capture
- T1057: Process Discovery
- T1059: Command and Scripting Interpreter
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1071.001: Web Protocols
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1112: Modify Registry
- T1140: Deobfuscate/Decode Files or Information
- T1518.001: Security Software Discovery
- T1547.001: Registry Run Keys / Startup Folder
- T1560: Archive Collected Data
- T1573.001: Symmetric Cryptography
- T1620: Reflective Code Loading
- T1678: Delay Execution
