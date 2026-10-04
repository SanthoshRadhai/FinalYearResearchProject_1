# S0654: ProLock

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0654  
**Aliases:** ProLock  
**Platforms:** Windows  

## Description
[ProLock](https://attack.mitre.org/software/S0654) is a ransomware strain that has been used in Big Game Hunting (BGH) operations since at least 2020, often obtaining initial access with [QakBot](https://attack.mitre.org/software/S0650). [ProLock](https://attack.mitre.org/software/S0654) is the successor to PwndLocker ransomware which was found to contain a bug allowing decryption without ransom payment in 2019.(Citation: Group IB Ransomware September 2020)

## Techniques Used
- T1027.003: Steganography
- T1047: Windows Management Instrumentation
- T1068: Exploitation for Privilege Escalation
- T1070.004: File Deletion
- T1197: BITS Jobs
- T1486: Data Encrypted for Impact
- T1490: Inhibit System Recovery
