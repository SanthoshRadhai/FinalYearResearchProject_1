# S1135: MultiLayer Wiper

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1135  
**Aliases:** MultiLayer Wiper  
**Platforms:** Windows  

## Description
[MultiLayer Wiper](https://attack.mitre.org/software/S1135) is wiper malware written in .NET associated with [Agrius](https://attack.mitre.org/groups/G1030) operations. Observed samples of [MultiLayer Wiper](https://attack.mitre.org/software/S1135) have an anomalous, future compilation date suggesting possible metadata manipulation.(Citation: Unit42 Agrius 2023)

## Techniques Used
- T1027.009: Embedded Payloads
- T1053.005: Scheduled Task
- T1059.003: Windows Command Shell
- T1070: Indicator Removal
- T1070.004: File Deletion
- T1070.006: Timestomp
- T1083: File and Directory Discovery
- T1485: Data Destruction
- T1490: Inhibit System Recovery
- T1529: System Shutdown/Reboot
- T1561.002: Disk Structure Wipe
- T1565.001: Stored Data Manipulation
- T1685: Disable or Modify Tools
- T1685.005: Clear Windows Event Logs
