# S0136: USBStealer

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0136  
**Aliases:** USBStealer, USB Stealer, Win32/USBStealer  
**Platforms:** Windows  

## Description
[USBStealer](https://attack.mitre.org/software/S0136) is malware that has been used by [APT28](https://attack.mitre.org/groups/G0007) since at least 2005 to extract information from air-gapped networks. It does not have the capability to communicate over the Internet and has been used in conjunction with [ADVSTORESHELL](https://attack.mitre.org/software/S0045). (Citation: ESET Sednit USBStealer 2014) (Citation: Kaspersky Sofacy)

## Techniques Used
- T1020: Automated Exfiltration
- T1025: Data from Removable Media
- T1027.013: Encrypted/Encoded File
- T1036.005: Match Legitimate Resource Name or Location
- T1052.001: Exfiltration over USB
- T1070.004: File Deletion
- T1070.006: Timestomp
- T1074.001: Local Data Staging
- T1083: File and Directory Discovery
- T1091: Replication Through Removable Media
- T1092: Communication Through Removable Media
- T1119: Automated Collection
- T1120: Peripheral Device Discovery
- T1547.001: Registry Run Keys / Startup Folder
