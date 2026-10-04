# S0352: OSX_OCEANLOTUS.D

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0352  
**Aliases:** OSX_OCEANLOTUS.D, Backdoor.MacOS.OCEANLOTUS.F  
**Platforms:** macOS  

## Description
[OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) is a macOS backdoor used by [APT32](https://attack.mitre.org/groups/G0050). First discovered in 2015, [APT32](https://attack.mitre.org/groups/G0050) has continued to make improvements using a plugin architecture to extend capabilities, specifically using `.dylib` files. [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) can also determine it's permission level and execute according to access type (`root` or `user`).(Citation: Unit42 OceanLotus 2017)(Citation: TrendMicro MacOS April 2018)(Citation: Trend Micro MacOS Backdoor November 2020)

## Techniques Used
- T1005: Data from Local System
- T1016: System Network Configuration Discovery
- T1027.002: Software Packing
- T1027.013: Encrypted/Encoded File
- T1036.004: Masquerade Task or Service
- T1036.008: Masquerade File Type
- T1059.001: PowerShell
- T1059.004: Unix Shell
- T1059.005: Visual Basic
- T1070.004: File Deletion
- T1070.006: Timestomp
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1095: Non-Application Layer Protocol
- T1105: Ingress Tool Transfer
- T1129: Shared Modules
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1222.002: Linux and Mac Permissions
- T1497.001: System Checks
- T1543.001: Launch Agent
- T1543.004: Launch Daemon
- T1553.001: Gatekeeper Bypass
- T1560.002: Archive via Library
- T1560.003: Archive via Custom Method
- T1564.001: Hidden Files and Directories
- T1571: Non-Standard Port
- T1573.001: Symmetric Cryptography
