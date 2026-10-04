# TA0011: Command and Control

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0011  

## Description
The adversary is trying to communicate with compromised systems to control them.

Command and Control consists of techniques that adversaries may use to communicate with systems under their control within a victim network. Adversaries commonly attempt to mimic normal, expected traffic to avoid detection. There are many ways an adversary can establish command and control with various levels of stealth depending on the victim’s network structure and defenses.

## Techniques in This Tactic
- T1001: Data Obfuscation
- T1001.001: Junk Data
- T1001.002: Steganography
- T1001.003: Protocol or Service Impersonation
- T1008: Fallback Channels
- T1071: Application Layer Protocol
- T1071.001: Web Protocols
- T1071.002: File Transfer Protocols
- T1071.003: Mail Protocols
- T1071.004: DNS
- T1071.005: Publish/Subscribe Protocols
- T1090: Proxy
- T1090.001: Internal Proxy
- T1090.002: External Proxy
- T1090.003: Multi-hop Proxy
- T1090.004: Domain Fronting
- T1092: Communication Through Removable Media
- T1095: Non-Application Layer Protocol
- T1102: Web Service
- T1102.001: Dead Drop Resolver
- T1102.002: Bidirectional Communication
- T1102.003: One-Way Communication
- T1104: Multi-Stage Channels
- T1105: Ingress Tool Transfer
- T1132: Data Encoding
- T1132.001: Standard Encoding
- T1132.002: Non-Standard Encoding
- T1205: Traffic Signaling
- T1205.001: Port Knocking
- T1205.002: Socket Filters
- T1219: Remote Access Tools
- T1219.001: IDE Tunneling
- T1219.002: Remote Desktop Software
- T1219.003: Remote Access Hardware
- T1568: Dynamic Resolution
- T1568.001: Fast Flux DNS
- T1568.002: Domain Generation Algorithms
- T1568.003: DNS Calculation
- T1571: Non-Standard Port
- T1572: Protocol Tunneling
- T1573: Encrypted Channel
- T1573.001: Symmetric Cryptography
- T1573.002: Asymmetric Cryptography
- T1659: Content Injection
- T1665: Hide Infrastructure
