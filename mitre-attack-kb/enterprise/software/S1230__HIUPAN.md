# S1230: HIUPAN

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1230  
**Aliases:** HIUPAN  
**Platforms:** Windows  

## Description
[HIUPAN](https://attack.mitre.org/software/S1230) (aka U2DiskWatch) is a is a worm that propagates through removable drives known to be leveraged by [Mustang Panda](https://attack.mitre.org/groups/G0129) and was first observed utilized in 2024. (Citation: 2025_IBM_PUBLOAD_TONESHELL_HIUPAN_CLAIMLOADER_MUSTANG PANDA)(Citation: Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024)

## Techniques Used
- T1057: Process Discovery
- T1091: Replication Through Removable Media
- T1112: Modify Registry
- T1120: Peripheral Device Discovery
- T1204.002: Malicious File
- T1547.001: Registry Run Keys / Startup Folder
- T1564.001: Hidden Files and Directories
- T1574.001: DLL
- T1678: Delay Execution
