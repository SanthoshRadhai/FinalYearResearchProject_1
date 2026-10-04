# S0239: Bankshot

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0239  
**Aliases:** Bankshot, Trojan Manuscript  
**Platforms:** Windows  

## Description
[Bankshot](https://attack.mitre.org/software/S0239) is a remote access tool (RAT) that was first reported by the Department of Homeland Security in December of 2017. In 2018, [Lazarus Group](https://attack.mitre.org/groups/G0032) used the [Bankshot](https://attack.mitre.org/software/S0239) implant in attacks against the Turkish financial sector. (Citation: McAfee Bankshot)

## Techniques Used
- T1001.003: Protocol or Service Impersonation
- T1005: Data from Local System
- T1012: Query Registry
- T1041: Exfiltration Over C2 Channel
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1070: Indicator Removal
- T1070.004: File Deletion
- T1070.006: Timestomp
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087.001: Local Account
- T1087.002: Domain Account
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1112: Modify Registry
- T1119: Automated Collection
- T1132.002: Non-Standard Encoding
- T1134.002: Create Process with Token
- T1140: Deobfuscate/Decode Files or Information
- T1203: Exploitation for Client Execution
- T1543.003: Windows Service
- T1571: Non-Standard Port
- T1680: Local Storage Discovery
