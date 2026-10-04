# S1184: BOLDMOVE

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1184  
**Aliases:** BOLDMOVE  
**Platforms:** Linux, Network Devices  

## Description
[BOLDMOVE](https://attack.mitre.org/software/S1184) is a type of backdoor malware written in C linked to People’s Republic of China operations from 2022 through 2023. [BOLDMOVE](https://attack.mitre.org/software/S1184) includes both Windows and Linux variants, with some Linux variants specifically designed for FortiGate Firewall devices. [BOLDMOVE](https://attack.mitre.org/software/S1184) is linked to zero-day exploitation of CVE-2022-42475 in FortiOSS SSL-VPNs.(Citation: Google Cloud BOLDMOVE 2023) The record for [BOLDMOVE](https://attack.mitre.org/software/S1184) only covers known Linux variants.

## Techniques Used
- T1016: System Network Configuration Discovery
- T1059.004: Unix Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1090.003: Multi-hop Proxy
- T1190: Exploit Public-Facing Application
- T1480: Execution Guardrails
- T1543: Create or Modify System Process
- T1554: Compromise Host Software Binary
- T1564.011: Ignore Process Interrupts
- T1573.002: Asymmetric Cryptography
- T1685: Disable or Modify Tools
