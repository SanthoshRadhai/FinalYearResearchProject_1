# S0452: USBferry

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0452  
**Aliases:** USBferry  
**Platforms:** Windows  

## Description
[USBferry](https://attack.mitre.org/software/S0452) is an information stealing malware and has been used by [Tropic Trooper](https://attack.mitre.org/groups/G0081) in targeted attacks against Taiwanese and Philippine air-gapped military environments. [USBferry](https://attack.mitre.org/software/S0452) shares an overlapping codebase with [YAHOYAH](https://attack.mitre.org/software/S0388), though it has several features which makes it a distinct piece of malware.(Citation: TrendMicro Tropic Trooper May 2020)

## Techniques Used
- T1005: Data from Local System
- T1016: System Network Configuration Discovery
- T1018: Remote System Discovery
- T1049: System Network Connections Discovery
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1083: File and Directory Discovery
- T1087.001: Local Account
- T1091: Replication Through Removable Media
- T1120: Peripheral Device Discovery
- T1218.011: Rundll32
