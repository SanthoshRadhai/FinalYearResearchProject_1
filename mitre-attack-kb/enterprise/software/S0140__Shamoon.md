# S0140: Shamoon

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0140  
**Aliases:** Shamoon, Disttrack  
**Platforms:** Windows  

## Description
[Shamoon](https://attack.mitre.org/software/S0140) is wiper malware that was first used by an Iranian group known as the "Cutting Sword of Justice" in 2012. Other versions known as Shamoon 2 and Shamoon 3 were observed in 2016 and 2018. [Shamoon](https://attack.mitre.org/software/S0140) has also been seen leveraging [RawDisk](https://attack.mitre.org/software/S0364) and Filerase to carry out data wiping tasks. Analysis has linked [Shamoon](https://attack.mitre.org/software/S0140) with [Kwampirs](https://attack.mitre.org/software/S0236) based on multiple shared artifacts and coding patterns.(Citation: Cylera Kwampirs 2022) The term Shamoon is sometimes used to refer to the group using the malware as well as the malware itself.(Citation: Palo Alto Shamoon Nov 2016)(Citation: Unit 42 Shamoon3 2018)(Citation: Symantec Shamoon 2012)(Citation: FireEye Shamoon Nov 2016)

## Techniques Used
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1018: Remote System Discovery
- T1021.002: SMB/Windows Admin Shares
- T1027: Obfuscated Files or Information
- T1036.004: Masquerade Task or Service
- T1053.005: Scheduled Task
- T1070.006: Timestomp
- T1071.001: Web Protocols
- T1078.002: Domain Accounts
- T1082: System Information Discovery
- T1105: Ingress Tool Transfer
- T1112: Modify Registry
- T1124: System Time Discovery
- T1134.001: Token Impersonation/Theft
- T1140: Deobfuscate/Decode Files or Information
- T1485: Data Destruction
- T1486: Data Encrypted for Impact
- T1529: System Shutdown/Reboot
- T1543.003: Windows Service
- T1548.002: Bypass User Account Control
- T1561.002: Disk Structure Wipe
- T1569.002: Service Execution
- T1570: Lateral Tool Transfer
