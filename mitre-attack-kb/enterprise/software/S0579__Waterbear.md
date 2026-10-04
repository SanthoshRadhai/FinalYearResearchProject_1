# S0579: Waterbear

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0579  
**Aliases:** Waterbear  
**Platforms:** Windows  

## Description
[Waterbear](https://attack.mitre.org/software/S0579) is modular malware attributed to [BlackTech](https://attack.mitre.org/groups/G0098) that has been used primarily for lateral movement, decrypting, and triggering payloads and is capable of hiding network behaviors.(Citation: Trend Micro Waterbear December 2019)

## Techniques Used
- T1012: Query Registry
- T1027.005: Indicator Removal from Tools
- T1027.013: Encrypted/Encoded File
- T1049: System Network Connections Discovery
- T1055: Process Injection
- T1055.003: Thread Execution Hijacking
- T1057: Process Discovery
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1112: Modify Registry
- T1140: Deobfuscate/Decode Files or Information
- T1518.001: Security Software Discovery
- T1574.001: DLL
- T1685: Disable or Modify Tools
