# S1146: MgBot

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1146  
**Aliases:** MgBot  
**Platforms:** Windows  

## Description
[MgBot](https://attack.mitre.org/software/S1146) is a modular malware framework exclusively associated with [Daggerfly](https://attack.mitre.org/groups/G1034) operations since at least 2012. [MgBot](https://attack.mitre.org/software/S1146) was developed in C++ and features a module design with multiple available plugins that have been under active development through 2024.(Citation: Szappanos MgBot 2014)(Citation: ESET EvasivePanda 2023)(Citation: Symantec Daggerfly 2024)

## Techniques Used
- T1003: OS Credential Dumping
- T1005: Data from Local System
- T1018: Remote System Discovery
- T1025: Data from Removable Media
- T1033: System Owner/User Discovery
- T1046: Network Service Discovery
- T1056.001: Keylogging
- T1057: Process Discovery
- T1087.001: Local Account
- T1087.002: Domain Account
- T1115: Clipboard Data
- T1123: Audio Capture
- T1213.006: Databases
- T1482: Domain Trust Discovery
- T1539: Steal Web Session Cookie
- T1555: Credentials from Password Stores
- T1555.003: Credentials from Web Browsers
