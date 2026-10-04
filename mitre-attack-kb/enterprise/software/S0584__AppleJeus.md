# S0584: AppleJeus

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0584  
**Aliases:** AppleJeus  
**Platforms:** Windows, macOS  

## Description
[AppleJeus](https://attack.mitre.org/software/S0584) is a family of downloaders initially discovered in 2018 embedded within trojanized cryptocurrency applications. [AppleJeus](https://attack.mitre.org/software/S0584) has been used by [Lazarus Group](https://attack.mitre.org/groups/G0032), targeting companies in the energy, finance, government, industry, technology, and telecommunications sectors, and several countries including the United States, United Kingdom, South Korea, Australia, Brazil, New Zealand, and Russia. [AppleJeus](https://attack.mitre.org/software/S0584) has been used to distribute the [FALLCHILL](https://attack.mitre.org/software/S0181) RAT.(Citation: CISA AppleJeus Feb 2021)

## Techniques Used
- T1027: Obfuscated Files or Information
- T1041: Exfiltration Over C2 Channel
- T1053.005: Scheduled Task
- T1059.004: Unix Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1204.001: Malicious Link
- T1204.002: Malicious File
- T1218.007: Msiexec
- T1497.003: Time Based Checks
- T1543.003: Windows Service
- T1543.004: Launch Daemon
- T1546.016: Installer Packages
- T1548.002: Bypass User Account Control
- T1553.002: Code Signing
- T1564.001: Hidden Files and Directories
- T1566.002: Spearphishing Link
- T1569.001: Launchctl
