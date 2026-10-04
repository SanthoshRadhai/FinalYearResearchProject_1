# S0330: Zeus Panda

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0330  
**Aliases:** Zeus Panda  
**Platforms:** Windows  

## Description
[Zeus Panda](https://attack.mitre.org/software/S0330) is a Trojan designed to steal banking information and other sensitive credentials for exfiltration. [Zeus Panda](https://attack.mitre.org/software/S0330)’s original source code was leaked in 2011, allowing threat actors to use its source code as a basis for new malware variants. It is mainly used to target Windows operating systems ranging from Windows XP through Windows 10.(Citation: Talos Zeus Panda Nov 2017)(Citation: GDATA Zeus Panda June 2017)

## Techniques Used
- T1012: Query Registry
- T1027.010: Command Obfuscation
- T1027.013: Encrypted/Encoded File
- T1055.002: Portable Executable Injection
- T1056.001: Keylogging
- T1056.004: Credential API Hooking
- T1057: Process Discovery
- T1059: Command and Scripting Interpreter
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1112: Modify Registry
- T1113: Screen Capture
- T1115: Clipboard Data
- T1124: System Time Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1518.001: Security Software Discovery
- T1547.001: Registry Run Keys / Startup Folder
- T1614.001: System Language Discovery
