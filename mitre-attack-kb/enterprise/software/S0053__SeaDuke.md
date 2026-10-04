# S0053: SeaDuke

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0053  
**Aliases:** SeaDuke, SeaDaddy, SeaDesk  
**Platforms:** Windows  

## Description
[SeaDuke](https://attack.mitre.org/software/S0053) is malware that was used by [APT29](https://attack.mitre.org/groups/G0016) from 2014 to 2015. It was used primarily as a secondary backdoor for victims that were already compromised with [CozyCar](https://attack.mitre.org/software/S0046). (Citation: F-Secure The Dukes)

## Techniques Used
- T1027.002: Software Packing
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1078: Valid Accounts
- T1105: Ingress Tool Transfer
- T1114.002: Remote Email Collection
- T1132.001: Standard Encoding
- T1546.003: Windows Management Instrumentation Event Subscription
- T1547.001: Registry Run Keys / Startup Folder
- T1547.009: Shortcut Modification
- T1550.003: Pass the Ticket
- T1560.002: Archive via Library
- T1573.001: Symmetric Cryptography
