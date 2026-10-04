# S1080: Fakecalls

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1080  
**Aliases:** Fakecalls  
**Platforms:** Android  

## Description
[Fakecalls](https://attack.mitre.org/software/S1080) is an Android trojan, first detected in January 2021, that masquerades as South Korean banking apps. It has capabilities to intercept calls to banking institutions and even maintain realistic dialogues with the victim using pre-recorded audio snippets.(Citation: kaspersky_fakecalls_0422)

## Techniques Used
- T1429: Audio Capture
- T1430: Location Tracking
- T1512: Video Capture
- T1533: Data from Local System
- T1616: Call Control
- T1630.002: File Deletion
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1646: Exfiltration Over C2 Channel
- T1655.001: Match Legitimate Name or Location
