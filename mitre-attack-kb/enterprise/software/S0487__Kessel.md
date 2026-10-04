# S0487: Kessel

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0487  
**Aliases:** Kessel  
**Platforms:** Linux  

## Description
[Kessel](https://attack.mitre.org/software/S0487) is an advanced version of OpenSSH which acts as a custom backdoor, mainly acting to steal credentials and function as a bot. [Kessel](https://attack.mitre.org/software/S0487) has been active since its C2 domain began resolving in August 2018.(Citation: ESET ForSSHe December 2018)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1027.013: Encrypted/Encoded File
- T1030: Data Transfer Size Limits
- T1041: Exfiltration Over C2 Channel
- T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol
- T1059: Command and Scripting Interpreter
- T1082: System Information Discovery
- T1090: Proxy
- T1105: Ingress Tool Transfer
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1554: Compromise Host Software Binary
- T1556: Modify Authentication Process
- T1560: Archive Collected Data
