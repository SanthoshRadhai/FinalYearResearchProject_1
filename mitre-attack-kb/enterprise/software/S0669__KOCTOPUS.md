# S0669: KOCTOPUS

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0669  
**Aliases:** KOCTOPUS  
**Platforms:** Windows  

## Description
[KOCTOPUS](https://attack.mitre.org/software/S0669)'s batch variant is loader used by [LazyScripter](https://attack.mitre.org/groups/G0140) since 2018 to launch [Octopus](https://attack.mitre.org/software/S0340) and [Koadic](https://attack.mitre.org/software/S0250) and, in some cases, [QuasarRAT](https://attack.mitre.org/software/S0262). [KOCTOPUS](https://attack.mitre.org/software/S0669) also has a VBA variant that has the same functionality as the batch version.(Citation: MalwareBytes LazyScripter Feb 2021)

## Techniques Used
- T1027.010: Command Obfuscation
- T1036.005: Match Legitimate Resource Name or Location
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1070.009: Clear Persistence
- T1082: System Information Discovery
- T1090: Proxy
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1112: Modify Registry
- T1140: Deobfuscate/Decode Files or Information
- T1204.001: Malicious Link
- T1204.002: Malicious File
- T1547.001: Registry Run Keys / Startup Folder
- T1548.002: Bypass User Account Control
- T1564.003: Hidden Window
- T1566.001: Spearphishing Attachment
- T1566.002: Spearphishing Link
- T1685: Disable or Modify Tools
