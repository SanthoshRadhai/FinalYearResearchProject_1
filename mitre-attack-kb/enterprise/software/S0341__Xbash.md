# S0341: Xbash

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0341  
**Aliases:** Xbash  
**Platforms:** Windows, Linux  

## Description
[Xbash](https://attack.mitre.org/software/S0341) is a malware family that has targeted Linux and Microsoft Windows servers. The malware has been tied to the Iron Group, a threat actor group known for previous ransomware attacks. [Xbash](https://attack.mitre.org/software/S0341) was developed in Python and then converted into a self-contained Linux ELF executable by using PyInstaller.(Citation: Unit42 Xbash Sept 2018)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1046: Network Service Discovery
- T1053.003: Cron
- T1059.001: PowerShell
- T1059.005: Visual Basic
- T1059.007: JavaScript
- T1071.001: Web Protocols
- T1102.001: Dead Drop Resolver
- T1105: Ingress Tool Transfer
- T1110.001: Password Guessing
- T1203: Exploitation for Client Execution
- T1218.005: Mshta
- T1218.010: Regsvr32
- T1485: Data Destruction
- T1486: Data Encrypted for Impact
- T1547.001: Registry Run Keys / Startup Folder
