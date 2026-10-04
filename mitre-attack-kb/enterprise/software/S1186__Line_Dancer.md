# S1186: Line Dancer

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1186  
**Aliases:** Line Dancer  
**Platforms:** Network Devices  

## Description
[Line Dancer](https://attack.mitre.org/software/S1186) is a memory-only Lua-based shellcode loader associated with the [ArcaneDoor](https://attack.mitre.org/campaigns/C0046) campaign. [Line Dancer](https://attack.mitre.org/software/S1186) allows an adversary to upload and execute arbitrary shellcode on victim devices.(Citation: Cisco ArcaneDoor 2024)(Citation: CCCS ArcaneDoor 2024)

## Techniques Used
- T1014: Rootkit
- T1040: Network Sniffing
- T1041: Exfiltration Over C2 Channel
- T1059.008: Network Device CLI
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1653: Power Settings
- T1690: Prevent Command History Logging
