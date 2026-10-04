# S0256: Mosquito

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0256  
**Aliases:** Mosquito  
**Platforms:** Windows  

## Description
[Mosquito](https://attack.mitre.org/software/S0256) is a Win32 backdoor that has been used by [Turla](https://attack.mitre.org/groups/G0010). [Mosquito](https://attack.mitre.org/software/S0256) is made up of three parts: the installer, the launcher, and the backdoor. The main backdoor is called CommanderDLL and is launched by the loader program. (Citation: ESET Turla Mosquito Jan 2018)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1027.011: Fileless Storage
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1047: Windows Management Instrumentation
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1112: Modify Registry
- T1218.011: Rundll32
- T1518.001: Security Software Discovery
- T1546.015: Component Object Model Hijacking
- T1547.001: Registry Run Keys / Startup Folder
- T1573.001: Symmetric Cryptography
