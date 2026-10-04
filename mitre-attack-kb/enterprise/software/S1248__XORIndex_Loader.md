# S1248: XORIndex Loader

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1248  
**Aliases:** XORIndex Loader  
**Platforms:** Windows  

## Description
[XORIndex Loader](https://attack.mitre.org/software/S1248) is a XOR-encoded loader that collects host data, decodes follow-on scripts and acts as a downloader for the [BeaverTail](https://attack.mitre.org/software/S1246) malware.  [XORIndex Loader](https://attack.mitre.org/software/S1248) was first reported in June 2025.  [XORIndex Loader](https://attack.mitre.org/software/S1248) has been leveraged by North Korea-affiliated threat actors identified as [Contagious Interview](https://attack.mitre.org/groups/G1052).  [XORIndex Loader](https://attack.mitre.org/software/S1248) has been delivered to victims through code repository sites utilizing typo squatting naming conventions of various npm packages.(Citation: Socket BeaverTail XORIndex HexEval Contagious Interview July 2025)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1027.010: Command Obfuscation
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1059.007: JavaScript
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1105: Ingress Tool Transfer
- T1140: Deobfuscate/Decode Files or Information
- T1614: System Location Discovery
