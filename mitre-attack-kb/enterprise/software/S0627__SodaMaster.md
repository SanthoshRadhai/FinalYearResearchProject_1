# S0627: SodaMaster

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0627  
**Aliases:** SodaMaster, DARKTOWN, dfls, DelfsCake  
**Platforms:** Windows  

## Description
[SodaMaster](https://attack.mitre.org/software/S0627) is a fileless malware used by [menuPass](https://attack.mitre.org/groups/G0045) to download and execute payloads since at least 2020.(Citation: Securelist APT10 March 2021)

## Techniques Used
- T1012: Query Registry
- T1027: Obfuscated Files or Information
- T1033: System Owner/User Discovery
- T1057: Process Discovery
- T1082: System Information Discovery
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1497.001: System Checks
- T1497.003: Time Based Checks
- T1573.001: Symmetric Cryptography
- T1573.002: Asymmetric Cryptography
