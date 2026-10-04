# S0139: PowerDuke

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0139  
**Aliases:** PowerDuke  
**Platforms:** Windows  

## Description
[PowerDuke](https://attack.mitre.org/software/S0139) is a backdoor that was used by [APT29](https://attack.mitre.org/groups/G0016) in 2016. It has primarily been delivered through Microsoft Word or Excel attachments containing malicious macros. (Citation: Volexity PowerDuke November 2016)

## Techniques Used
- T1010: Application Window Discovery
- T1016: System Network Configuration Discovery
- T1027.003: Steganography
- T1033: System Owner/User Discovery
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1124: System Time Discovery
- T1218.011: Rundll32
- T1485: Data Destruction
- T1547.001: Registry Run Keys / Startup Folder
- T1564.004: NTFS File Attributes
