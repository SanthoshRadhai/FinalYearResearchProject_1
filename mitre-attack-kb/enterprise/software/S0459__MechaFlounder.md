# S0459: MechaFlounder

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0459  
**Aliases:** MechaFlounder  
**Platforms:** Windows  

## Description
[MechaFlounder](https://attack.mitre.org/software/S0459) is a python-based remote access tool (RAT) that has been used by [APT39](https://attack.mitre.org/groups/G0087). The payload uses a combination of actor developed code and code snippets freely available online in development communities.(Citation: Unit 42 MechaFlounder March 2019)

## Techniques Used
- T1033: System Owner/User Discovery
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1059.003: Windows Command Shell
- T1059.006: Python
- T1071.001: Web Protocols
- T1105: Ingress Tool Transfer
- T1132.001: Standard Encoding
