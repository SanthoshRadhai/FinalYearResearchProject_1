# S9005: DocSwap

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9005  
**Aliases:** DocSwap  
**Platforms:** Android  

## Description
[DocSwap](https://attack.mitre.org/software/S9005) is an Android malware first identified in 2025, and attributed to [Kimsuky](https://attack.mitre.org/groups/G0094). [DocSwap](https://attack.mitre.org/software/S9005)’s name is a combination of its Korean name “문서열람 인증 앱” (Document Viewing Authentication App) and a phishing page masquerading as CoinSwap at the C2 address. Based on [DocSwap](https://attack.mitre.org/software/S9005)’s name and Korean-language strings, [DocSwap](https://attack.mitre.org/software/S9005) potentially targets mobile device users in South Korea. Several variants of [DocSwap](https://attack.mitre.org/software/S9005) exist; one of the latest samples indicates that the adversary added a native decryption function that decrypts an internal APK.(Citation: EnkiWhiteHat_KimsukyDOCSWAP_Dec2025)(Citation: S2W_DocSwap_Mar2025)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1417.001: Keylogging
- T1418: Software Discovery
- T1420: File and Directory Discovery
- T1422: System Network Configuration Discovery
- T1422.002: Wi-Fi Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1437.001: Web Protocols
- T1453: Abuse Accessibility Features
- T1512: Video Capture
- T1533: Data from Local System
- T1541: Foreground Persistence
- T1544: Ingress Tool Transfer
- T1575: Native API
- T1616: Call Control
- T1624.001: Broadcast Receivers
- T1627: Execution Guardrails
- T1630.002: File Deletion
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1636.005: Accounts
- T1646: Exfiltration Over C2 Channel
- T1655.001: Match Legitimate Name or Location
- T1660: Phishing
