# S1042: SUGARDUMP

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1042  
**Aliases:** SUGARDUMP  
**Platforms:** Windows  

## Description
[SUGARDUMP](https://attack.mitre.org/software/S1042) is a proprietary browser credential harvesting tool that was used by UNC3890 during the [C0010](https://attack.mitre.org/campaigns/C0010) campaign. The first known [SUGARDUMP](https://attack.mitre.org/software/S1042) version was used since at least early 2021, a second SMTP C2 version was used from late 2021-early 2022, and a third HTTP C2 variant was used since at least April 2022.(Citation: Mandiant UNC3890 Aug 2022)

## Techniques Used
- T1036.004: Masquerade Task or Service
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1053.005: Scheduled Task
- T1071.001: Web Protocols
- T1071.003: Mail Protocols
- T1074.001: Local Data Staging
- T1083: File and Directory Discovery
- T1204.002: Malicious File
- T1217: Browser Information Discovery
- T1518: Software Discovery
- T1555.003: Credentials from Web Browsers
- T1560.003: Archive via Custom Method
