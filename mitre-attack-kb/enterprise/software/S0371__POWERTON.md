# S0371: POWERTON

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0371  
**Aliases:** POWERTON  
**Platforms:** Windows  

## Description
[POWERTON](https://attack.mitre.org/software/S0371) is a custom PowerShell backdoor first observed in 2018. It has typically been deployed as a late-stage backdoor by [APT33](https://attack.mitre.org/groups/G0064). At least two variants of the backdoor have been identified, with the later version containing improved functionality.(Citation: FireEye APT33 Guardrail)

## Techniques Used
- T1003.002: Security Account Manager
- T1059.001: PowerShell
- T1071.001: Web Protocols
- T1546.003: Windows Management Instrumentation Event Subscription
- T1547.001: Registry Run Keys / Startup Folder
- T1573.001: Symmetric Cryptography
