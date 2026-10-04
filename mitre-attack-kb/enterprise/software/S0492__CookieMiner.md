# S0492: CookieMiner

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0492  
**Aliases:** CookieMiner  
**Platforms:** macOS  

## Description
[CookieMiner](https://attack.mitre.org/software/S0492) is mac-based malware that targets information associated with cryptocurrency exchanges as well as enabling cryptocurrency mining on the victim system itself. It was first discovered in the wild in 2019.(Citation: Unit42 CookieMiner Jan 2019)

## Techniques Used
- T1005: Data from Local System
- T1027.010: Command Obfuscation
- T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol
- T1059.004: Unix Shell
- T1059.006: Python
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1140: Deobfuscate/Decode Files or Information
- T1496.001: Compute Hijacking
- T1518.001: Security Software Discovery
- T1539: Steal Web Session Cookie
- T1543.001: Launch Agent
- T1555.003: Credentials from Web Browsers
- T1686: Disable or Modify System Firewall
