# S0513: LiteDuke

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0513  
**Aliases:** LiteDuke  
**Platforms:** Windows  

## Description
[LiteDuke](https://attack.mitre.org/software/S0513) is a third stage backdoor that was used by [APT29](https://attack.mitre.org/groups/G0016), primarily in 2014-2015. [LiteDuke](https://attack.mitre.org/software/S0513) used the same dropper as [PolyglotDuke](https://attack.mitre.org/software/S0518), and was found on machines also compromised by [MiniDuke](https://attack.mitre.org/software/S0051).(Citation: ESET Dukes October 2019)

## Techniques Used
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1027.002: Software Packing
- T1027.003: Steganography
- T1033: System Owner/User Discovery
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1105: Ingress Tool Transfer
- T1140: Deobfuscate/Decode Files or Information
- T1497.003: Time Based Checks
- T1518.001: Security Software Discovery
- T1547.001: Registry Run Keys / Startup Folder
