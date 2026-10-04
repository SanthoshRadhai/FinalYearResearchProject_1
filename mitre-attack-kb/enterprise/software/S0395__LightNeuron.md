# S0395: LightNeuron

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0395  
**Aliases:** LightNeuron  
**Platforms:** Windows, Linux  

## Description
[LightNeuron](https://attack.mitre.org/software/S0395) is a sophisticated backdoor that has targeted Microsoft Exchange servers since at least 2014. [LightNeuron](https://attack.mitre.org/software/S0395) has been used by [Turla](https://attack.mitre.org/groups/G0010) to target diplomatic and foreign affairs-related organizations. The presence of certain strings in the malware suggests a Linux variant of [LightNeuron](https://attack.mitre.org/software/S0395) exists.(Citation: ESET LightNeuron May 2019)

## Techniques Used
- T1001.002: Steganography
- T1005: Data from Local System
- T1016: System Network Configuration Discovery
- T1020: Automated Exfiltration
- T1027.013: Encrypted/Encoded File
- T1029: Scheduled Transfer
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1071.003: Mail Protocols
- T1074.001: Local Data Staging
- T1082: System Information Discovery
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1114.002: Remote Email Collection
- T1119: Automated Collection
- T1140: Deobfuscate/Decode Files or Information
- T1505.002: Transport Agent
- T1560: Archive Collected Data
- T1565.002: Transmitted Data Manipulation
- T1573.001: Symmetric Cryptography
