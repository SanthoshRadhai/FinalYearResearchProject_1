# S0665: ThreatNeedle

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0665  
**Aliases:** ThreatNeedle  
**Platforms:** Windows  

## Description
[ThreatNeedle](https://attack.mitre.org/software/S0665) is a backdoor that has been used by [Lazarus Group](https://attack.mitre.org/groups/G0032) since at least 2019 to target cryptocurrency, defense, and mobile gaming organizations.  It is considered to be an advanced cluster of [Lazarus Group](https://attack.mitre.org/groups/G0032)'s Manuscrypt (a.k.a. NukeSped) malware family.(Citation: Kaspersky ThreatNeedle Feb 2021)

## Techniques Used
- T1005: Data from Local System
- T1027.011: Fileless Storage
- T1027.013: Encrypted/Encoded File
- T1027.015: Compression
- T1036.005: Match Legitimate Resource Name or Location
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1112: Modify Registry
- T1140: Deobfuscate/Decode Files or Information
- T1204.002: Malicious File
- T1543.003: Windows Service
- T1547.001: Registry Run Keys / Startup Folder
- T1566.001: Spearphishing Attachment
