# S0401: Exaramel for Linux

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0401  
**Aliases:** Exaramel for Linux  
**Platforms:** Linux  

## Description
[Exaramel for Linux](https://attack.mitre.org/software/S0401) is a backdoor written in the Go Programming Language and compiled as a 64-bit ELF binary. The Windows version is tracked separately under [Exaramel for Windows](https://attack.mitre.org/software/S0343).(Citation: ESET TeleBots Oct 2018)

## Techniques Used
- T1008: Fallback Channels
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1053.003: Cron
- T1059.004: Unix Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1105: Ingress Tool Transfer
- T1140: Deobfuscate/Decode Files or Information
- T1543: Create or Modify System Process
- T1543.002: Systemd Service
- T1548.001: Setuid and Setgid
