# S1232: SplatDropper

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1232  
**Aliases:** SplatDropper  
**Platforms:** Windows  

## Description
[SplatDropper](https://attack.mitre.org/software/S1232) is a loader that utilizes native windows API to deliver its payload to the victim environment.  [SplatDropper](https://attack.mitre.org/software/S1232) has been delivered through RAR archives and used legitimate executable for DLL side-loading.  [SplatDropper](https://attack.mitre.org/software/S1232) is known to be leveraged by [Mustang Panda](https://attack.mitre.org/groups/G0129) and was first observed utilized in 2025.

## Techniques Used
- T1027.007: Dynamic API Resolution
- T1027.013: Encrypted/Encoded File
- T1070.009: Clear Persistence
- T1106: Native API
- T1140: Deobfuscate/Decode Files or Information
- T1543.003: Windows Service
- T1553.002: Code Signing
- T1574.001: DLL
