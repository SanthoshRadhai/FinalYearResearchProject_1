# S1169: Mango

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1169  
**Aliases:** Mango  
**Platforms:** Windows  

## Description
[Mango](https://attack.mitre.org/software/S1169) is a first-stage backdoor written in C#/.NET that was used by [OilRig](https://attack.mitre.org/groups/G0049) during the [Juicy Mix](https://attack.mitre.org/campaigns/C0044) campaign. [Mango](https://attack.mitre.org/software/S1169) is the successor to [Solar](https://attack.mitre.org/software/S1166) and includes additional exfiltration capabilities, the use of native APIs, and added detection evasion code.(Citation: ESET OilRig Campaigns Sep 2023)

## Techniques Used
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1041: Exfiltration Over C2 Channel
- T1053.005: Scheduled Task
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1106: Native API
- T1132.001: Standard Encoding
- T1204.002: Malicious File
- T1573.001: Symmetric Cryptography
- T1573.002: Asymmetric Cryptography
- T1685: Disable or Modify Tools
