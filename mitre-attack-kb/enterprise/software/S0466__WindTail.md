# S0466: WindTail

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0466  
**Aliases:** WindTail  
**Platforms:** macOS  

## Description
[WindTail](https://attack.mitre.org/software/S0466) is a macOS surveillance implant used by [Windshift](https://attack.mitre.org/groups/G0112). [WindTail](https://attack.mitre.org/software/S0466) shares code similarities with Hack Back aka KitM OSX.(Citation: SANS Windshift August 2018)(Citation: objective-see windtail1 dec 2018)(Citation: objective-see windtail2 jan 2019)

## Techniques Used
- T1027.013: Encrypted/Encoded File
- T1027.015: Compression
- T1036: Masquerading
- T1036.001: Invalid Code Signature
- T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol
- T1059.004: Unix Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1083: File and Directory Discovery
- T1106: Native API
- T1119: Automated Collection
- T1124: System Time Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1560.001: Archive via Utility
- T1564.003: Hidden Window
