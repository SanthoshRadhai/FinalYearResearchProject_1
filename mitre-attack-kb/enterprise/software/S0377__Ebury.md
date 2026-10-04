# S0377: Ebury

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0377  
**Aliases:** Ebury  
**Platforms:** Linux  

## Description
[Ebury](https://attack.mitre.org/software/S0377) is an OpenSSH backdoor and credential stealer targeting Linux servers and container hosts developed by [Windigo](https://attack.mitre.org/groups/G0124). [Ebury](https://attack.mitre.org/software/S0377) is primarily installed through modifying shared libraries (`.so` files) executed by the legitimate OpenSSH program. First seen in 2009, [Ebury](https://attack.mitre.org/software/S0377) has been used to maintain a botnet of servers, deploy additional malware, and steal cryptocurrency wallets, credentials, and credit card details.(Citation: ESET Ebury Feb 2014)(Citation: BleepingComputer Ebury March 2017)(Citation: ESET Ebury Oct 2017)(Citation: ESET Ebury May 2024)

## Techniques Used
- T1008: Fallback Channels
- T1014: Rootkit
- T1020: Automated Exfiltration
- T1027: Obfuscated Files or Information
- T1041: Exfiltration Over C2 Channel
- T1059.004: Unix Shell
- T1059.006: Python
- T1071.004: DNS
- T1129: Shared Modules
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1552.004: Private Keys
- T1553.002: Code Signing
- T1554: Compromise Host Software Binary
- T1556: Modify Authentication Process
- T1556.003: Pluggable Authentication Modules
- T1568.002: Domain Generation Algorithms
- T1573.001: Symmetric Cryptography
- T1574.006: Dynamic Linker Hijacking
- T1685: Disable or Modify Tools
- T1685.004: Disable or Modify Linux Audit System Log
