# S1079: BOULDSPY

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1079  
**Aliases:** BOULDSPY  
**Platforms:** Android  

## Description
[BOULDSPY](https://attack.mitre.org/software/S1079) is an Android malware, detected in early 2023, with surveillance and remote-control capabilities. Analysis of exfiltrated C2 data suggests that [BOULDSPY](https://attack.mitre.org/software/S1079) primarily targeted minority groups in Iran.(Citation: lookout_bouldspy_0423)

## Techniques Used
- T1398: Boot or Logon Initialization Scripts
- T1407: Download New Code at Runtime
- T1409: Stored Application Data
- T1414: Clipboard Data
- T1417.001: Keylogging
- T1418: Software Discovery
- T1422: System Network Configuration Discovery
- T1422.001: Internet Connection Discovery
- T1422.002: Wi-Fi Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1437.001: Web Protocols
- T1512: Video Capture
- T1513: Screen Capture
- T1532: Archive Collected Data
- T1533: Data from Local System
- T1577: Compromise Application Executable
- T1624: Event Triggered Execution
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1644: Out of Band Data
- T1646: Exfiltration Over C2 Channel
- T1655.001: Match Legitimate Name or Location
