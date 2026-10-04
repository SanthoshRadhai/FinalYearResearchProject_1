# S0046: CozyCar

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0046  
**Aliases:** CozyCar, CozyDuke, CozyBear, Cozer, EuroAPT  
**Platforms:** Windows  

## Description
[CozyCar](https://attack.mitre.org/software/S0046) is malware that was used by [APT29](https://attack.mitre.org/groups/G0016) from 2010 to 2015. It is a modular malware platform, and its backdoor component can be instructed to download and execute a variety of modules with different functionality. (Citation: F-Secure The Dukes)

## Techniques Used
- T1003.001: LSASS Memory
- T1003.002: Security Account Manager
- T1027.013: Encrypted/Encoded File
- T1036.003: Rename Legitimate Utilities
- T1053.005: Scheduled Task
- T1059.003: Windows Command Shell
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1102.002: Bidirectional Communication
- T1218.011: Rundll32
- T1497: Virtualization/Sandbox Evasion
- T1518.001: Security Software Discovery
- T1543.003: Windows Service
- T1547.001: Registry Run Keys / Startup Folder
