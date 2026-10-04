# S1115: WIREFIRE

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1115  
**Aliases:** WIREFIRE, GIFTEDVISITOR  
**Platforms:** Network Devices  

## Description
[WIREFIRE](https://attack.mitre.org/software/S1115) is a web shell written in Python that exists as trojanized logic to the visits.py component of Ivanti Connect Secure VPN appliances. [WIREFIRE](https://attack.mitre.org/software/S1115) was used during [Cutting Edge](https://attack.mitre.org/campaigns/C0029) for downloading files and command execution.(Citation: Mandiant Cutting Edge January 2024)

## Techniques Used
- T1071.001: Web Protocols
- T1105: Ingress Tool Transfer
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1505.003: Web Shell
- T1554: Compromise Host Software Binary
- T1573.001: Symmetric Cryptography
