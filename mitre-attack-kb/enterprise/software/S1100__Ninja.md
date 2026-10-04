# S1100: Ninja

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1100  
**Aliases:** Ninja  
**Platforms:** Windows  

## Description
[Ninja](https://attack.mitre.org/software/S1100) is a malware developed in C++ that has been used by [ToddyCat](https://attack.mitre.org/groups/G1022) to penetrate networks and control remote systems since at least 2020.  [Ninja](https://attack.mitre.org/software/S1100) is possibly part of a post exploitation toolkit exclusively used by [ToddyCat](https://attack.mitre.org/groups/G1022) and allows multiple operators to work simultaneously on the same machine. [Ninja](https://attack.mitre.org/software/S1100) has been used against government and military entities in Europe and Asia and observed in specific infection chains being deployed by [Samurai](https://attack.mitre.org/software/S1099).(Citation: Kaspersky ToddyCat June 2022)

## Techniques Used
- T1001: Data Obfuscation
- T1001.003: Protocol or Service Impersonation
- T1016: System Network Configuration Discovery
- T1027.013: Encrypted/Encoded File
- T1027.015: Compression
- T1029: Scheduled Transfer
- T1036.005: Match Legitimate Resource Name or Location
- T1055: Process Injection
- T1057: Process Discovery
- T1070.006: Timestomp
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1090.001: Internal Proxy
- T1090.003: Multi-hop Proxy
- T1095: Non-Application Layer Protocol
- T1106: Native API
- T1132.002: Non-Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1204.002: Malicious File
- T1218.011: Rundll32
- T1480.001: Environmental Keying
- T1543.003: Windows Service
- T1559: Inter-Process Communication
- T1566.003: Spearphishing via Service
- T1573.001: Symmetric Cryptography
- T1574.001: DLL
- T1680: Local Storage Discovery
