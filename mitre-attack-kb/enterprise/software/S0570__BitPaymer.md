# S0570: BitPaymer

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0570  
**Aliases:** BitPaymer, wp_encrypt, FriedEx  
**Platforms:** Windows  

## Description
[BitPaymer](https://attack.mitre.org/software/S0570) is a ransomware variant first observed in August 2017 targeting hospitals in the U.K. [BitPaymer](https://attack.mitre.org/software/S0570) uses a unique encryption key, ransom note, and contact information for each operation. [BitPaymer](https://attack.mitre.org/software/S0570) has several indicators suggesting overlap with the [Dridex](https://attack.mitre.org/software/S0384) malware and is often delivered via [Dridex](https://attack.mitre.org/software/S0384).(Citation: Crowdstrike Indrik November 2018)

## Techniques Used
- T1007: System Service Discovery
- T1012: Query Registry
- T1018: Remote System Discovery
- T1027.013: Encrypted/Encoded File
- T1070.006: Timestomp
- T1087.001: Local Account
- T1106: Native API
- T1112: Modify Registry
- T1134.001: Token Impersonation/Theft
- T1135: Network Share Discovery
- T1222.001: Windows Permissions
- T1480: Execution Guardrails
- T1486: Data Encrypted for Impact
- T1490: Inhibit System Recovery
- T1543.003: Windows Service
- T1547.001: Registry Run Keys / Startup Folder
- T1548.002: Bypass User Account Control
- T1564.004: NTFS File Attributes
