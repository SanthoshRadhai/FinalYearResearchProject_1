# S0601: Hildegard

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0601  
**Aliases:** Hildegard  
**Platforms:** Linux, Containers, IaaS  

## Description
[Hildegard](https://attack.mitre.org/software/S0601) is malware that targets misconfigured kubelets for initial access and runs cryptocurrency miner operations. The malware was first observed in January 2021. The TeamTNT activity group is believed to be behind [Hildegard](https://attack.mitre.org/software/S0601). (Citation: Unit 42 Hildegard Malware)

## Techniques Used
- T1014: Rootkit
- T1027.002: Software Packing
- T1027.013: Encrypted/Encoded File
- T1036.004: Masquerade Task or Service
- T1046: Network Service Discovery
- T1059.004: Unix Shell
- T1068: Exploitation for Privilege Escalation
- T1070.003: Clear Command History
- T1070.004: File Deletion
- T1071: Application Layer Protocol
- T1082: System Information Discovery
- T1102: Web Service
- T1105: Ingress Tool Transfer
- T1133: External Remote Services
- T1136.001: Local Account
- T1140: Deobfuscate/Decode Files or Information
- T1219: Remote Access Tools
- T1496.001: Compute Hijacking
- T1543.002: Systemd Service
- T1552.001: Credentials In Files
- T1552.004: Private Keys
- T1552.005: Cloud Instance Metadata API
- T1574.006: Dynamic Linker Hijacking
- T1609: Container Administration Command
- T1611: Escape to Host
- T1613: Container and Resource Discovery
- T1685: Disable or Modify Tools
