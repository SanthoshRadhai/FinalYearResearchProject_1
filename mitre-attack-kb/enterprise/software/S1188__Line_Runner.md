# S1188: Line Runner

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1188  
**Aliases:** Line Runner  
**Platforms:** Network Devices  

## Description
[Line Runner](https://attack.mitre.org/software/S1188) is a persistent backdoor and web shell allowing threat actors to upload and execute arbitrary Lua scripts. [Line Runner](https://attack.mitre.org/software/S1188) is associated with the [ArcaneDoor](https://attack.mitre.org/campaigns/C0046) campaign.(Citation: CCCS ArcaneDoor 2024)(Citation: Cisco ArcaneDoor 2024)

## Techniques Used
- T1027.015: Compression
- T1041: Exfiltration Over C2 Channel
- T1059.011: Lua
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1505.003: Web Shell
- T1557: Adversary-in-the-Middle
- T1653: Power Settings
