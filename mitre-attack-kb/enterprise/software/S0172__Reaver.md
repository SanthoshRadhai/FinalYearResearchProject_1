# S0172: Reaver

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0172  
**Aliases:** Reaver  
**Platforms:** Windows  

## Description
[Reaver](https://attack.mitre.org/software/S0172) is a malware family that has been in the wild since at least late 2016. Reporting indicates victims have primarily been associated with the "Five Poisons," which are movements the Chinese government considers dangerous. The type of malware is rare due to its final payload being in the form of [Control Panel](https://attack.mitre.org/techniques/T1218/002) items.(Citation: Palo Alto Reaver Nov 2017)

## Techniques Used
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1095: Non-Application Layer Protocol
- T1218.002: Control Panel
- T1543.003: Windows Service
- T1547.001: Registry Run Keys / Startup Folder
- T1547.009: Shortcut Modification
- T1560.003: Archive via Custom Method
- T1680: Local Storage Discovery
