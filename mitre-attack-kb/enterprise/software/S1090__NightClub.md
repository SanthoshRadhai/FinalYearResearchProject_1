# S1090: NightClub

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1090  
**Aliases:** NightClub  
**Platforms:** Windows  

## Description
[NightClub](https://attack.mitre.org/software/S1090) is a modular implant written in C++ that has been used by [MoustachedBouncer](https://attack.mitre.org/groups/G1019) since at least 2014.(Citation: MoustachedBouncer ESET August 2023)

## Techniques Used
- T1005: Data from Local System
- T1010: Application Window Discovery
- T1027: Obfuscated Files or Information
- T1036.004: Masquerade Task or Service
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1056.001: Keylogging
- T1057: Process Discovery
- T1070.006: Timestomp
- T1071.003: Mail Protocols
- T1071.004: DNS
- T1074.001: Local Data Staging
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1112: Modify Registry
- T1113: Screen Capture
- T1120: Peripheral Device Discovery
- T1123: Audio Capture
- T1132.002: Non-Standard Encoding
- T1543.003: Windows Service
