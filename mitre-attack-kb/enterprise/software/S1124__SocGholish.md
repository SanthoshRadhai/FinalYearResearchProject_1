# S1124: SocGholish

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1124  
**Aliases:** SocGholish, FakeUpdates  
**Platforms:** Windows  

## Description
[SocGholish](https://attack.mitre.org/software/S1124) is a JavaScript-based loader malware that has been used since at least 2017. It has been observed in use against multiple sectors globally for initial access, primarily through drive-by-downloads masquerading as software updates. SocGholish is operated by [Mustard Tempest](https://attack.mitre.org/groups/G1020) and its access has been sold to groups including [Indrik Spider](https://attack.mitre.org/groups/G0119) for downloading secondary RAT and ransomware payloads.(Citation: SentinelOne SocGholish Infrastructure November 2022)(Citation: SocGholish-update)(Citation: Red Canary SocGholish March 2024)(Citation: Secureworks Gold Prelude Profile)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1027.013: Encrypted/Encoded File
- T1027.015: Compression
- T1033: System Owner/User Discovery
- T1036.005: Match Legitimate Resource Name or Location
- T1047: Windows Management Instrumentation
- T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol
- T1057: Process Discovery
- T1059.007: JavaScript
- T1074.001: Local Data Staging
- T1082: System Information Discovery
- T1102: Web Service
- T1105: Ingress Tool Transfer
- T1189: Drive-by Compromise
- T1204.001: Malicious Link
- T1482: Domain Trust Discovery
- T1518: Software Discovery
- T1566.002: Spearphishing Link
- T1614: System Location Discovery
