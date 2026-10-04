# S0241: RATANKBA

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0241  
**Aliases:** RATANKBA  
**Platforms:** Windows  

## Description
[RATANKBA](https://attack.mitre.org/software/S0241) is a remote controller tool used by [Lazarus Group](https://attack.mitre.org/groups/G0032). [RATANKBA](https://attack.mitre.org/software/S0241) has been used in attacks targeting financial institutions in Poland, Mexico, Uruguay, the United Kingdom, and Chile. It was also seen used against organizations related to telecommunications, management consulting, information technology, insurance, aviation, and education. [RATANKBA](https://attack.mitre.org/software/S0241) has a graphical user interface to allow the attacker to issue jobs to perform on the infected machines. (Citation: Lazarus RATANKBA) (Citation: RATANKBA)

## Techniques Used
- T1007: System Service Discovery
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1018: Remote System Discovery
- T1033: System Owner/User Discovery
- T1047: Windows Management Instrumentation
- T1049: System Network Connections Discovery
- T1055.001: Dynamic-link Library Injection
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1087.001: Local Account
- T1105: Ingress Tool Transfer
