# S0484: Carberp

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0484  
**Aliases:** Carberp  
**Platforms:** Windows  

## Description
[Carberp](https://attack.mitre.org/software/S0484) is a credential and information stealing malware that has been active since at least 2009. [Carberp](https://attack.mitre.org/software/S0484)'s source code was leaked online in 2013, and subsequently used as the foundation for the [Carbanak](https://attack.mitre.org/software/S0030) backdoor.(Citation: Trend Micro Carberp February 2014)(Citation: KasperskyCarbanak)(Citation: RSA Carbanak November 2017)

## Techniques Used
- T1012: Query Registry
- T1014: Rootkit
- T1021.005: VNC
- T1027.013: Encrypted/Encoded File
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1055.001: Dynamic-link Library Injection
- T1055.004: Asynchronous Procedure Call
- T1056.004: Credential API Hooking
- T1057: Process Discovery
- T1068: Exploitation for Privilege Escalation
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1113: Screen Capture
- T1185: Browser Session Hijacking
- T1497: Virtualization/Sandbox Evasion
- T1518.001: Security Software Discovery
- T1542.003: Bootkit
- T1547.001: Registry Run Keys / Startup Folder
- T1555: Credentials from Password Stores
- T1555.003: Credentials from Web Browsers
- T1564.001: Hidden Files and Directories
- T1685: Disable or Modify Tools
