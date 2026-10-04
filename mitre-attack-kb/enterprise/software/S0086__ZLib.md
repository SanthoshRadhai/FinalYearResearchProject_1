# S0086: ZLib

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0086  
**Aliases:** ZLib  
**Platforms:** Windows  

## Description
[ZLib](https://attack.mitre.org/software/S0086) is a full-featured backdoor that was used as a second-stage implant during [Operation Dust Storm](https://attack.mitre.org/campaigns/C0016) since at least 2014. [ZLib](https://attack.mitre.org/software/S0086) is malware and should not be confused with the legitimate compression library from which its name is derived.(Citation: Cylance Dust Storm)

## Techniques Used
- T1007: System Service Discovery
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1059.003: Windows Command Shell
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1113: Screen Capture
- T1543.003: Windows Service
- T1560.002: Archive via Library
