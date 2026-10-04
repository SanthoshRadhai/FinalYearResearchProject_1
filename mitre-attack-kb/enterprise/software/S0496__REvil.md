# S0496: REvil

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0496  
**Aliases:** REvil, Sodin, Sodinokibi  
**Platforms:** Windows  

## Description
[REvil](https://attack.mitre.org/software/S0496) is a ransomware family that has been linked to the [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) group and operated as ransomware-as-a-service (RaaS) since at least April 2019. [REvil](https://attack.mitre.org/software/S0496), which as been used against organizations in the manufacturing, transportation, and electric sectors, is highly configurable and shares code similarities with the GandCrab RaaS.(Citation: Secureworks REvil September 2019)(Citation: Intel 471 REvil March 2020)(Citation: Group IB Ransomware May 2020)

## Techniques Used
- T1007: System Service Discovery
- T1012: Query Registry
- T1027.011: Fileless Storage
- T1027.013: Encrypted/Encoded File
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1047: Windows Management Instrumentation
- T1055: Process Injection
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1069.002: Domain Groups
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1112: Modify Registry
- T1134.001: Token Impersonation/Theft
- T1134.002: Create Process with Token
- T1140: Deobfuscate/Decode Files or Information
- T1189: Drive-by Compromise
- T1204.002: Malicious File
- T1480.002: Mutual Exclusion
- T1485: Data Destruction
- T1486: Data Encrypted for Impact
- T1489: Service Stop
- T1490: Inhibit System Recovery
- T1566.001: Spearphishing Attachment
- T1573.002: Asymmetric Cryptography
- T1614.001: System Language Discovery
- T1680: Local Storage Discovery
- T1685: Disable or Modify Tools
- T1688: Safe Mode Boot
