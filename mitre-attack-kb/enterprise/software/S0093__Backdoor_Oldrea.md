# S0093: Backdoor.Oldrea

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0093  
**Aliases:** Backdoor.Oldrea, Havex  
**Platforms:** Windows  

## Description
[Backdoor.Oldrea](https://attack.mitre.org/software/S0093) is a modular backdoor that used by [Dragonfly](https://attack.mitre.org/groups/G0035) against energy companies since at least 2013. [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) was distributed via supply chain compromise, and included specialized modules to enumerate and map ICS-specific systems, processes, and protocols.(Citation: Symantec Dragonfly)(Citation: Gigamon Berserk Bear October 2021)(Citation: Symantec Dragonfly Sept 2017)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1018: Remote System Discovery
- T1033: System Owner/User Discovery
- T1046: Network Service Discovery
- T1055: Process Injection
- T1057: Process Discovery
- T1070.004: File Deletion
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087.003: Email Account
- T1105: Ingress Tool Transfer
- T1132.001: Standard Encoding
- T1218.011: Rundll32
- T1547.001: Registry Run Keys / Startup Folder
- T1555.003: Credentials from Web Browsers
- T1560: Archive Collected Data
