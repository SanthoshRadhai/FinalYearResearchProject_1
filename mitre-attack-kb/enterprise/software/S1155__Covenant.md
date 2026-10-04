# S1155: Covenant

**Type:** tool  
**Reference:** https://attack.mitre.org/software/S1155  
**Aliases:** Covenant  
**Platforms:** Linux, macOS, Windows  

## Description
[Covenant](https://attack.mitre.org/software/S1155) is a multi-platform command and control framework written in .NET. While designed for penetration testing and security research, the tool has also been used by threat actors such as [HAFNIUM](https://attack.mitre.org/groups/G0125) during operations. [Covenant](https://attack.mitre.org/software/S1155) functions through a central listener managing multiple deployed "Grunts" that communicate back to the controller.(Citation: Github Covenant)(Citation: Microsoft HAFNIUM March 2020)

## Techniques Used
- T1047: Windows Management Instrumentation
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1218.004: InstallUtil
- T1218.005: Mshta
- T1218.010: Regsvr32
- T1571: Non-Standard Port
- T1573.002: Asymmetric Cryptography
