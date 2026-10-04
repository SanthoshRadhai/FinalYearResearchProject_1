# S1180: BlackByte Ransomware

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1180  
**Aliases:** BlackByte Ransomware  
**Platforms:** Windows  

## Description
[BlackByte Ransomware](https://attack.mitre.org/software/S1180) is uniquely associated with [BlackByte](https://attack.mitre.org/groups/G1043) operations. [BlackByte Ransomware](https://attack.mitre.org/software/S1180) used a common key for infections, allowing for the creation of a universal decryptor.(Citation: Trustwave BlackByte 2021)(Citation: FBI BlackByte 2022) [BlackByte Ransomware](https://attack.mitre.org/software/S1180) was replaced in [BlackByte](https://attack.mitre.org/groups/G1043) operations by [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) by 2023.(Citation: Microsoft BlackByte 2023)(Citation: Cisco BlackByte 2024)

## Techniques Used
- T1012: Query Registry
- T1021.002: SMB/Windows Admin Shares
- T1027.013: Encrypted/Encoded File
- T1046: Network Service Discovery
- T1053.005: Scheduled Task
- T1059.007: JavaScript
- T1082: System Information Discovery
- T1106: Native API
- T1112: Modify Registry
- T1135: Network Share Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1222.001: Windows Permissions
- T1480: Execution Guardrails
- T1486: Data Encrypted for Impact
- T1490: Inhibit System Recovery
- T1497.001: System Checks
- T1518.001: Security Software Discovery
- T1570: Lateral Tool Transfer
- T1614.001: System Language Discovery
- T1685: Disable or Modify Tools
- T1689: Downgrade Attack
