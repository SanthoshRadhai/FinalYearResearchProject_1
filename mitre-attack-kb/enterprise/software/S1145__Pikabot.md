# S1145: Pikabot

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1145  
**Aliases:** Pikabot  
**Platforms:** Windows  

## Description
[Pikabot](https://attack.mitre.org/software/S1145) is a backdoor used for initial access and follow-on tool deployment active since early 2023. [Pikabot](https://attack.mitre.org/software/S1145) is notable for extensive use of multiple encoding, encryption, and defense evasion mechanisms to evade defenses and avoid analysis. [Pikabot](https://attack.mitre.org/software/S1145) has some overlaps with [QakBot](https://attack.mitre.org/software/S0650), but insufficient evidence exists to definitively link these two malware families. [Pikabot](https://attack.mitre.org/software/S1145) is frequently used to deploy follow on tools such as [Cobalt Strike](https://attack.mitre.org/software/S0154) or ransomware variants.(Citation: Zscaler Pikabot 2023)(Citation: Elastic Pikabot 2024)(Citation: Logpoint Pikabot 2024)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1027.003: Steganography
- T1027.009: Embedded Payloads
- T1027.011: Fileless Storage
- T1041: Exfiltration Over C2 Channel
- T1055.002: Portable Executable Injection
- T1055.003: Thread Execution Hijacking
- T1059.003: Windows Command Shell
- T1082: System Information Discovery
- T1087.001: Local Account
- T1106: Native API
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1480.001: Environmental Keying
- T1482: Domain Trust Discovery
- T1497.001: System Checks
- T1547.001: Registry Run Keys / Startup Folder
- T1571: Non-Standard Port
- T1573.001: Symmetric Cryptography
- T1620: Reflective Code Loading
- T1622: Debugger Evasion
