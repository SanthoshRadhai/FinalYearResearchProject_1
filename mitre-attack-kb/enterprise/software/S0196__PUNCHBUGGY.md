# S0196: PUNCHBUGGY

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0196  
**Aliases:** PUNCHBUGGY, ShellTea  
**Platforms:** Windows  

## Description
[PUNCHBUGGY](https://attack.mitre.org/software/S0196) is a backdoor malware used by [FIN8](https://attack.mitre.org/groups/G0061) that has been observed targeting POS networks in the hospitality industry. (Citation: Morphisec ShellTea June 2019)(Citation: FireEye Fin8 May 2016) (Citation: FireEye Know Your Enemy FIN8 Aug 2016)

## Techniques Used
- T1027: Obfuscated Files or Information
- T1036.005: Match Legitimate Resource Name or Location
- T1059.001: PowerShell
- T1059.006: Python
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1074.001: Local Data Staging
- T1082: System Information Discovery
- T1087.001: Local Account
- T1105: Ingress Tool Transfer
- T1129: Shared Modules
- T1140: Deobfuscate/Decode Files or Information
- T1218.011: Rundll32
- T1518.001: Security Software Discovery
- T1546.009: AppCert DLLs
- T1547.001: Registry Run Keys / Startup Folder
- T1560.001: Archive via Utility
