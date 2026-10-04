# S0226: Smoke Loader

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0226  
**Aliases:** Smoke Loader, Dofoil  
**Platforms:** Windows  

## Description
[Smoke Loader](https://attack.mitre.org/software/S0226) is a malicious bot application that can be used to load other malware.
[Smoke Loader](https://attack.mitre.org/software/S0226) has been seen in the wild since at least 2011 and has included a number of different payloads. It is notorious for its use of deception and self-protection. It also comes with several plug-ins. (Citation: Malwarebytes SmokeLoader 2016) (Citation: Microsoft Dofoil 2018)

## Techniques Used
- T1027.013: Encrypted/Encoded File
- T1053.005: Scheduled Task
- T1055: Process Injection
- T1055.012: Process Hollowing
- T1059.005: Visual Basic
- T1071.001: Web Protocols
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1114.001: Local Email Collection
- T1140: Deobfuscate/Decode Files or Information
- T1497.001: System Checks
- T1547.001: Registry Run Keys / Startup Folder
- T1552.001: Credentials In Files
- T1555.003: Credentials from Web Browsers
