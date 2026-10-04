# S1123: PITSTOP

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1123  
**Aliases:** PITSTOP  
**Platforms:** Network Devices  

## Description
[PITSTOP](https://attack.mitre.org/software/S1123) is a backdoor that was deployed on compromised Ivanti Connect Secure VPNs during [Cutting Edge](https://attack.mitre.org/campaigns/C0029) to enable command execution and file read/write.(Citation: Mandiant Cutting Edge Part 3 February 2024)

## Techniques Used
- T1059.004: Unix Shell
- T1140: Deobfuscate/Decode Files or Information
- T1205.002: Socket Filters
- T1559: Inter-Process Communication
- T1573.002: Asymmetric Cryptography
