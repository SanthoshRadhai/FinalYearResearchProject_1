# S0022: Uroburos

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0022  
**Aliases:** Uroburos, Snake  
**Platforms:** Linux, Windows, macOS  

## Description
[Uroburos](https://attack.mitre.org/software/S0022) is a sophisticated cyber espionage tool written in C that has been used by units within Russia's Federal Security Service (FSB) associated with the [Turla](https://attack.mitre.org/groups/G0010) toolset to collect intelligence on sensitive targets worldwide. [Uroburos](https://attack.mitre.org/software/S0022) has several variants and has undergone nearly constant upgrade since its initial development in 2003 to keep it viable after public disclosures. [Uroburos](https://attack.mitre.org/software/S0022) is typically deployed to external-facing nodes on a targeted network and has the ability to leverage additional tools and TTPs to further exploit an internal network. [Uroburos](https://attack.mitre.org/software/S0022) has interoperable implants for Windows, Linux, and macOS, employs a high level of stealth in communications and architecture, and can easily incorporate new or replacement components.(Citation: Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023)(Citation: Kaspersky Turla)

## Techniques Used
- T1001.001: Junk Data
- T1001.003: Protocol or Service Impersonation
- T1005: Data from Local System
- T1008: Fallback Channels
- T1012: Query Registry
- T1014: Rootkit
- T1027.002: Software Packing
- T1027.009: Embedded Payloads
- T1027.011: Fileless Storage
- T1027.013: Encrypted/Encoded File
- T1036.004: Masquerade Task or Service
- T1055.001: Dynamic-link Library Injection
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1071.003: Mail Protocols
- T1071.004: DNS
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1090.003: Multi-hop Proxy
- T1095: Non-Application Layer Protocol
- T1104: Multi-Stage Channels
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1112: Modify Registry
- T1132.002: Non-Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1205: Traffic Signaling
- T1543.003: Windows Service
- T1559: Inter-Process Communication
- T1564.005: Hidden File System
- T1572: Protocol Tunneling
- T1573.001: Symmetric Cryptography
- T1573.002: Asymmetric Cryptography
- T1620: Reflective Code Loading
