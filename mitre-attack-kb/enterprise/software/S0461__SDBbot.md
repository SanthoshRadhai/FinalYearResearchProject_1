# S0461: SDBbot

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0461  
**Aliases:** SDBbot  
**Platforms:** Windows  

## Description
[SDBbot](https://attack.mitre.org/software/S0461) is a backdoor with installer and loader components that has been used by [TA505](https://attack.mitre.org/groups/G0092) since at least 2019.(Citation: Proofpoint TA505 October 2019)(Citation: IBM TA505 April 2020)

## Techniques Used
- T1005: Data from Local System
- T1016: System Network Configuration Discovery
- T1021.001: Remote Desktop Protocol
- T1027: Obfuscated Files or Information
- T1027.002: Software Packing
- T1033: System Owner/User Discovery
- T1041: Exfiltration Over C2 Channel
- T1055.001: Dynamic-link Library Injection
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1070: Indicator Removal
- T1070.004: File Deletion
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1090: Proxy
- T1095: Non-Application Layer Protocol
- T1105: Ingress Tool Transfer
- T1125: Video Capture
- T1140: Deobfuscate/Decode Files or Information
- T1218.011: Rundll32
- T1546.011: Application Shimming
- T1546.012: Image File Execution Options Injection
- T1547.001: Registry Run Keys / Startup Folder
- T1614: System Location Discovery
