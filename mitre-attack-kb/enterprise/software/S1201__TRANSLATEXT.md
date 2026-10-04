# S1201: TRANSLATEXT

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1201  
**Aliases:** TRANSLATEXT  
**Platforms:** Windows  

## Description
[TRANSLATEXT](https://attack.mitre.org/software/S1201) is malware that is believed to be used by [Kimsuky](https://attack.mitre.org/groups/G0094).(Citation: Zscaler Kimsuky TRANSLATEXT) [TRANSLATEXT](https://attack.mitre.org/software/S1201) masqueraded as a Google Translate extension for Google Chrome, but is actually a collection of four malicious Javascript files that perform defense evasion, information collection and exfiltration.(Citation: Zscaler Kimsuky TRANSLATEXT)

## Techniques Used
- T1012: Query Registry
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1059.001: PowerShell
- T1071.001: Web Protocols
- T1102.001: Dead Drop Resolver
- T1102.002: Bidirectional Communication
- T1112: Modify Registry
- T1113: Screen Capture
- T1114: Email Collection
- T1176.001: Browser Extensions
- T1185: Browser Session Hijacking
- T1205: Traffic Signaling
- T1539: Steal Web Session Cookie
- T1555.003: Credentials from Web Browsers
