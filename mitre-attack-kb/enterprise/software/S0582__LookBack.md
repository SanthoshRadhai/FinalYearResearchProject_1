# S0582: LookBack

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0582  
**Aliases:** LookBack  
**Platforms:** Windows  

## Description
[LookBack](https://attack.mitre.org/software/S0582) is a remote access trojan written in C++ that was used against at least three US utility companies in July 2019. The TALONITE activity group has been observed using [LookBack](https://attack.mitre.org/software/S0582).(Citation: Proofpoint LookBack Malware Aug 2019)(Citation: Dragos TALONITE)(Citation: Dragos Threat Report 2020)

## Techniques Used
- T1007: System Service Discovery
- T1036.005: Match Legitimate Resource Name or Location
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1083: File and Directory Discovery
- T1095: Non-Application Layer Protocol
- T1113: Screen Capture
- T1140: Deobfuscate/Decode Files or Information
- T1489: Service Stop
- T1529: System Shutdown/Reboot
- T1547.001: Registry Run Keys / Startup Folder
- T1573.001: Symmetric Cryptography
- T1574.001: DLL
