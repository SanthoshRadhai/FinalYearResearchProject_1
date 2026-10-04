# S0170: Helminth

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0170  
**Aliases:** Helminth  
**Platforms:** Windows  

## Description
[Helminth](https://attack.mitre.org/software/S0170) is a backdoor that has at least two variants - one written in VBScript and PowerShell that is delivered via a macros in Excel spreadsheets, and one that is a standalone Windows executable. (Citation: Palo Alto OilRig May 2016)

## Techniques Used
- T1027.013: Encrypted/Encoded File
- T1030: Data Transfer Size Limits
- T1053.005: Scheduled Task
- T1056.001: Keylogging
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1069.001: Local Groups
- T1069.002: Domain Groups
- T1071.001: Web Protocols
- T1071.004: DNS
- T1074.001: Local Data Staging
- T1105: Ingress Tool Transfer
- T1115: Clipboard Data
- T1119: Automated Collection
- T1132.001: Standard Encoding
- T1547.001: Registry Run Keys / Startup Folder
- T1547.009: Shortcut Modification
- T1553.002: Code Signing
- T1573.001: Symmetric Cryptography
