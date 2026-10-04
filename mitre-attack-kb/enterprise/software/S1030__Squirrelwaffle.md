# S1030: Squirrelwaffle

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1030  
**Aliases:** Squirrelwaffle  
**Platforms:** Windows  

## Description
[Squirrelwaffle](https://attack.mitre.org/software/S1030) is a loader that was first seen in September 2021. It has been used in spam email campaigns to deliver additional malware such as [Cobalt Strike](https://attack.mitre.org/software/S0154) and the [QakBot](https://attack.mitre.org/software/S0650) banking trojan.(Citation: ZScaler Squirrelwaffle Sep 2021)(Citation: Netskope Squirrelwaffle Oct 2021)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1027.002: Software Packing
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1041: Exfiltration Over C2 Channel
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1105: Ingress Tool Transfer
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1204.001: Malicious Link
- T1204.002: Malicious File
- T1218.010: Regsvr32
- T1218.011: Rundll32
- T1497: Virtualization/Sandbox Evasion
- T1560.003: Archive via Custom Method
- T1566.001: Spearphishing Attachment
- T1566.002: Spearphishing Link
