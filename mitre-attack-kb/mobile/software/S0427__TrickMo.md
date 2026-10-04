# S0427: TrickMo

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0427  
**Aliases:** TrickMo  
**Platforms:** Android  

## Description
[TrickMo](https://attack.mitre.org/software/S0427) a 2FA bypass mobile banking trojan, most likely being distributed by [TrickBot](https://attack.mitre.org/software/S0266). [TrickMo](https://attack.mitre.org/software/S0427) has been primarily targeting users located in Germany.(Citation: SecurityIntelligence TrickMo)

[TrickMo](https://attack.mitre.org/software/S0427) is designed to steal transaction authorization numbers (TANs), which are typically used as one-time passwords.(Citation: SecurityIntelligence TrickMo)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1418: Software Discovery
- T1422: System Network Configuration Discovery
- T1422.001: Internet Connection Discovery
- T1422.002: Wi-Fi Discovery
- T1426: System Information Discovery
- T1437.001: Web Protocols
- T1513: Screen Capture
- T1516: Input Injection
- T1533: Data from Local System
- T1582: SMS Control
- T1624.001: Broadcast Receivers
- T1629.002: Device Lockout
- T1630.001: Uninstall Malicious Application
- T1633.001: System Checks
- T1636.004: SMS Messages
- T1644: Out of Band Data
