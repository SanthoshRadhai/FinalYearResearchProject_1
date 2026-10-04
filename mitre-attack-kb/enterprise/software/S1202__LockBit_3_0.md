# S1202: LockBit 3.0

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1202  
**Aliases:** LockBit 3.0, LockBit Black  
**Platforms:** Windows  

## Description
[LockBit 3.0](https://attack.mitre.org/software/S1202) is an evolution of the LockBit Ransomware-as-a-Service (RaaS) offering with similarities to BlackMatter and [BlackCat](https://attack.mitre.org/software/S1068) ransomware. [LockBit 3.0](https://attack.mitre.org/software/S1202) has been in use since at least June 2022 and features enhanced defense evasion and exfiltration tactics, robust encryption methods for Windows and VMware ESXi systems, and a more refined RaaS structure over its predecessors such as [LockBit 2.0](https://attack.mitre.org/software/S1199).(Citation: Sentinel Labs LockBit 3.0 JUL 2022)(Citation: Joint Cybersecurity Advisory LockBit JUN 2023)(Citation: Joint Cybersecurity Advisory LockBit 3.0 MAR 2023)(Citation: INCIBE-CERT LockBit MAR 2024)

## Techniques Used
- T1021.002: SMB/Windows Admin Shares
- T1027.002: Software Packing
- T1027.013: Encrypted/Encoded File
- T1057: Process Discovery
- T1059.001: PowerShell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1078.003: Local Accounts
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1106: Native API
- T1112: Modify Registry
- T1120: Peripheral Device Discovery
- T1132.001: Standard Encoding
- T1135: Network Share Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1218.003: CMSTP
- T1480: Execution Guardrails
- T1480.002: Mutual Exclusion
- T1484.001: Group Policy Modification
- T1486: Data Encrypted for Impact
- T1489: Service Stop
- T1490: Inhibit System Recovery
- T1543.003: Windows Service
- T1547.004: Winlogon Helper DLL
- T1548.002: Bypass User Account Control
- T1569.002: Service Execution
- T1573.001: Symmetric Cryptography
- T1614.001: System Language Discovery
- T1622: Debugger Evasion
- T1680: Local Storage Discovery
- T1685: Disable or Modify Tools
- T1685.005: Clear Windows Event Logs
- T1688: Safe Mode Boot
