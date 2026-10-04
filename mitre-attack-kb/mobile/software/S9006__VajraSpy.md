# S9006: VajraSpy

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9006  
**Aliases:** VajraSpy  
**Platforms:** Android  

## Description
[VajraSpy](https://attack.mitre.org/software/S9006) is Android malware distributed via trojanized messaging and news applications. It has been used to target individuals in Pakistan and India since at least 2021 and has been delivered through the Google Play Store, malicious domains, and other uncontrolled distribution channels. [VajraSpy](https://attack.mitre.org/software/S9006) is attributed with high confidence to [Patchwork](https://attack.mitre.org/groups/G0040) which has used the malware to conduct targeted espionage, primarily against devices in Pakistan.(Citation: ESET_VajraSpy_Feb2024)(Citation: ArcticWolf_DroppingElephant_July2025)(Citation: K7Dhanalakshmi_VajraSpy_April2022)

## Techniques Used
- T1409: Stored Application Data
- T1417.001: Keylogging
- T1418: Software Discovery
- T1420: File and Directory Discovery
- T1422.002: Wi-Fi Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1453: Abuse Accessibility Features
- T1461: Lockscreen Bypass
- T1481.002: Bidirectional Communication
- T1512: Video Capture
- T1517: Access Notifications
- T1533: Data from Local System
- T1616: Call Control
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1636.005: Accounts
- T1639.001: Exfiltration Over Unencrypted Non-C2 Protocol
- T1646: Exfiltration Over C2 Channel
- T1655: Masquerading
- T1660: Phishing
