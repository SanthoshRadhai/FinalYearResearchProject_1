# S0631: Chaes

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0631  
**Aliases:** Chaes  
**Platforms:** Windows  

## Description
[Chaes](https://attack.mitre.org/software/S0631) is a multistage information stealer written in several programming languages that collects login credentials, credit card numbers, and other financial information. [Chaes](https://attack.mitre.org/software/S0631) was first observed in 2020, and appears to primarily target victims in Brazil as well as other e-commerce customers in Latin America.(Citation: Cybereason Chaes Nov 2020)

## Techniques Used
- T1027.011: Fileless Storage
- T1033: System Owner/User Discovery
- T1036.005: Match Legitimate Resource Name or Location
- T1048: Exfiltration Over Alternative Protocol
- T1056: Input Capture
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1059.006: Python
- T1059.007: JavaScript
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1112: Modify Registry
- T1113: Screen Capture
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1185: Browser Session Hijacking
- T1204.002: Malicious File
- T1218.004: InstallUtil
- T1218.007: Msiexec
- T1221: Template Injection
- T1539: Steal Web Session Cookie
- T1547.001: Registry Run Keys / Startup Folder
- T1555.003: Credentials from Web Browsers
- T1566.001: Spearphishing Attachment
- T1573: Encrypted Channel
- T1574.001: DLL
