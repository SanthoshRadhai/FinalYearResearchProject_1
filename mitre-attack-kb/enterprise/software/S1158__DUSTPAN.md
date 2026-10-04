# S1158: DUSTPAN

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1158  
**Aliases:** DUSTPAN  
**Platforms:** Windows  

## Description
[DUSTPAN](https://attack.mitre.org/software/S1158) is an in-memory dropper written in C/C++ used by [APT41](https://attack.mitre.org/groups/G0096) since 2021 that decrypts and executes an embedded payload.(Citation: Google Cloud APT41 2024)(Citation: Google Cloud APT41 2022)

## Techniques Used
- T1027.009: Embedded Payloads
- T1027.013: Encrypted/Encoded File
- T1036.005: Match Legitimate Resource Name or Location
- T1055.002: Portable Executable Injection
- T1140: Deobfuscate/Decode Files or Information
- T1543.003: Windows Service
