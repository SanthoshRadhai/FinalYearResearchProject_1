# S0150: POSHSPY

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0150  
**Aliases:** POSHSPY  
**Platforms:** Windows  

## Description
[POSHSPY](https://attack.mitre.org/software/S0150) is a backdoor that has been used by [APT29](https://attack.mitre.org/groups/G0016) since at least 2015. It appears to be used as a secondary backdoor used if the actors lost access to their primary backdoors. (Citation: FireEye POSHSPY April 2017)

## Techniques Used
- T1027: Obfuscated Files or Information
- T1030: Data Transfer Size Limits
- T1059.001: PowerShell
- T1070.006: Timestomp
- T1105: Ingress Tool Transfer
- T1546.003: Windows Management Instrumentation Event Subscription
- T1568.002: Domain Generation Algorithms
- T1573.002: Asymmetric Cryptography
