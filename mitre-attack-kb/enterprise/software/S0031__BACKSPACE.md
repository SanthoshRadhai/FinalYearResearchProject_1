# S0031: BACKSPACE

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0031  
**Aliases:** BACKSPACE, Lecna  
**Platforms:** Windows  

## Description
[BACKSPACE](https://attack.mitre.org/software/S0031) is a backdoor used by [APT30](https://attack.mitre.org/groups/G0013) that dates back to at least 2005. (Citation: FireEye APT30)

## Techniques Used
- T1012: Query Registry
- T1041: Exfiltration Over C2 Channel
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1090.001: Internal Proxy
- T1104: Multi-Stage Channels
- T1112: Modify Registry
- T1132.002: Non-Standard Encoding
- T1547.001: Registry Run Keys / Startup Folder
- T1547.009: Shortcut Modification
- T1686: Disable or Modify System Firewall
