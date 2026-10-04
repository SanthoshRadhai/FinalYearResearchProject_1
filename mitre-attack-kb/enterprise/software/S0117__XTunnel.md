# S0117: XTunnel

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0117  
**Aliases:** XTunnel, Trojan.Shunnael, X-Tunnel, XAPS  
**Platforms:** Windows  

## Description
[XTunnel](https://attack.mitre.org/software/S0117) a VPN-like network proxy tool that can relay traffic between a C2 server and a victim. It was first seen in May 2013 and reportedly used by [APT28](https://attack.mitre.org/groups/G0007) during the compromise of the Democratic National Committee. (Citation: Crowdstrike DNC June 2016) (Citation: Invincea XTunnel) (Citation: ESET Sednit Part 2)

## Techniques Used
- T1008: Fallback Channels
- T1027: Obfuscated Files or Information
- T1027.016: Junk Code Insertion
- T1046: Network Service Discovery
- T1059.003: Windows Command Shell
- T1090: Proxy
- T1552.001: Credentials In Files
- T1573.002: Asymmetric Cryptography
