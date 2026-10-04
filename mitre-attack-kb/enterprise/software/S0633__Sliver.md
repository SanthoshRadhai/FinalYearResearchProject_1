# S0633: Sliver

**Type:** tool  
**Reference:** https://attack.mitre.org/software/S0633  
**Aliases:** Sliver  
**Platforms:** Windows, Linux, macOS  

## Description
[Sliver](https://attack.mitre.org/software/S0633) is an open source, cross-platform, red team command and control (C2) framework written in Golang. [Sliver](https://attack.mitre.org/software/S0633) includes its own package manager, "armory," for staging and downloading additional tools and payloads to the primary C2 framework.(Citation: Bishop Fox Sliver Framework August 2019)(Citation: Cybereason Sliver Undated)

## Techniques Used
- T1001.002: Steganography
- T1003.001: LSASS Memory
- T1016: System Network Configuration Discovery
- T1027: Obfuscated Files or Information
- T1027.004: Compile After Delivery
- T1027.013: Encrypted/Encoded File
- T1041: Exfiltration Over C2 Channel
- T1049: System Network Connections Discovery
- T1055: Process Injection
- T1059.001: PowerShell
- T1071: Application Layer Protocol
- T1071.001: Web Protocols
- T1071.004: DNS
- T1083: File and Directory Discovery
- T1090.001: Internal Proxy
- T1105: Ingress Tool Transfer
- T1113: Screen Capture
- T1132.001: Standard Encoding
- T1134: Access Token Manipulation
- T1548.002: Bypass User Account Control
- T1558.001: Golden Ticket
- T1573.001: Symmetric Cryptography
- T1573.002: Asymmetric Cryptography
