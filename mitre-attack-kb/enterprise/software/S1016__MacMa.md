# S1016: MacMa

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1016  
**Aliases:** MacMa, OSX.CDDS, DazzleSpy  
**Platforms:** macOS  

## Description
[MacMa](https://attack.mitre.org/software/S1016) is a macOS-based backdoor with a large set of functionalities to control and exfiltrate files from a compromised computer. [MacMa](https://attack.mitre.org/software/S1016) has been observed in the wild since November 2021.(Citation: ESET DazzleSpy Jan 2022) [MacMa](https://attack.mitre.org/software/S1016) shares command and control and unique libraries with [MgBot](https://attack.mitre.org/software/S1146) and [Nightdoor](https://attack.mitre.org/software/S1147), indicating a relationship with the [Daggerfly](https://attack.mitre.org/groups/G1034) threat actor.(Citation: Symantec Daggerfly 2024)

## Techniques Used
- T1005: Data from Local System
- T1016: System Network Configuration Discovery
- T1021: Remote Services
- T1033: System Owner/User Discovery
- T1041: Exfiltration Over C2 Channel
- T1056.001: Keylogging
- T1057: Process Discovery
- T1059.004: Unix Shell
- T1070.004: File Deletion
- T1070.006: Timestomp
- T1074.001: Local Data Staging
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1095: Non-Application Layer Protocol
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1113: Screen Capture
- T1123: Audio Capture
- T1140: Deobfuscate/Decode Files or Information
- T1543.001: Launch Agent
- T1553.001: Gatekeeper Bypass
- T1553.002: Code Signing
- T1555.001: Keychain
- T1571: Non-Standard Port
- T1573: Encrypted Channel
- T1680: Local Storage Discovery
- T1685.006: Clear Linux or Mac System Logs
