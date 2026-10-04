# S1039: Bumblebee

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1039  
**Aliases:** Bumblebee  
**Platforms:** Windows  

## Description
[Bumblebee](https://attack.mitre.org/software/S1039) is a custom loader written in C++ that has been used by multiple threat actors, including possible initial access brokers, to download and execute additional payloads since at least March 2022. [Bumblebee](https://attack.mitre.org/software/S1039) has been linked to ransomware operations including [Conti](https://attack.mitre.org/software/S0575), Quantum, and Mountlocker and derived its name from the appearance of "bumblebee" in the user-agent.(Citation: Google EXOTIC LILY March 2022)(Citation: Proofpoint Bumblebee April 2022)(Citation: Symantec Bumblebee June 2022)

## Techniques Used
- T1005: Data from Local System
- T1008: Fallback Channels
- T1012: Query Registry
- T1027: Obfuscated Files or Information
- T1033: System Owner/User Discovery
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1047: Windows Management Instrumentation
- T1053.005: Scheduled Task
- T1055: Process Injection
- T1055.001: Dynamic-link Library Injection
- T1055.004: Asynchronous Procedure Call
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1070.004: File Deletion
- T1082: System Information Discovery
- T1102: Web Service
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1129: Shared Modules
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1204.001: Malicious Link
- T1204.002: Malicious File
- T1218.008: Odbcconf
- T1218.011: Rundll32
- T1497: Virtualization/Sandbox Evasion
- T1497.001: System Checks
- T1497.003: Time Based Checks
- T1518.001: Security Software Discovery
- T1548.002: Bypass User Account Control
- T1559.001: Component Object Model
- T1560: Archive Collected Data
- T1566.001: Spearphishing Attachment
- T1566.002: Spearphishing Link
- T1573.001: Symmetric Cryptography
- T1622: Debugger Evasion
