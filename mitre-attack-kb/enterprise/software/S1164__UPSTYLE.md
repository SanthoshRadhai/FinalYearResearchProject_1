# S1164: UPSTYLE

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1164  
**Aliases:** UPSTYLE  
**Platforms:** Network Devices, Linux  

## Description
[UPSTYLE](https://attack.mitre.org/software/S1164) is a Python-based backdoor associated with exploitation of Palo Alto firewalls using CVE-2024-3400 in early 2024. [UPSTYLE](https://attack.mitre.org/software/S1164) has only been observed in relation to this exploitation activity, which involved attempted install on compromised devices by the threat actor UTA0218.(Citation: Volexity UPSTYLE 2024)(Citation: Palo Alto MidnightEclipse APR 2024)

## Techniques Used
- T1001.001: Junk Data
- T1027.013: Encrypted/Encoded File
- T1036: Masquerading
- T1057: Process Discovery
- T1059.006: Python
- T1070.004: File Deletion
- T1070.006: Timestomp
- T1102.003: One-Way Communication
- T1140: Deobfuscate/Decode Files or Information
- T1546: Event Triggered Execution
- T1665: Hide Infrastructure
- T1685.006: Clear Linux or Mac System Logs
