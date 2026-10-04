# S9022: MirrorStealer

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9022  
**Aliases:** MirrorStealer  
**Platforms:** Windows  

## Description
[MirrorStealer](https://attack.mitre.org/software/S9022) is a credential stealer that has been used by [MirrorFace](https://attack.mitre.org/groups/G1054) since at least 2022 to steal credentials from various applications, including browsers and email clients. [MirrorStealer](https://attack.mitre.org/software/S9022) has been delivered directly into system memory via commands issued by [LODEINFO](https://attack.mitre.org/software/S9020).(Citation: ESET MirrorFace DEC 2022)

## Techniques Used
- T1074.001: Local Data Staging
- T1552.006: Group Policy Preferences
- T1555: Credentials from Password Stores
- T1555.003: Credentials from Web Browsers
