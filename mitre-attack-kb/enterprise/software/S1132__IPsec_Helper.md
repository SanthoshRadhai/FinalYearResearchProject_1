# S1132: IPsec Helper

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1132  
**Aliases:** IPsec Helper  
**Platforms:** Windows  

## Description
[IPsec Helper](https://attack.mitre.org/software/S1132) is a post-exploitation remote access tool linked to [Agrius](https://attack.mitre.org/groups/G1030) operations. This malware shares significant programming and functional overlaps with [Apostle](https://attack.mitre.org/software/S1133) ransomware, also linked to [Agrius](https://attack.mitre.org/groups/G1030). [IPsec Helper](https://attack.mitre.org/software/S1132) provides basic remote access tool functionality such as uploading files from victim systems, running commands, and deploying additional payloads.(Citation: SentinelOne Agrius 2021)

## Techniques Used
- T1005: Data from Local System
- T1027.013: Encrypted/Encoded File
- T1041: Exfiltration Over C2 Channel
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1070: Indicator Removal
- T1070.004: File Deletion
- T1070.009: Clear Persistence
- T1071.001: Web Protocols
- T1112: Modify Registry
- T1497.003: Time Based Checks
- T1569.002: Service Execution
- T1570: Lateral Tool Transfer
