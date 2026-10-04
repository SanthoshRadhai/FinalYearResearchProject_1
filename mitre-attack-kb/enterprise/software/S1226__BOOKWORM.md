# S1226: BOOKWORM

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1226  
**Aliases:** BOOKWORM  
**Platforms:** Windows  

## Description
[BOOKWORM](https://attack.mitre.org/software/S1226) is a modular trojan known to be leveraged by [Mustang Panda](https://attack.mitre.org/groups/G0129) and was first observed utilized in 2015.  [BOOKWORM](https://attack.mitre.org/software/S1226) was later updated in late 2021 and the fall of 2022 to launch shellcode represented as UUID parameters. (Citation: Broadcom)(Citation: Unit42 Bookworm Nov2015)(Citation: Palo Alto Networks, Unit 42)

## Techniques Used
- T1001.003: Protocol or Service Impersonation
- T1027: Obfuscated Files or Information
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1036.004: Masquerade Task or Service
- T1056.001: Keylogging
- T1070.006: Timestomp
- T1071.001: Web Protocols
- T1106: Native API
- T1112: Modify Registry
- T1115: Clipboard Data
- T1140: Deobfuscate/Decode Files or Information
- T1543.003: Windows Service
- T1553.002: Code Signing
- T1564.003: Hidden Window
- T1573.001: Symmetric Cryptography
- T1574.001: DLL
