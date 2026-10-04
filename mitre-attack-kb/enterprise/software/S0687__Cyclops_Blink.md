# S0687: Cyclops Blink

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0687  
**Aliases:** Cyclops Blink  
**Platforms:** Network Devices  

## Description
[Cyclops Blink](https://attack.mitre.org/software/S0687) is a modular malware that has been used in widespread campaigns by [Sandworm Team](https://attack.mitre.org/groups/G0034) since at least 2019 to target Small/Home Office (SOHO) network devices, including WatchGuard and Asus. [Cyclops Blink](https://attack.mitre.org/software/S0687) is assessed to be a replacement for [VPNFilter](https://attack.mitre.org/software/S1010), a similar platform targeting network devices.(Citation: NCSC Cyclops Blink February 2022)(Citation: NCSC CISA Cyclops Blink Advisory February 2022)(Citation: Trend Micro Cyclops Blink March 2022)

## Techniques Used
- T1005: Data from Local System
- T1016: System Network Configuration Discovery
- T1036.005: Match Legitimate Resource Name or Location
- T1037.004: RC Scripts
- T1041: Exfiltration Over C2 Channel
- T1057: Process Discovery
- T1070.006: Timestomp
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1090.003: Multi-hop Proxy
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1132.002: Non-Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1542.002: Component Firmware
- T1559: Inter-Process Communication
- T1571: Non-Standard Port
- T1572: Protocol Tunneling
- T1573.002: Asymmetric Cryptography
- T1686.002: Network Device Firewall
