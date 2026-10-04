# S1216: TriangleDB

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1216  
**Aliases:** TriangleDB  
**Platforms:** iOS  

## Description
[TriangleDB](https://attack.mitre.org/software/S1216) is an Objective-C written implant deployed after [Binary Validator](https://attack.mitre.org/software/S1215) and after root privileges are obtained during [Operation Triangulation](https://attack.mitre.org/campaigns/C0054)’s infection chain. Upon execution, [TriangleDB](https://attack.mitre.org/software/S1216) communicates with the C2 server, relaying information about the victim device.(Citation: SecureList OpTriangulation 21Jun2023)

## Techniques Used
- T1418: Software Discovery
- T1420: File and Directory Discovery
- T1422: System Network Configuration Discovery
- T1424: Process Discovery
- T1430: Location Tracking
- T1521.001: Symmetric Cryptography
- T1521.002: Asymmetric Cryptography
- T1533: Data from Local System
- T1544: Ingress Tool Transfer
- T1630.002: File Deletion
- T1634.001: Keychain
- T1644: Out of Band Data
