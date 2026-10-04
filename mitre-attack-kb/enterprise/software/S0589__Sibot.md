# S0589: Sibot

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0589  
**Aliases:** Sibot  
**Platforms:** Windows  

## Description
[Sibot](https://attack.mitre.org/software/S0589) is dual-purpose malware written in VBScript designed to achieve persistence on a compromised system as well as download and execute additional payloads. Microsoft discovered three [Sibot](https://attack.mitre.org/software/S0589) variants in early 2021 during its investigation of [APT29](https://attack.mitre.org/groups/G0016) and the [SolarWinds Compromise](https://attack.mitre.org/campaigns/C0024).(Citation: MSTIC NOBELIUM Mar 2021)

## Techniques Used
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1027.010: Command Obfuscation
- T1027.011: Fileless Storage
- T1036.005: Match Legitimate Resource Name or Location
- T1047: Windows Management Instrumentation
- T1049: System Network Connections Discovery
- T1053.005: Scheduled Task
- T1059.005: Visual Basic
- T1070: Indicator Removal
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1102: Web Service
- T1105: Ingress Tool Transfer
- T1112: Modify Registry
- T1140: Deobfuscate/Decode Files or Information
- T1218.005: Mshta
- T1218.011: Rundll32
