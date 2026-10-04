# S1183: StrelaStealer

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1183  
**Aliases:** StrelaStealer  
**Platforms:** Windows  

## Description
[StrelaStealer](https://attack.mitre.org/software/S1183) is an information stealer malware variant first identified in November 2022 and active through late 2024. [StrelaStealer](https://attack.mitre.org/software/S1183) focuses on the automated identification, collection, and exfiltration of email credentials from email clients such as Outlook and Thunderbird.(Citation: DCSO StrelaStealer 2022)(Citation: PaloAlto StrelaStealer 2024)(Citation: Fortgale StrelaStealer 2023)(Citation: IBM StrelaStealer 2024)

## Techniques Used
- T1001: Data Obfuscation
- T1020: Automated Exfiltration
- T1027: Obfuscated Files or Information
- T1027.002: Software Packing
- T1027.013: Encrypted/Encoded File
- T1027.015: Compression
- T1027.016: Junk Code Insertion
- T1036: Masquerading
- T1036.003: Rename Legitimate Utilities
- T1036.005: Match Legitimate Resource Name or Location
- T1036.008: Masquerade File Type
- T1041: Exfiltration Over C2 Channel
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.007: JavaScript
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1105: Ingress Tool Transfer
- T1119: Automated Collection
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1204.002: Malicious File
- T1218.011: Rundll32
- T1480: Execution Guardrails
- T1480.002: Mutual Exclusion
- T1497: Virtualization/Sandbox Evasion
- T1518: Software Discovery
- T1552.001: Credentials In Files
- T1552.002: Credentials in Registry
- T1553.002: Code Signing
- T1566.001: Spearphishing Attachment
- T1574.001: DLL
- T1614.001: System Language Discovery
- T1622: Debugger Evasion
