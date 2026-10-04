# S0697: HermeticWiper

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0697  
**Aliases:** HermeticWiper, Trojan.Killdisk, DriveSlayer  
**Platforms:** Windows  

## Description
[HermeticWiper](https://attack.mitre.org/software/S0697) is a data wiper that has been used since at least early 2022, primarily against Ukraine with additional activity observed in Latvia and Lithuania. Some sectors targeted include government, financial, defense, aviation, and IT services.(Citation: SentinelOne Hermetic Wiper February 2022)(Citation: Symantec Ukraine Wipers February 2022)(Citation: Crowdstrike DriveSlayer February 2022)(Citation: ESET Hermetic Wiper February 2022)(Citation: Qualys Hermetic Wiper March 2022)

## Techniques Used
- T1027.015: Compression
- T1036.005: Match Legitimate Resource Name or Location
- T1053.005: Scheduled Task
- T1059.003: Windows Command Shell
- T1070: Indicator Removal
- T1070.004: File Deletion
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1106: Native API
- T1112: Modify Registry
- T1134: Access Token Manipulation
- T1140: Deobfuscate/Decode Files or Information
- T1484.001: Group Policy Modification
- T1485: Data Destruction
- T1489: Service Stop
- T1490: Inhibit System Recovery
- T1497.003: Time Based Checks
- T1529: System Shutdown/Reboot
- T1543.003: Windows Service
- T1553.002: Code Signing
- T1561.001: Disk Content Wipe
- T1561.002: Disk Structure Wipe
- T1569.002: Service Execution
- T1680: Local Storage Discovery
- T1685: Disable or Modify Tools
- T1685.005: Clear Windows Event Logs
