# S0449: Maze

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0449  
**Aliases:** Maze  
**Platforms:** Windows  

## Description
[Maze](https://attack.mitre.org/software/S0449) ransomware, previously known as "ChaCha", was discovered in May 2019. In addition to encrypting files on victim machines for impact, [Maze](https://attack.mitre.org/software/S0449) operators conduct information stealing campaigns prior to encryption and post the information online to extort affected companies.(Citation: FireEye Maze May 2020)(Citation: McAfee Maze March 2020)(Citation: Sophos Maze VM September 2020)

## Techniques Used
- T1027: Obfuscated Files or Information
- T1027.016: Junk Code Insertion
- T1036.004: Masquerade Task or Service
- T1047: Windows Management Instrumentation
- T1049: System Network Connections Discovery
- T1053.005: Scheduled Task
- T1055.001: Dynamic-link Library Injection
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1070: Indicator Removal
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1106: Native API
- T1218.007: Msiexec
- T1486: Data Encrypted for Impact
- T1489: Service Stop
- T1490: Inhibit System Recovery
- T1529: System Shutdown/Reboot
- T1547.001: Registry Run Keys / Startup Folder
- T1564.006: Run Virtual Instance
- T1568: Dynamic Resolution
- T1614.001: System Language Discovery
- T1685: Disable or Modify Tools
