# S0036: FLASHFLOOD

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0036  
**Aliases:** FLASHFLOOD  
**Platforms:** Windows  

## Description
[FLASHFLOOD](https://attack.mitre.org/software/S0036) is malware developed by [APT30](https://attack.mitre.org/groups/G0013) that allows propagation and exfiltration of data over removable devices. [APT30](https://attack.mitre.org/groups/G0013) may use this capability to exfiltrate data across air-gaps. (Citation: FireEye APT30)

## Techniques Used
- T1005: Data from Local System
- T1025: Data from Removable Media
- T1074.001: Local Data Staging
- T1083: File and Directory Discovery
- T1547.001: Registry Run Keys / Startup Folder
- T1560.003: Archive via Custom Method
