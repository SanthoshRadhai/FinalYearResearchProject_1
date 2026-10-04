# S0023: CHOPSTICK

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0023  
**Aliases:** CHOPSTICK, Backdoor.SofacyX, SPLM, Xagent, X-Agent, webhp  
**Platforms:** Windows, Linux  

## Description
[CHOPSTICK](https://attack.mitre.org/software/S0023) is a malware family of modular backdoors used by [APT28](https://attack.mitre.org/groups/G0007). It has been used since at least 2012 and is usually dropped on victims as second-stage malware, though it has been used as first-stage malware in several cases. It has both Windows and Linux variants. (Citation: FireEye APT28) (Citation: ESET Sednit Part 2) (Citation: FireEye APT28 January 2017) (Citation: DOJ GRU Indictment Jul 2018) It is tracked separately from the [X-Agent for Android](https://attack.mitre.org/software/S0314).

## Techniques Used
- T1008: Fallback Channels
- T1012: Query Registry
- T1027.011: Fileless Storage
- T1056.001: Keylogging
- T1059: Command and Scripting Interpreter
- T1071.001: Web Protocols
- T1071.003: Mail Protocols
- T1083: File and Directory Discovery
- T1090.001: Internal Proxy
- T1091: Replication Through Removable Media
- T1092: Communication Through Removable Media
- T1105: Ingress Tool Transfer
- T1112: Modify Registry
- T1113: Screen Capture
- T1497: Virtualization/Sandbox Evasion
- T1518.001: Security Software Discovery
- T1568.002: Domain Generation Algorithms
- T1573.001: Symmetric Cryptography
- T1573.002: Asymmetric Cryptography
