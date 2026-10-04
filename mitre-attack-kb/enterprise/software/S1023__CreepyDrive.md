# S1023: CreepyDrive

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1023  
**Aliases:** CreepyDrive  
**Platforms:** Windows, Office Suite  

## Description
[CreepyDrive](https://attack.mitre.org/software/S1023) is a custom implant has been used by [POLONIUM](https://attack.mitre.org/groups/G1005) since at least early 2022 for C2 with and exfiltration to actor-controlled OneDrive accounts.(Citation: Microsoft POLONIUM June 2022)

[POLONIUM](https://attack.mitre.org/groups/G1005) has used a similar implant called CreepyBox that relies on actor-controlled DropBox accounts.(Citation: Microsoft POLONIUM June 2022)

## Techniques Used
- T1005: Data from Local System
- T1059.001: PowerShell
- T1071.001: Web Protocols
- T1083: File and Directory Discovery
- T1102.002: Bidirectional Communication
- T1105: Ingress Tool Transfer
- T1550.001: Application Access Token
- T1567.002: Exfiltration to Cloud Storage
