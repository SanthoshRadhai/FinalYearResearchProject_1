# S1064: SVCReady

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1064  
**Aliases:** SVCReady  
**Platforms:** Windows  

## Description
[SVCReady](https://attack.mitre.org/software/S1064) is a loader that has been used since at least April 2022 in malicious spam campaigns. Security researchers have noted overlaps between [TA551](https://attack.mitre.org/groups/G0127) activity and [SVCReady](https://attack.mitre.org/software/S1064) distribution, including similarities in file names, lure images, and identical grammatical errors.(Citation: HP SVCReady Jun 2022)

## Techniques Used
- T1005: Data from Local System
- T1012: Query Registry
- T1027: Obfuscated Files or Information
- T1033: System Owner/User Discovery
- T1036.004: Masquerade Task or Service
- T1041: Exfiltration Over C2 Channel
- T1047: Windows Management Instrumentation
- T1053.005: Scheduled Task
- T1057: Process Discovery
- T1059.005: Visual Basic
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1113: Screen Capture
- T1120: Peripheral Device Discovery
- T1124: System Time Discovery
- T1204.002: Malicious File
- T1218.011: Rundll32
- T1497.001: System Checks
- T1497.003: Time Based Checks
- T1518: Software Discovery
- T1546.015: Component Object Model Hijacking
- T1566.001: Spearphishing Attachment
