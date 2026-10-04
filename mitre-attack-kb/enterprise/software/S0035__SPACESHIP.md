# S0035: SPACESHIP

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0035  
**Aliases:** SPACESHIP  
**Platforms:** Windows  

## Description
[SPACESHIP](https://attack.mitre.org/software/S0035) is malware developed by [APT30](https://attack.mitre.org/groups/G0013) that allows propagation and exfiltration of data over removable devices. [APT30](https://attack.mitre.org/groups/G0013) may use this capability to exfiltrate data across air-gaps. (Citation: FireEye APT30)

## Techniques Used
- T1052.001: Exfiltration over USB
- T1074.001: Local Data Staging
- T1083: File and Directory Discovery
- T1547.001: Registry Run Keys / Startup Folder
- T1547.009: Shortcut Modification
- T1560.003: Archive via Custom Method
