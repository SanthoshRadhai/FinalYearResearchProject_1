# S0447: Lokibot

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0447  
**Aliases:** Lokibot  
**Platforms:** Windows  

## Description
[Lokibot](https://attack.mitre.org/software/S0447) is a widely distributed information stealer that was first reported in 2015. It is designed to steal sensitive information such as usernames, passwords, cryptocurrency wallets, and other credentials. [Lokibot](https://attack.mitre.org/software/S0447) can also create a backdoor into infected systems to allow an attacker to install additional payloads.(Citation: Infoblox Lokibot January 2019)(Citation: Morphisec Lokibot April 2020)(Citation: CISA Lokibot September 2020)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1027: Obfuscated Files or Information
- T1027.002: Software Packing
- T1033: System Owner/User Discovery
- T1041: Exfiltration Over C2 Channel
- T1053: Scheduled Task/Job
- T1053.005: Scheduled Task
- T1055.012: Process Hollowing
- T1056.001: Keylogging
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1112: Modify Registry
- T1140: Deobfuscate/Decode Files or Information
- T1204.002: Malicious File
- T1497.003: Time Based Checks
- T1548.002: Bypass User Account Control
- T1555: Credentials from Password Stores
- T1555.003: Credentials from Web Browsers
- T1564.001: Hidden Files and Directories
- T1566.001: Spearphishing Attachment
- T1620: Reflective Code Loading
