# S1138: Gootloader

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1138  
**Aliases:** Gootloader  
**Platforms:** Windows  

## Description
[Gootloader](https://attack.mitre.org/software/S1138) is a Javascript-based infection framework that has been used since at least 2020 as a delivery method for the Gootkit banking trojan, [Cobalt Strike](https://attack.mitre.org/software/S0154), [REvil](https://attack.mitre.org/software/S0496), and others. [Gootloader](https://attack.mitre.org/software/S1138) operates on an "Initial Access as a Service" model and has leveraged [SEO Poisoning](https://attack.mitre.org/techniques/T1608/006) to provide access to entities in multiple sectors worldwide including financial, military, automotive, pharmaceutical, and energy.(Citation: Sophos Gootloader)(Citation: SentinelOne Gootloader June 2021)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1027: Obfuscated Files or Information
- T1055.002: Portable Executable Injection
- T1055.012: Process Hollowing
- T1059.001: PowerShell
- T1059.007: JavaScript
- T1069.002: Domain Groups
- T1082: System Information Discovery
- T1105: Ingress Tool Transfer
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1204.001: Malicious Link
- T1497.003: Time Based Checks
- T1547.001: Registry Run Keys / Startup Folder
- T1584.001: Domains
- T1584.006: Web Services
- T1614: System Location Discovery
- T1614.001: System Language Discovery
