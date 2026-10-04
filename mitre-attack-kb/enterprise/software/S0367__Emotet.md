# S0367: Emotet

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0367  
**Aliases:** Emotet, Geodo  
**Platforms:** Windows  

## Description
[Emotet](https://attack.mitre.org/software/S0367) is a modular malware variant which is primarily used as a downloader for other malware variants such as [TrickBot](https://attack.mitre.org/software/S0266) and [IcedID](https://attack.mitre.org/software/S0483). Emotet first emerged in June 2014, initially targeting the financial sector, and has expanded to multiple verticals over time.(Citation: Trend Micro Banking Malware Jan 2019)

## Techniques Used
- T1003.001: LSASS Memory
- T1016.002: Wi-Fi Discovery
- T1021.002: SMB/Windows Admin Shares
- T1027.001: Binary Padding
- T1027.002: Software Packing
- T1027.009: Embedded Payloads
- T1027.010: Command Obfuscation
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1036.004: Masquerade Task or Service
- T1040: Network Sniffing
- T1041: Exfiltration Over C2 Channel
- T1047: Windows Management Instrumentation
- T1053.005: Scheduled Task
- T1055.001: Dynamic-link Library Injection
- T1055.012: Process Hollowing
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1071.001: Web Protocols
- T1078.003: Local Accounts
- T1087.003: Email Account
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1110.001: Password Guessing
- T1114: Email Collection
- T1114.001: Local Email Collection
- T1132.001: Standard Encoding
- T1134.001: Token Impersonation/Theft
- T1135: Network Share Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1204.001: Malicious Link
- T1204.002: Malicious File
- T1210: Exploitation of Remote Services
- T1218.010: Regsvr32
- T1543.003: Windows Service
- T1547.001: Registry Run Keys / Startup Folder
- T1552.001: Credentials In Files
- T1555.003: Credentials from Web Browsers
- T1566.001: Spearphishing Attachment
- T1566.002: Spearphishing Link
- T1570: Lateral Tool Transfer
- T1571: Non-Standard Port
- T1573: Encrypted Channel
- T1573.001: Symmetric Cryptography
- T1620: Reflective Code Loading
