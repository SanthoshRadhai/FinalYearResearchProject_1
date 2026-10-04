# S0511: RegDuke

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0511  
**Aliases:** RegDuke  
**Platforms:** Windows  

## Description
[RegDuke](https://attack.mitre.org/software/S0511) is a first stage implant written in .NET and used by [APT29](https://attack.mitre.org/groups/G0016) since at least 2017. [RegDuke](https://attack.mitre.org/software/S0511) has been used to control a compromised machine when control of other implants on the machine was lost.(Citation: ESET Dukes October 2019)

## Techniques Used
- T1027: Obfuscated Files or Information
- T1027.003: Steganography
- T1027.011: Fileless Storage
- T1059.001: PowerShell
- T1102.002: Bidirectional Communication
- T1105: Ingress Tool Transfer
- T1112: Modify Registry
- T1140: Deobfuscate/Decode Files or Information
- T1546.003: Windows Management Instrumentation Event Subscription
