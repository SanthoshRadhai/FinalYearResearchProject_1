# S1099: Samurai

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1099  
**Aliases:** Samurai  
**Platforms:** Windows  

## Description
[Samurai](https://attack.mitre.org/software/S1099) is a passive backdoor that has been used by [ToddyCat](https://attack.mitre.org/groups/G1022) since at least 2020. [Samurai](https://attack.mitre.org/software/S1099) allows arbitrary C# code execution and is used with multiple modules for remote administration and lateral movement.(Citation: Kaspersky ToddyCat June 2022)

## Techniques Used
- T1005: Data from Local System
- T1012: Query Registry
- T1027: Obfuscated Files or Information
- T1027.004: Compile After Delivery
- T1027.007: Dynamic API Resolution
- T1027.015: Compression
- T1036.005: Match Legitimate Resource Name or Location
- T1059.003: Windows Command Shell
- T1071.001: Web Protocols
- T1083: File and Directory Discovery
- T1090: Proxy
- T1095: Non-Application Layer Protocol
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1112: Modify Registry
- T1132.001: Standard Encoding
- T1518: Software Discovery
- T1543.003: Windows Service
- T1573.001: Symmetric Cryptography
