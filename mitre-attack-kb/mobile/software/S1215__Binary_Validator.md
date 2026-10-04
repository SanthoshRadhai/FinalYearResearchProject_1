# S1215: Binary Validator

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1215  
**Aliases:** Binary Validator  
**Platforms:** iOS  

## Description
[Binary Validator](https://attack.mitre.org/software/S1215) is a Mach-O binary file used during [Operation Triangulation](https://attack.mitre.org/campaigns/C0054).(Citation: SecureList OpTriangulation 23Oct2023) [Binary Validator](https://attack.mitre.org/software/S1215) first collects information about the device, such as the device's phone number and a list of installed applications, before the deployment of the [TriangleDB](https://attack.mitre.org/software/S1216) implant.  After the actions are completed and the data is collected, [Binary Validator](https://attack.mitre.org/software/S1215) encrypts and sends the data to the C2 server, and in turn, the C2 server sends the [TriangleDB](https://attack.mitre.org/software/S1216) implant.

## Techniques Used
- T1418: Software Discovery
- T1422: System Network Configuration Discovery
- T1424: Process Discovery
- T1533: Data from Local System
- T1627: Execution Guardrails
- T1630.002: File Deletion
- T1646: Exfiltration Over C2 Channel
