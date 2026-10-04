# S1212: RansomHub

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1212  
**Aliases:** RansomHub  
**Platforms:** Linux, Windows  

## Description
[RansomHub](https://attack.mitre.org/software/S1212) is a ransomware-as-a-service (RaaS) offering with Windows, ESXi, Linux, and FreeBSD versions that has been in use since at least 2024 to target organizations in multiple sectors globally. [RansomHub](https://attack.mitre.org/software/S1212) operators may have purchased and rebranded resources from Knight  (formerly Cyclops) Ransomware which shares infrastructure, feature, and code overlaps with [RansomHub](https://attack.mitre.org/software/S1212).(Citation: CISA RansomHub AUG 2024)(Citation: Group-IB RansomHub FEB 2025)

## Techniques Used
- T1018: Remote System Discovery
- T1021.002: SMB/Windows Admin Shares
- T1027.013: Encrypted/Encoded File
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1090: Proxy
- T1135: Network Share Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1480: Execution Guardrails
- T1486: Data Encrypted for Impact
- T1489: Service Stop
- T1490: Inhibit System Recovery
- T1491.001: Internal Defacement
- T1497.003: Time Based Checks
- T1547.001: Registry Run Keys / Startup Folder
- T1685.005: Clear Windows Event Logs
- T1688: Safe Mode Boot
