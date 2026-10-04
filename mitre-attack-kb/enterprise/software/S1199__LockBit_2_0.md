# S1199: LockBit 2.0

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1199  
**Aliases:** LockBit 2.0  
**Platforms:** Windows  

## Description
[LockBit 2.0](https://attack.mitre.org/software/S1199) is an affiliate-based Ransomware-as-a-Service (RaaS) that has been in use since at least June 2021 as the successor to LockBit Ransomware. [LockBit 2.0](https://attack.mitre.org/software/S1199) has versions capable of infecting Windows and VMware ESXi virtual machines, and has been observed targeting multiple industry verticals globally.(Citation: FBI Lockbit 2.0 FEB 2022)(Citation: Palo Alto Lockbit 2.0 JUN 2022)

## Techniques Used
- T1021.002: SMB/Windows Admin Shares
- T1047: Windows Management Instrumentation
- T1053.005: Scheduled Task
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1112: Modify Registry
- T1120: Peripheral Device Discovery
- T1135: Network Share Discovery
- T1136: Create Account
- T1140: Deobfuscate/Decode Files or Information
- T1480: Execution Guardrails
- T1484.001: Group Policy Modification
- T1486: Data Encrypted for Impact
- T1489: Service Stop
- T1490: Inhibit System Recovery
- T1547.001: Registry Run Keys / Startup Folder
- T1548.002: Bypass User Account Control
- T1564.003: Hidden Window
- T1614.001: System Language Discovery
- T1680: Local Storage Discovery
- T1685: Disable or Modify Tools
- T1685.005: Clear Windows Event Logs
