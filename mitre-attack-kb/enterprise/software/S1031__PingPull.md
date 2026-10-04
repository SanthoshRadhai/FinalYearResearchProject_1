# S1031: PingPull

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1031  
**Aliases:** PingPull  
**Platforms:** Windows  

## Description
[PingPull](https://attack.mitre.org/software/S1031) is a remote access Trojan (RAT) written in Visual C++ that has been used by [GALLIUM](https://attack.mitre.org/groups/G0093) since at least June 2022. [PingPull](https://attack.mitre.org/software/S1031) has been used to target telecommunications companies, financial institutions, and government entities in Afghanistan, Australia, Belgium, Cambodia, Malaysia, Mozambique, the Philippines, Russia, and Vietnam.(Citation: Unit 42 PingPull Jun 2022)

## Techniques Used
- T1005: Data from Local System
- T1016: System Network Configuration Discovery
- T1036.004: Masquerade Task or Service
- T1041: Exfiltration Over C2 Channel
- T1059.003: Windows Command Shell
- T1070.006: Timestomp
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1095: Non-Application Layer Protocol
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1543.003: Windows Service
- T1571: Non-Standard Port
- T1573.001: Symmetric Cryptography
