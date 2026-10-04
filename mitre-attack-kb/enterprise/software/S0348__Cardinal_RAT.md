# S0348: Cardinal RAT

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0348  
**Aliases:** Cardinal RAT  
**Platforms:** Windows  

## Description
[Cardinal RAT](https://attack.mitre.org/software/S0348) is a potentially low volume remote access trojan (RAT) observed since December 2015. [Cardinal RAT](https://attack.mitre.org/software/S0348) is notable for its unique utilization of uncompiled C# source code and the Microsoft Windows built-in csc.exe compiler.(Citation: PaloAlto CardinalRat Apr 2017)

## Techniques Used
- T1008: Fallback Channels
- T1012: Query Registry
- T1027.004: Compile After Delivery
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1055: Process Injection
- T1056.001: Keylogging
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1090: Proxy
- T1105: Ingress Tool Transfer
- T1112: Modify Registry
- T1113: Screen Capture
- T1140: Deobfuscate/Decode Files or Information
- T1204.002: Malicious File
- T1547.001: Registry Run Keys / Startup Folder
- T1560.002: Archive via Library
- T1573.001: Symmetric Cryptography
