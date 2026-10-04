# S0266: TrickBot

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0266  
**Aliases:** TrickBot, Totbrick, TSPY_TRICKLOAD  
**Platforms:** Windows  

## Description
[TrickBot](https://attack.mitre.org/software/S0266) is a Trojan spyware program written in C++ that first emerged in September 2016 as a possible successor to [Dyre](https://attack.mitre.org/software/S0024). [TrickBot](https://attack.mitre.org/software/S0266) was developed and initially used by [Wizard Spider](https://attack.mitre.org/groups/G0102) for targeting banking sites in North America, Australia, and throughout Europe; it has since been used against all sectors worldwide as part of "big game hunting" ransomware campaigns.(Citation: S2 Grupo TrickBot June 2017)(Citation: Fidelis TrickBot Oct 2016)(Citation: IBM TrickBot Nov 2016)(Citation: CrowdStrike Wizard Spider October 2020)

## Techniques Used
- T1005: Data from Local System
- T1007: System Service Discovery
- T1008: Fallback Channels
- T1016: System Network Configuration Discovery
- T1018: Remote System Discovery
- T1021.005: VNC
- T1027: Obfuscated Files or Information
- T1027.002: Software Packing
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1036: Masquerading
- T1041: Exfiltration Over C2 Channel
- T1053.005: Scheduled Task
- T1055: Process Injection
- T1055.012: Process Hollowing
- T1056.004: Credential API Hooking
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1069: Permission Groups Discovery
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087.001: Local Account
- T1087.003: Email Account
- T1090.002: External Proxy
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1110.004: Credential Stuffing
- T1112: Modify Registry
- T1132.001: Standard Encoding
- T1135: Network Share Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1185: Browser Session Hijacking
- T1204.002: Malicious File
- T1210: Exploitation of Remote Services
- T1219: Remote Access Tools
- T1482: Domain Trust Discovery
- T1495: Firmware Corruption
- T1497.003: Time Based Checks
- T1542.003: Bootkit
- T1543.003: Windows Service
- T1547.001: Registry Run Keys / Startup Folder
- T1552.001: Credentials In Files
- T1552.002: Credentials in Registry
- T1553.002: Code Signing
- T1555.003: Credentials from Web Browsers
- T1555.005: Password Managers
- T1559.001: Component Object Model
- T1564.003: Hidden Window
- T1566.001: Spearphishing Attachment
- T1566.002: Spearphishing Link
- T1571: Non-Standard Port
- T1573.001: Symmetric Cryptography
- T1685: Disable or Modify Tools
