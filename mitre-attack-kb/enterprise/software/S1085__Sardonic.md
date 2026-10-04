# S1085: Sardonic

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1085  
**Aliases:** Sardonic  
**Platforms:** Windows  

## Description
[Sardonic](https://attack.mitre.org/software/S1085) is a backdoor written in C and C++ that is known to be used by [FIN8](https://attack.mitre.org/groups/G0061), as early as August 2021 to target a financial institution in the United States. [Sardonic](https://attack.mitre.org/software/S1085) has a plugin system that can load specially made DLLs and execute their functions.(Citation: Bitdefender Sardonic Aug 2021)(Citation: Symantec FIN8 Jul 2023)

## Techniques Used
- T1005: Data from Local System
- T1007: System Service Discovery
- T1016: System Network Configuration Discovery
- T1027: Obfuscated Files or Information
- T1027.010: Command Obfuscation
- T1047: Windows Management Instrumentation
- T1049: System Network Connections Discovery
- T1055.004: Asynchronous Procedure Call
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1070: Indicator Removal
- T1082: System Information Discovery
- T1095: Non-Application Layer Protocol
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1132.001: Standard Encoding
- T1135: Network Share Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1546.003: Windows Management Instrumentation Event Subscription
- T1571: Non-Standard Port
- T1573.001: Symmetric Cryptography
- T1573.002: Asymmetric Cryptography
- T1620: Reflective Code Loading
- T1680: Local Storage Discovery
