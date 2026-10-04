# S0448: Rising Sun

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0448  
**Aliases:** Rising Sun  
**Platforms:** Windows  

## Description
[Rising Sun](https://attack.mitre.org/software/S0448) is a modular backdoor that was used extensively in [Operation Sharpshooter](https://attack.mitre.org/campaigns/C0013) between 2017 and 2019. [Rising Sun](https://attack.mitre.org/software/S0448) infected at least 87 organizations around the world, including nuclear, defense, energy, and financial service companies. Security researchers assessed [Rising Sun](https://attack.mitre.org/software/S0448) included some source code from [Lazarus Group](https://attack.mitre.org/groups/G0032)'s Trojan Duuzer.(Citation: McAfee Sharpshooter December 2018)

## Techniques Used
- T1005: Data from Local System
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1016.001: Internet Connection Discovery
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1041: Exfiltration Over C2 Channel
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1070: Indicator Removal
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1106: Native API
- T1140: Deobfuscate/Decode Files or Information
- T1560.003: Archive via Custom Method
- T1564.001: Hidden Files and Directories
- T1573.002: Asymmetric Cryptography
- T1680: Local Storage Discovery
