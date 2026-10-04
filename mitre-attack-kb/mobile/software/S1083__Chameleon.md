# S1083: Chameleon

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1083  
**Aliases:** Chameleon  
**Platforms:** Android  

## Description
[Chameleon](https://attack.mitre.org/software/S1083) is an Android banking trojan that can leverage Android’s Accessibility Services to perform malicious activities. Believed to have been first active in January 2023, [Chameleon](https://attack.mitre.org/software/S1083) has been observed targeting users in Australia and Poland by masquerading as official applications. A new variant of [Chameleon](https://attack.mitre.org/software/S1083) has expanded its targets to include Android users in the United Kingdom and Italy.(Citation: cyble_chameleon_0423)(Citation: ThreatFabric_Chameleon_Dec2023)

## Techniques Used
- T1407: Download New Code at Runtime
- T1417.001: Keylogging
- T1417.002: GUI Input Capture
- T1418: Software Discovery
- T1426: System Information Discovery
- T1430: Location Tracking
- T1437: Application Layer Protocol
- T1437.001: Web Protocols
- T1453: Abuse Accessibility Features
- T1461: Lockscreen Bypass
- T1509: Non-Standard Port
- T1513: Screen Capture
- T1517: Access Notifications
- T1533: Data from Local System
- T1544: Ingress Tool Transfer
- T1575: Native API
- T1603: Scheduled Task/Job
- T1616: Call Control
- T1629.001: Prevent Application Removal
- T1629.003: Disable or Modify Tools
- T1630: Indicator Removal on Host
- T1633.001: System Checks
- T1636.004: SMS Messages
- T1646: Exfiltration Over C2 Channel
- T1655.001: Match Legitimate Name or Location
- T1660: Phishing
