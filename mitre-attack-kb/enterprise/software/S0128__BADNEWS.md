# S0128: BADNEWS

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0128  
**Aliases:** BADNEWS  
**Platforms:** Windows  

## Description
[BADNEWS](https://attack.mitre.org/software/S0128) is malware that has been used by the actors responsible for the [Patchwork](https://attack.mitre.org/groups/G0040) campaign. Its name was given due to its use of RSS feeds, forums, and blogs for command and control. (Citation: Forcepoint Monsoon) (Citation: TrendMicro Patchwork Dec 2017)

## Techniques Used
- T1005: Data from Local System
- T1025: Data from Removable Media
- T1036.001: Invalid Code Signature
- T1036.005: Match Legitimate Resource Name or Location
- T1039: Data from Network Shared Drive
- T1053.005: Scheduled Task
- T1055.012: Process Hollowing
- T1056.001: Keylogging
- T1059.003: Windows Command Shell
- T1071.001: Web Protocols
- T1074.001: Local Data Staging
- T1083: File and Directory Discovery
- T1102.001: Dead Drop Resolver
- T1102.002: Bidirectional Communication
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1113: Screen Capture
- T1119: Automated Collection
- T1120: Peripheral Device Discovery
- T1132: Data Encoding
- T1132.001: Standard Encoding
- T1547.001: Registry Run Keys / Startup Folder
- T1573.001: Symmetric Cryptography
- T1574.001: DLL
