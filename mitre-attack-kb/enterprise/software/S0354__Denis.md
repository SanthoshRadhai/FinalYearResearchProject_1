# S0354: Denis

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0354  
**Aliases:** Denis  
**Platforms:** Windows  

## Description
[Denis](https://attack.mitre.org/software/S0354) is a Windows backdoor and Trojan used by [APT32](https://attack.mitre.org/groups/G0050). [Denis](https://attack.mitre.org/software/S0354) shares several similarities to the [SOUNDBITE](https://attack.mitre.org/software/S0157) backdoor and has been used in conjunction with the [Goopy](https://attack.mitre.org/software/S0477) backdoor.(Citation: Cybereason Oceanlotus May 2017)

## Techniques Used
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1027: Obfuscated Files or Information
- T1027.010: Command Obfuscation
- T1033: System Owner/User Discovery
- T1055.012: Process Hollowing
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1071.004: DNS
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1497.001: System Checks
- T1560.002: Archive via Library
- T1574: Hijack Execution Flow
- T1574.001: DLL
