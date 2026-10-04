# S1236: CLAIMLOADER

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1236  
**Aliases:** CLAIMLOADER  
**Platforms:** Windows  

## Description
[CLAIMLOADER](https://attack.mitre.org/software/S1236) is a malware variant that frequently accompanies legitimate executables that are used for DLL side-loading known to be leveraged by [Mustang Panda](https://attack.mitre.org/groups/G0129) and was first observed utilized in 2021.(Citation: IBM MUSTANG PANDA PUBLOAD CLAIMLOADER JUNE 2025)(Citation: 2025_IBM_PUBLOAD_TONESHELL_HIUPAN_CLAIMLOADER_MUSTANG PANDA)

## Techniques Used
- T1027.007: Dynamic API Resolution
- T1036.005: Match Legitimate Resource Name or Location
- T1053.005: Scheduled Task
- T1106: Native API
- T1140: Deobfuscate/Decode Files or Information
- T1204.002: Malicious File
- T1480.002: Mutual Exclusion
- T1547.001: Registry Run Keys / Startup Folder
- T1559.001: Component Object Model
- T1564.001: Hidden Files and Directories
- T1574.001: DLL
