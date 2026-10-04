# S1214: Android/SpyAgent

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1214  
**Aliases:** Android/SpyAgent  
**Platforms:** Android  

## Description
[Android/SpyAgent](https://attack.mitre.org/software/S1214) is a variant of spyware in the MoqHao phishing campaign primarily targeting Korean and Japanese users.(Citation: McAfee MoqHao 2019) Fake security applications were used to target Japanese users, while fake police applications were used to target Korean users. Both fake applications have common C2 commands and share the same crash report key on a cloud service.(Citation: McAfee MoqHao 2019)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1422: System Network Configuration Discovery
- T1481: Web Service
- T1481.001: Dead Drop Resolver
- T1616: Call Control
- T1629.003: Disable or Modify Tools
- T1636.004: SMS Messages
- T1655.001: Match Legitimate Name or Location
