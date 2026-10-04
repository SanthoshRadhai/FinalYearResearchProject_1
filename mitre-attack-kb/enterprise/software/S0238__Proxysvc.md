# S0238: Proxysvc

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0238  
**Aliases:** Proxysvc  
**Platforms:** Windows  

## Description
[Proxysvc](https://attack.mitre.org/software/S0238) is a malicious DLL used by [Lazarus Group](https://attack.mitre.org/groups/G0032) in a campaign known as Operation GhostSecret. It has appeared to be operating undetected since 2017 and was mostly observed in higher education organizations. The goal of [Proxysvc](https://attack.mitre.org/software/S0238) is to deliver additional payloads to the target and to maintain control for the attacker. It is in the form of a DLL that can also be executed as a standalone process. (Citation: McAfee GhostSecret)

## Techniques Used
- T1005: Data from Local System
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1041: Exfiltration Over C2 Channel
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1119: Automated Collection
- T1124: System Time Discovery
- T1485: Data Destruction
- T1569.002: Service Execution
- T1680: Local Storage Discovery
