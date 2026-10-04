# S0397: LoJax

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0397  
**Aliases:** LoJax  
**Platforms:** Windows  

## Description
[LoJax](https://attack.mitre.org/software/S0397) is a UEFI rootkit used by [APT28](https://attack.mitre.org/groups/G0007) to persist remote access software on targeted systems.(Citation: ESET LoJax Sept 2018)

## Techniques Used
- T1014: Rootkit
- T1112: Modify Registry
- T1542.001: System Firmware
- T1547.001: Registry Run Keys / Startup Folder
- T1564.004: NTFS File Attributes
