# S0671: Tomiris

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0671  
**Aliases:** Tomiris  

## Description
[Tomiris](https://attack.mitre.org/software/S0671) is a backdoor written in Go that continuously queries its C2 server for executables to download and execute on a victim system. It was first reported in September 2021 during an investigation of a successful DNS hijacking campaign against a Commonwealth of Independent States (CIS) member. Security researchers assess there are similarities between [Tomiris](https://attack.mitre.org/software/S0671) and [GoldMax](https://attack.mitre.org/software/S0588).(Citation: Kaspersky Tomiris Sep 2021)

## Techniques Used
- T1005: Data from Local System
- T1027.002: Software Packing
- T1041: Exfiltration Over C2 Channel
- T1053.005: Scheduled Task
- T1071.001: Web Protocols
- T1105: Ingress Tool Transfer
- T1497.003: Time Based Checks
- T1568: Dynamic Resolution
