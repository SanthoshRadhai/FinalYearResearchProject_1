# S0409: Machete

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0409  
**Aliases:** Machete, Pyark  
**Platforms:** Windows  

## Description
[Machete](https://attack.mitre.org/software/S0409) is a cyber espionage toolset used by [Machete](https://attack.mitre.org/groups/G0095). It is a Python-based backdoor targeting Windows machines that was first observed in 2010.(Citation: ESET Machete July 2019)(Citation: Securelist Machete Aug 2014)(Citation: 360 Machete Sep 2020)

## Techniques Used
- T1005: Data from Local System
- T1008: Fallback Channels
- T1010: Application Window Discovery
- T1016: System Network Configuration Discovery
- T1016.002: Wi-Fi Discovery
- T1020: Automated Exfiltration
- T1025: Data from Removable Media
- T1027.002: Software Packing
- T1027.010: Command Obfuscation
- T1029: Scheduled Transfer
- T1036.004: Masquerade Task or Service
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1052.001: Exfiltration over USB
- T1053.005: Scheduled Task
- T1056.001: Keylogging
- T1057: Process Discovery
- T1059.006: Python
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1071.002: File Transfer Protocols
- T1074.001: Local Data Staging
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1113: Screen Capture
- T1115: Clipboard Data
- T1120: Peripheral Device Discovery
- T1123: Audio Capture
- T1125: Video Capture
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1217: Browser Information Discovery
- T1547.001: Registry Run Keys / Startup Folder
- T1552.004: Private Keys
- T1555.003: Credentials from Web Browsers
- T1560: Archive Collected Data
- T1560.003: Archive via Custom Method
- T1564.001: Hidden Files and Directories
- T1573.001: Symmetric Cryptography
- T1573.002: Asymmetric Cryptography
