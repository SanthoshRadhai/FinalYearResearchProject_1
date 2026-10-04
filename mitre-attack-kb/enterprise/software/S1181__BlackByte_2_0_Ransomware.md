# S1181: BlackByte 2.0 Ransomware

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1181  
**Aliases:** BlackByte 2.0 Ransomware  
**Platforms:** Windows  

## Description
[BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) is a replacement for [BlackByte Ransomware](https://attack.mitre.org/software/S1180). Unlike [BlackByte Ransomware](https://attack.mitre.org/software/S1180), [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) does not have a common key for victim decryption. [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) remains uniquely associated with [BlackByte](https://attack.mitre.org/groups/G1043) operations.(Citation: Microsoft BlackByte 2023)

## Techniques Used
- T1055: Process Injection
- T1068: Exploitation for Privilege Escalation
- T1070.004: File Deletion
- T1070.006: Timestomp
- T1112: Modify Registry
- T1135: Network Share Discovery
- T1486: Data Encrypted for Impact
- T1489: Service Stop
- T1490: Inhibit System Recovery
- T1569.002: Service Execution
- T1686.003: Windows Host Firewall
