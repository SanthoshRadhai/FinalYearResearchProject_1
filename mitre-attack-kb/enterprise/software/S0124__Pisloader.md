# S0124: Pisloader

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0124  
**Aliases:** Pisloader  
**Platforms:** Windows  

## Description
[Pisloader](https://attack.mitre.org/software/S0124) is a malware family that is notable due to its use of DNS as a C2 protocol as well as its use of anti-analysis tactics. It has been used by [APT18](https://attack.mitre.org/groups/G0026) and is similar to another malware family, [HTTPBrowser](https://attack.mitre.org/software/S0070), that has been used by the group. (Citation: Palo Alto DNS Requests)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1027: Obfuscated Files or Information
- T1059.003: Windows Command Shell
- T1071.004: DNS
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1132.001: Standard Encoding
- T1547.001: Registry Run Keys / Startup Folder
