# S0034: NETEAGLE

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0034  
**Aliases:** NETEAGLE  
**Platforms:** Windows  

## Description
[NETEAGLE](https://attack.mitre.org/software/S0034) is a backdoor developed by [APT30](https://attack.mitre.org/groups/G0013) with compile dates as early as 2008. It has two main variants known as “Scout” and “Norton.” (Citation: FireEye APT30)

## Techniques Used
- T1008: Fallback Channels
- T1041: Exfiltration Over C2 Channel
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1071: Application Layer Protocol
- T1071.001: Web Protocols
- T1083: File and Directory Discovery
- T1095: Non-Application Layer Protocol
- T1547.001: Registry Run Keys / Startup Folder
- T1568: Dynamic Resolution
- T1573.001: Symmetric Cryptography
