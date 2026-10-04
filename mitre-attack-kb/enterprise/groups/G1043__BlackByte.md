# G1043: BlackByte

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G1043  
**Aliases:** BlackByte, Hecamede  

## Description
[BlackByte](https://attack.mitre.org/groups/G1043) is a ransomware threat actor operating since at least 2021. [BlackByte](https://attack.mitre.org/groups/G1043) is associated with several versions of ransomware also labeled [BlackByte Ransomware](https://attack.mitre.org/software/S1180). [BlackByte](https://attack.mitre.org/groups/G1043) ransomware operations initially used a common encryption key allowing for the development of a universal decryptor, but subsequent versions such as [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) use more robust encryption mechanisms. [BlackByte](https://attack.mitre.org/groups/G1043) is notable for operations targeting critical infrastructure entities among other targets across North America.(Citation: FBI BlackByte 2022)(Citation: Picus BlackByte 2022)(Citation: Symantec BlackByte 2022)(Citation: Microsoft BlackByte 2023)(Citation: Cisco BlackByte 2024)

## Techniques Used
- T1003: OS Credential Dumping
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1018: Remote System Discovery
- T1021.001: Remote Desktop Protocol
- T1021.002: SMB/Windows Admin Shares
- T1036.008: Masquerade File Type
- T1041: Exfiltration Over C2 Channel
- T1046: Network Service Discovery
- T1047: Windows Management Instrumentation
- T1053.005: Scheduled Task
- T1055: Process Injection
- T1055.012: Process Hollowing
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1068: Exploitation for Privilege Escalation
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1078: Valid Accounts
- T1078.002: Domain Accounts
- T1082: System Information Discovery
- T1087.002: Domain Account
- T1105: Ingress Tool Transfer
- T1112: Modify Registry
- T1134.003: Make and Impersonate Token
- T1135: Network Share Discovery
- T1136.002: Domain Account
- T1140: Deobfuscate/Decode Files or Information
- T1190: Exploit Public-Facing Application
- T1219: Remote Access Tools
- T1480: Execution Guardrails
- T1482: Domain Trust Discovery
- T1486: Data Encrypted for Impact
- T1490: Inhibit System Recovery
- T1491.001: Internal Defacement
- T1505.003: Web Shell
- T1518.001: Security Software Discovery
- T1543.003: Windows Service
- T1547.001: Registry Run Keys / Startup Folder
- T1560: Archive Collected Data
- T1567: Exfiltration Over Web Service
- T1569.002: Service Execution
- T1570: Lateral Tool Transfer
- T1583.003: Virtual Private Server
- T1608.001: Upload Malware
- T1614.001: System Language Discovery
- T1685: Disable or Modify Tools
- T1686: Disable or Modify System Firewall
