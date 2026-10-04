# S1208: FjordPhantom

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1208  
**Aliases:** FjordPhantom  
**Platforms:** Android  

## Description
[FjordPhantom](https://attack.mitre.org/software/S1208) is a malicious Android application first discovered in September 2024 with targets in Southeast Asia, specifically Indonesia, Thailand, and Vietnam. [FjordPhantom](https://attack.mitre.org/software/S1208) was distributed through email and messaging applications. Once installed, the application launches a virtualization solution to steal important information, such as bank accounts, and to manipulate the user interface. The malicious activity from the virtualization solution runs alongside legitimate banking applications.(Citation: Promon FjordPhantom Oct2024)

## Techniques Used
- T1617: Hooking
- T1631: Process Injection
- T1655: Masquerading
- T1660: Phishing
- T1670: Virtualization Solution
