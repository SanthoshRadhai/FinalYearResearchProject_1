# S9007: HTTPTroy

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9007  
**Aliases:** HTTPTroy  
**Platforms:** Windows  

## Description
[HTTPTroy](https://attack.mitre.org/software/S9007) is a highly obfuscated backdoor that facilitates collection, command and control, defense evasion and exfiltration.  [HTTPTroy](https://attack.mitre.org/software/S9007) was first reported in October 2025. [HTTPTroy](https://attack.mitre.org/software/S9007) has been observed in operations attributed to DPRK-affiliated threat actors, including [Kimsuky](https://attack.mitre.org/groups/G0094).  [HTTPTroy](https://attack.mitre.org/software/S9007) has been delivered to victims through a separate loader leveraged by [Kimsuky](https://attack.mitre.org/groups/G0094).(Citation: Gen Digital Kimsuky HTTPTroy October 2025)

## Techniques Used
- T1027: Obfuscated Files or Information
- T1027.007: Dynamic API Resolution
- T1041: Exfiltration Over C2 Channel
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1113: Screen Capture
- T1132.002: Non-Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1548.002: Bypass User Account Control
- T1573.001: Symmetric Cryptography
