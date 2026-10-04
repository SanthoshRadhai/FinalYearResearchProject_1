# S1133: Apostle

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1133  
**Aliases:** Apostle  
**Platforms:** Windows  

## Description
[Apostle](https://attack.mitre.org/software/S1133) is malware that has functioned as both a wiper and, in more recent versions, as ransomware.  [Apostle](https://attack.mitre.org/software/S1133) is written in .NET and shares various programming and functional overlaps with [IPsec Helper](https://attack.mitre.org/software/S1132).(Citation: SentinelOne Agrius 2021)

## Techniques Used
- T1053.005: Scheduled Task
- T1057: Process Discovery
- T1070.004: File Deletion
- T1140: Deobfuscate/Decode Files or Information
- T1480: Execution Guardrails
- T1485: Data Destruction
- T1486: Data Encrypted for Impact
- T1529: System Shutdown/Reboot
- T1561.001: Disk Content Wipe
- T1685.005: Clear Windows Event Logs
