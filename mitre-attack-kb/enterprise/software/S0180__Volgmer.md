# S0180: Volgmer

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0180  
**Aliases:** Volgmer  
**Platforms:** Windows  

## Description
[Volgmer](https://attack.mitre.org/software/S0180) is a backdoor Trojan designed to provide covert access to a compromised system. It has been used since at least 2013 to target the government, financial, automotive, and media industries. Its primary delivery mechanism is suspected to be spearphishing. (Citation: US-CERT Volgmer Nov 2017)

## Techniques Used
- T1007: System Service Discovery
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1027.011: Fileless Storage
- T1027.013: Encrypted/Encoded File
- T1036.004: Masquerade Task or Service
- T1049: System Network Connections Discovery
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1112: Modify Registry
- T1140: Deobfuscate/Decode Files or Information
- T1543.003: Windows Service
- T1573.001: Symmetric Cryptography
- T1573.002: Asymmetric Cryptography
