# S0444: ShimRat

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0444  
**Aliases:** ShimRat  
**Platforms:** Windows  

## Description
[ShimRat](https://attack.mitre.org/software/S0444) has been used by the suspected China-based adversary [Mofang](https://attack.mitre.org/groups/G0103) in campaigns targeting multiple countries and sectors including government, military, critical infrastructure, automobile, and weapons development. The name "[ShimRat](https://attack.mitre.org/software/S0444)" comes from the malware's extensive use of Windows Application Shimming to maintain persistence. (Citation: FOX-IT May 2016 Mofang)

## Techniques Used
- T1005: Data from Local System
- T1008: Fallback Channels
- T1027.002: Software Packing
- T1027.015: Compression
- T1029: Scheduled Transfer
- T1036.004: Masquerade Task or Service
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1083: File and Directory Discovery
- T1090.002: External Proxy
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1112: Modify Registry
- T1135: Network Share Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1543.003: Windows Service
- T1546.011: Application Shimming
- T1547.001: Registry Run Keys / Startup Folder
- T1548.002: Bypass User Account Control
- T1574: Hijack Execution Flow
