# S0443: MESSAGETAP

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0443  
**Aliases:** MESSAGETAP  
**Platforms:** Linux  

## Description
[MESSAGETAP](https://attack.mitre.org/software/S0443) is a data mining malware family deployed by [APT41](https://attack.mitre.org/groups/G0096) into telecommunications networks to monitor and save SMS traffic from specific phone numbers, IMSI numbers, or that contain specific keywords. (Citation: FireEye MESSAGETAP October 2019)

## Techniques Used
- T1040: Network Sniffing
- T1049: System Network Connections Discovery
- T1070.004: File Deletion
- T1074.001: Local Data Staging
- T1083: File and Directory Discovery
- T1119: Automated Collection
- T1140: Deobfuscate/Decode Files or Information
- T1560.003: Archive via Custom Method
