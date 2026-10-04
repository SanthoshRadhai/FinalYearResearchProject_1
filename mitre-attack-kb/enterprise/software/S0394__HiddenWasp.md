# S0394: HiddenWasp

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0394  
**Aliases:** HiddenWasp  
**Platforms:** Linux  

## Description
[HiddenWasp](https://attack.mitre.org/software/S0394) is a Linux-based Trojan used to target systems for remote control. It comes in the form of a statically linked ELF binary with stdlibc++.(Citation: Intezer HiddenWasp Map 2019)

## Techniques Used
- T1014: Rootkit
- T1027.013: Encrypted/Encoded File
- T1037.004: RC Scripts
- T1059.003: Windows Command Shell
- T1095: Non-Application Layer Protocol
- T1105: Ingress Tool Transfer
- T1136.001: Local Account
- T1140: Deobfuscate/Decode Files or Information
- T1573.001: Symmetric Cryptography
- T1574.006: Dynamic Linker Hijacking
