# S1106: NGLite

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1106  
**Aliases:** NGLite  
**Platforms:** Windows  

## Description
[NGLite](https://attack.mitre.org/software/S1106) is a backdoor Trojan that is only capable of running commands received through its C2 channel. While the capabilities are standard for a backdoor, NGLite uses a novel C2 channel that leverages a decentralized network based on the legitimate NKN to communicate between the backdoor and the actors.(Citation: NGLite Trojan)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1033: System Owner/User Discovery
- T1071.001: Web Protocols
- T1090.003: Multi-hop Proxy
- T1573.001: Symmetric Cryptography
