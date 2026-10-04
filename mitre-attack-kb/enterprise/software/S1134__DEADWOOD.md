# S1134: DEADWOOD

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1134  
**Aliases:** DEADWOOD  
**Platforms:** Windows  

## Description
[DEADWOOD](https://attack.mitre.org/software/S1134) is wiper malware written in C++ using Boost libraries. [DEADWOOD](https://attack.mitre.org/software/S1134) was first observed in an unattributed wiping event in Saudi Arabia in 2019, and has since been incorporated into [Agrius](https://attack.mitre.org/groups/G1030) operations.(Citation: SentinelOne Agrius 2021)

## Techniques Used
- T1027.009: Embedded Payloads
- T1027.013: Encrypted/Encoded File
- T1036.004: Masquerade Task or Service
- T1124: System Time Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1485: Data Destruction
- T1531: Account Access Removal
- T1561.001: Disk Content Wipe
- T1561.002: Disk Structure Wipe
- T1569.002: Service Execution
