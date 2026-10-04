# S0028: SHIPSHAPE

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0028  
**Aliases:** SHIPSHAPE  

## Description
[SHIPSHAPE](https://attack.mitre.org/software/S0028) is malware developed by [APT30](https://attack.mitre.org/groups/G0013) that allows propagation and exfiltration of data over removable devices. [APT30](https://attack.mitre.org/groups/G0013) may use this capability to exfiltrate data across air-gaps. (Citation: FireEye APT30)

## Techniques Used
- T1091: Replication Through Removable Media
- T1547.001: Registry Run Keys / Startup Folder
- T1547.009: Shortcut Modification
