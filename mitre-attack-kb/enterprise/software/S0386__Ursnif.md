# S0386: Ursnif

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0386  
**Aliases:** Ursnif, Gozi-ISFB, PE_URSNIF, Dreambot  
**Platforms:** Windows  

## Description
[Ursnif](https://attack.mitre.org/software/S0386) is a banking trojan and variant of the Gozi malware observed being spread through various automated exploit kits, [Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001)s, and malicious links.(Citation: NJCCIC Ursnif Sept 2016)(Citation: ProofPoint Ursnif Aug 2016) [Ursnif](https://attack.mitre.org/software/S0386) is associated primarily with data theft, but variants also include components (backdoors, spyware, file injectors, etc.) capable of a wide variety of behaviors.(Citation: TrendMicro Ursnif Mar 2015)

## Techniques Used
- T1005: Data from Local System
- T1007: System Service Discovery
- T1012: Query Registry
- T1027.010: Command Obfuscation
- T1027.013: Encrypted/Encoded File
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1047: Windows Management Instrumentation
- T1055.005: Thread Local Storage
- T1055.012: Process Hollowing
- T1056.004: Credential API Hooking
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.005: Visual Basic
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1074.001: Local Data Staging
- T1080: Taint Shared Content
- T1082: System Information Discovery
- T1090: Proxy
- T1090.003: Multi-hop Proxy
- T1091: Replication Through Removable Media
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1112: Modify Registry
- T1113: Screen Capture
- T1132: Data Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1185: Browser Session Hijacking
- T1497.003: Time Based Checks
- T1543.003: Windows Service
- T1547.001: Registry Run Keys / Startup Folder
- T1559.001: Component Object Model
- T1564.003: Hidden Window
- T1568.002: Domain Generation Algorithms
