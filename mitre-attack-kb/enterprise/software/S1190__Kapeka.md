# S1190: Kapeka

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1190  
**Aliases:** Kapeka, KnuckleTouch  
**Platforms:** Windows  

## Description
Kapeka is a backdoor written in C++ used against victims in Eastern Europe since at least mid-2022. Kapeka has technical overlaps with [Exaramel for Windows](https://attack.mitre.org/software/S0343) and [Prestige](https://attack.mitre.org/software/S1058) malware variants, both of which are linked to [Sandworm Team](https://attack.mitre.org/groups/G0034). Kapeka may have been used in advance of [Prestige](https://attack.mitre.org/software/S1058) deployment in late 2022.(Citation: WithSecure Kapeka 2024)(Citation: Microsoft KnuckleTouch 2024)

## Techniques Used
- T1012: Query Registry
- T1027.013: Encrypted/Encoded File
- T1036.008: Masquerade File Type
- T1053.005: Scheduled Task
- T1059.003: Windows Command Shell
- T1070.009: Clear Persistence
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1090: Proxy
- T1106: Native API
- T1112: Modify Registry
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1218.011: Rundll32
