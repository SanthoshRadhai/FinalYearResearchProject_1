# S0505: Desert Scorpion

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0505  
**Aliases:** Desert Scorpion  
**Platforms:** Android  

## Description
[Desert Scorpion](https://attack.mitre.org/software/S0505) is surveillanceware that has targeted the Middle East, specifically individuals located in Palestine. [Desert Scorpion](https://attack.mitre.org/software/S0505) is suspected to have been operated by the threat actor [APT-C-23](https://attack.mitre.org/groups/G1028).(Citation: Lookout Desert Scorpion) 

There are multiple close variants of [Desert Scorpion](https://attack.mitre.org/software/S0505), such as VAMP(Citation: Unit42 VAMP 2017), GnatSpy(Citation: Trendmicro GnatSpy 2017), [FrozenCell](https://attack.mitre.org/software/S0577) and [SpyC23](https://attack.mitre.org/software/S1195), which add some additional functionality but are not significantly different from the original malware.

## Techniques Used
- T1407: Download New Code at Runtime
- T1409: Stored Application Data
- T1418: Software Discovery
- T1420: File and Directory Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1512: Video Capture
- T1532: Archive Collected Data
- T1533: Data from Local System
- T1582: SMS Control
- T1628.001: Suppress Application Icon
- T1630.002: File Deletion
- T1632.001: Code Signing Policy Modification
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1644: Out of Band Data
