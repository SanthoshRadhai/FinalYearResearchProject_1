# S0596: ShadowPad

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0596  
**Aliases:** ShadowPad, POISONPLUG.SHADOW  
**Platforms:** Windows  

## Description
[ShadowPad](https://attack.mitre.org/software/S0596) is a modular backdoor that was first identified in a supply chain compromise of the NetSarang software in mid-July 2017. The malware was originally thought to be exclusively used by [APT41](https://attack.mitre.org/groups/G0096), but has since been observed to be used by various Chinese threat activity groups. (Citation: Recorded Future RedEcho Feb 2021)(Citation: Securelist ShadowPad Aug 2017)(Citation: Kaspersky ShadowPad Aug 2017)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1027: Obfuscated Files or Information
- T1027.011: Fileless Storage
- T1029: Scheduled Transfer
- T1033: System Owner/User Discovery
- T1055: Process Injection
- T1055.001: Dynamic-link Library Injection
- T1057: Process Discovery
- T1070: Indicator Removal
- T1071.001: Web Protocols
- T1071.002: File Transfer Protocols
- T1071.004: DNS
- T1082: System Information Discovery
- T1095: Non-Application Layer Protocol
- T1105: Ingress Tool Transfer
- T1112: Modify Registry
- T1124: System Time Discovery
- T1132.002: Non-Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1568.002: Domain Generation Algorithms
- T1680: Local Storage Discovery
