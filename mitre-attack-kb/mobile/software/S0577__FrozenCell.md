# S0577: FrozenCell

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0577  
**Aliases:** FrozenCell  
**Platforms:** Android  

## Description
[FrozenCell](https://attack.mitre.org/software/S0577) is the mobile component of a family of surveillanceware, with a corresponding desktop component known as KasperAgent and [Micropsia](https://attack.mitre.org/software/S0339).(Citation: Lookout FrozenCell) 

There are multiple close variants of [FrozenCell](https://attack.mitre.org/software/S0577), such as VAMP(Citation: Unit42 VAMP 2017), GnatSpy(Citation: Trendmicro GnatSpy 2017), [Desert Scorpion](https://attack.mitre.org/software/S0505) and [SpyC23](https://attack.mitre.org/software/S1195), which add some additional functionality but are not significantly different from the original malware.

## Techniques Used
- T1407: Download New Code at Runtime
- T1409: Stored Application Data
- T1420: File and Directory Discovery
- T1422: System Network Configuration Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1532: Archive Collected Data
- T1533: Data from Local System
- T1636.004: SMS Messages
- T1655.001: Match Legitimate Name or Location
