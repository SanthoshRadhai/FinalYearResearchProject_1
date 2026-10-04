# S1111: DarkGate

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1111  
**Aliases:** DarkGate  
**Platforms:** Windows  

## Description
[DarkGate](https://attack.mitre.org/software/S1111) first emerged in 2018 and has evolved into an initial access and data gathering tool associated with various criminal cyber operations. Written in Delphi and named "DarkGate" by its author, [DarkGate](https://attack.mitre.org/software/S1111) is associated with credential theft, cryptomining, cryptotheft, and pre-ransomware actions.(Citation: Ensilo Darkgate 2018) DarkGate use increased significantly starting in 2022 and is under active development by its author, who provides it as a Malware-as-a-Service offering.(Citation: Trellix Darkgate 2023)

## Techniques Used
- T1001: Data Obfuscation
- T1005: Data from Local System
- T1010: Application Window Discovery
- T1027: Obfuscated Files or Information
- T1027.013: Encrypted/Encoded File
- T1036: Masquerading
- T1036.003: Rename Legitimate Utilities
- T1036.007: Double File Extension
- T1041: Exfiltration Over C2 Channel
- T1047: Windows Management Instrumentation
- T1055.012: Process Hollowing
- T1056.001: Keylogging
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1059.010: AutoHotKey & AutoIT
- T1070.004: File Deletion
- T1071.004: DNS
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1098.007: Additional Local or Domain Groups
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1115: Clipboard Data
- T1119: Automated Collection
- T1124: System Time Discovery
- T1134.004: Parent PID Spoofing
- T1136.001: Local Account
- T1140: Deobfuscate/Decode Files or Information
- T1204.002: Malicious File
- T1480: Execution Guardrails
- T1486: Data Encrypted for Impact
- T1490: Inhibit System Recovery
- T1496.001: Compute Hijacking
- T1497.001: System Checks
- T1518.001: Security Software Discovery
- T1529: System Shutdown/Reboot
- T1539: Steal Web Session Cookie
- T1547.001: Registry Run Keys / Startup Folder
- T1548.002: Bypass User Account Control
- T1552: Unsecured Credentials
- T1555: Credentials from Password Stores
- T1561.001: Disk Content Wipe
- T1564.001: Hidden Files and Directories
- T1566.001: Spearphishing Attachment
- T1566.002: Spearphishing Link
- T1569.002: Service Execution
- T1574: Hijack Execution Flow
- T1574.001: DLL
- T1574.007: Path Interception by PATH Environment Variable
- T1583.001: Domains
- T1614: System Location Discovery
- T1622: Debugger Evasion
- T1657: Financial Theft
- T1665: Hide Infrastructure
- T1680: Local Storage Discovery
- T1685: Disable or Modify Tools
