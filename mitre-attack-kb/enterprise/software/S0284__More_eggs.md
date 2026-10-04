# S0284: More_eggs

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0284  
**Aliases:** More_eggs, SKID, Terra Loader, SpicyOmelette  
**Platforms:** Windows  

## Description
[More_eggs](https://attack.mitre.org/software/S0284) is a JScript backdoor used by [Cobalt Group](https://attack.mitre.org/groups/G0080) and [FIN6](https://attack.mitre.org/groups/G0037). Its name was given based on the variable "More_eggs" being present in its code. There are at least two different versions of the backdoor being used, version 2.0 and version 4.4. (Citation: Talos Cobalt Group July 2018)(Citation: Security Intelligence More Eggs Aug 2019)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1016.001: Internet Connection Discovery
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1105: Ingress Tool Transfer
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1218.010: Regsvr32
- T1518.001: Security Software Discovery
- T1553.002: Code Signing
- T1573.001: Symmetric Cryptography
