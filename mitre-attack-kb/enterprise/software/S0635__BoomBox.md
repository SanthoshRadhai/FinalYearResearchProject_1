# S0635: BoomBox

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0635  
**Aliases:** BoomBox  
**Platforms:** Windows  

## Description
[BoomBox](https://attack.mitre.org/software/S0635) is a downloader responsible for executing next stage components that has been used by [APT29](https://attack.mitre.org/groups/G0016) since at least 2021.(Citation: MSTIC Nobelium Toolset May 2021)

## Techniques Used
- T1027: Obfuscated Files or Information
- T1033: System Owner/User Discovery
- T1036: Masquerading
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087.002: Domain Account
- T1087.003: Email Account
- T1102: Web Service
- T1105: Ingress Tool Transfer
- T1140: Deobfuscate/Decode Files or Information
- T1204.002: Malicious File
- T1218.011: Rundll32
- T1480: Execution Guardrails
- T1547.001: Registry Run Keys / Startup Folder
- T1567.002: Exfiltration to Cloud Storage
