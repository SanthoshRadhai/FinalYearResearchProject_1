# S1059: metaMain

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1059  
**Aliases:** metaMain  
**Platforms:** Windows  

## Description
[metaMain](https://attack.mitre.org/software/S1059) is a backdoor used by [Metador](https://attack.mitre.org/groups/G1013) to maintain long-term access to compromised machines; it has also been used to decrypt [Mafalda](https://attack.mitre.org/software/S1060) into memory.(Citation: SentinelLabs Metador Sept 2022)(Citation: SentinelLabs Metador Technical Appendix Sept 2022)

## Techniques Used
- T1005: Data from Local System
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1041: Exfiltration Over C2 Channel
- T1055: Process Injection
- T1056: Input Capture
- T1056.001: Keylogging
- T1057: Process Discovery
- T1070.004: File Deletion
- T1070.006: Timestomp
- T1071.001: Web Protocols
- T1074.001: Local Data Staging
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1090.001: Internal Proxy
- T1095: Non-Application Layer Protocol
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1112: Modify Registry
- T1113: Screen Capture
- T1140: Deobfuscate/Decode Files or Information
- T1205.001: Port Knocking
- T1497.003: Time Based Checks
- T1546.003: Windows Management Instrumentation Event Subscription
- T1560.003: Archive via Custom Method
- T1573.001: Symmetric Cryptography
- T1574.001: DLL
- T1620: Reflective Code Loading
