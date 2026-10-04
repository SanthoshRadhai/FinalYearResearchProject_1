# S1241: RatMilad

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1241  
**Aliases:** RatMilad  
**Platforms:** Android  

## Description
[RatMilad](https://attack.mitre.org/software/S1241) is an Android remote access tool (RAT) with spyware functionality that has been used to target enterprise mobile devices in the Middle East since at least 2021. Variants of [RatMilad](https://attack.mitre.org/software/S1241) have been disguised as VPN applications and a fake app named NumRent. Upon installation, [RatMilad](https://attack.mitre.org/software/S1241) employs multiple [Collection](https://attack.mitre.org/tactics/TA0035) techniques to collect sensitive information before uploading the collected data to its command and control (C2) server. (Citation: ZimperiumGupta_RatMilad_Oct2022)

## Techniques Used
- T1407: Download New Code at Runtime
- T1414: Clipboard Data
- T1418: Software Discovery
- T1420: File and Directory Discovery
- T1422: System Network Configuration Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1437.001: Web Protocols
- T1512: Video Capture
- T1533: Data from Local System
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1636.005: Accounts
- T1646: Exfiltration Over C2 Channel
- T1660: Phishing
- T1662: Data Destruction
