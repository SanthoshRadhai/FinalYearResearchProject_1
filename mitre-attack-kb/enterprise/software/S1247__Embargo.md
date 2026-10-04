# S1247: Embargo

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1247  
**Aliases:** Embargo  
**Platforms:** ESXi, Linux, Windows  

## Description
[Embargo](https://attack.mitre.org/software/S1247) is a ransomware variant written in Rust that has been active since at least May 2024.(Citation: Cyble Embargo Ransomware May 2024)(Citation: ESET Embargo Ransomware October 2024)  [Embargo](https://attack.mitre.org/software/S1247) ransomware operations are associated with “double extortion” ransomware activity, where data is exfiltrated from victim environments prior to encryption, with threats to publish files if a ransom is not paid.(Citation: Cyble Embargo Ransomware May 2024)(Citation: ESET Embargo Ransomware October 2024)  [Embargo](https://attack.mitre.org/software/S1247) ransomware has been known to be delivered through a loader known as MDeployer which also leverages a malware component known as MS4Killer that facilitates termination of processes operating on the victim hosts.(Citation: ESET Embargo Ransomware October 2024) [Embargo](https://attack.mitre.org/software/S1247) is also reportedly a Ransomware as a Service (RaaS).(Citation: ESET Embargo Ransomware October 2024)

## Techniques Used
- T1007: System Service Discovery
- T1027.013: Encrypted/Encoded File
- T1053.005: Scheduled Task
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1068: Exploitation for Privilege Escalation
- T1070.004: File Deletion
- T1083: File and Directory Discovery
- T1106: Native API
- T1112: Modify Registry
- T1135: Network Share Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1480.002: Mutual Exclusion
- T1486: Data Encrypted for Impact
- T1489: Service Stop
- T1490: Inhibit System Recovery
- T1543.003: Windows Service
- T1547.001: Registry Run Keys / Startup Folder
- T1569.002: Service Execution
- T1657: Financial Theft
- T1679: Selective Exclusion
- T1688: Safe Mode Boot
