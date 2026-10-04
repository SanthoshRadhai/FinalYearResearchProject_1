# S1207: XLoader

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1207  
**Aliases:** XLoader, Formbook  
**Platforms:** Windows  

## Description
[XLoader](https://attack.mitre.org/software/S1207) is an infostealer malware in use since at least 2016. Previously known and sometimes still referred to as Formbook, [XLoader](https://attack.mitre.org/software/S1207) is a Malware as a Service (MaaS) known for stealing data from web browsers, email clients and File Transfer Protocol (FTP) applications.(Citation: Zscaler XLoader 2025)(Citation: ANY.RUN XLoader 2023)(Citation: CheckPoint XLoader 2022)(Citation: Acronis XLoader 2021)(Citation: Google XLoader 2017)

## Techniques Used
- T1027.002: Software Packing
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1053.005: Scheduled Task
- T1055.004: Asynchronous Procedure Call
- T1055.012: Process Hollowing
- T1056.001: Keylogging
- T1059.010: AutoHotKey & AutoIT
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1106: Native API
- T1113: Screen Capture
- T1115: Clipboard Data
- T1140: Deobfuscate/Decode Files or Information
- T1185: Browser Session Hijacking
- T1203: Exploitation for Client Execution
- T1497: Virtualization/Sandbox Evasion
- T1497.001: System Checks
- T1529: System Shutdown/Reboot
- T1539: Steal Web Session Cookie
- T1547.001: Registry Run Keys / Startup Folder
- T1555: Credentials from Password Stores
- T1555.003: Credentials from Web Browsers
- T1566.001: Spearphishing Attachment
- T1583.001: Domains
- T1622: Debugger Evasion
- T1685: Disable or Modify Tools
