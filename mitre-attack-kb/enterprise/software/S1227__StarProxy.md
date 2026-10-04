# S1227: StarProxy

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1227  
**Aliases:** StarProxy  
**Platforms:** Windows  

## Description
[StarProxy](https://attack.mitre.org/software/S1227) is custom malware used by [Mustang Panda](https://attack.mitre.org/groups/G0129) as a post-compromise tool, to enable proxying of traffic between the infected machine and other machines on the same network. (Citation: Zscaler)

## Techniques Used
- T1001.003: Protocol or Service Impersonation
- T1059: Command and Scripting Interpreter
- T1090.001: Internal Proxy
- T1095: Non-Application Layer Protocol
- T1106: Native API
- T1124: System Time Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1573.001: Symmetric Cryptography
- T1574.001: DLL
