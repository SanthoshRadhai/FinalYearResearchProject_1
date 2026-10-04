# S1068: BlackCat

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1068  
**Aliases:** BlackCat, ALPHV, Noberus  
**Platforms:** Linux, Windows  

## Description
[BlackCat](https://attack.mitre.org/software/S1068) is ransomware written in Rust that has been offered via the Ransomware-as-a-Service (RaaS) model. First observed November 2021, [BlackCat](https://attack.mitre.org/software/S1068) has been used to target multiple sectors and organizations in various countries and regions in Africa, the Americas, Asia, Australia, and Europe.(Citation: Microsoft BlackCat Jun 2022)(Citation: Sophos BlackCat Jul 2022)(Citation: ACSC BlackCat Apr 2022)

## Techniques Used
- T1018: Remote System Discovery
- T1033: System Owner/User Discovery
- T1047: Windows Management Instrumentation
- T1059.003: Windows Command Shell
- T1069.002: Domain Groups
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087.002: Domain Account
- T1112: Modify Registry
- T1134: Access Token Manipulation
- T1135: Network Share Discovery
- T1222.001: Windows Permissions
- T1486: Data Encrypted for Impact
- T1489: Service Stop
- T1490: Inhibit System Recovery
- T1491.001: Internal Defacement
- T1548.002: Bypass User Account Control
- T1561.001: Disk Content Wipe
- T1570: Lateral Tool Transfer
- T1680: Local Storage Discovery
- T1685.005: Clear Windows Event Logs
