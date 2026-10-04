# S0661: FoggyWeb

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0661  
**Aliases:** FoggyWeb  
**Platforms:** Windows  

## Description
[FoggyWeb](https://attack.mitre.org/software/S0661) is a passive and highly-targeted backdoor capable of remotely exfiltrating sensitive information from a compromised Active Directory Federated Services (AD FS) server. It has been used by [APT29](https://attack.mitre.org/groups/G0016) since at least early April 2021.(Citation: MSTIC FoggyWeb September 2021)

## Techniques Used
- T1005: Data from Local System
- T1027.004: Compile After Delivery
- T1027.013: Encrypted/Encoded File
- T1036: Masquerading
- T1036.005: Match Legitimate Resource Name or Location
- T1040: Network Sniffing
- T1041: Exfiltration Over C2 Channel
- T1057: Process Discovery
- T1071.001: Web Protocols
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1129: Shared Modules
- T1140: Deobfuscate/Decode Files or Information
- T1550: Use Alternate Authentication Material
- T1552.004: Private Keys
- T1560.002: Archive via Library
- T1560.003: Archive via Custom Method
- T1573.001: Symmetric Cryptography
- T1574.001: DLL
- T1620: Reflective Code Loading
