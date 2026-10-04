# S0559: SUNBURST

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0559  
**Aliases:** SUNBURST, Solorigate  
**Platforms:** Windows  

## Description
[SUNBURST](https://attack.mitre.org/software/S0559) is a trojanized DLL designed to fit within the SolarWinds Orion software update framework. It was used by [APT29](https://attack.mitre.org/groups/G0016) since at least February 2020.(Citation: SolarWinds Sunburst Sunspot Update January 2021)(Citation: Microsoft Deep Dive Solorigate January 2021)

## Techniques Used
- T1001.001: Junk Data
- T1001.002: Steganography
- T1001.003: Protocol or Service Impersonation
- T1005: Data from Local System
- T1007: System Service Discovery
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1027: Obfuscated Files or Information
- T1027.005: Indicator Removal from Tools
- T1027.015: Compression
- T1033: System Owner/User Discovery
- T1036.005: Match Legitimate Resource Name or Location
- T1047: Windows Management Instrumentation
- T1057: Process Discovery
- T1059.005: Visual Basic
- T1070: Indicator Removal
- T1070.004: File Deletion
- T1070.007: Clear Network Connection History and Configurations
- T1070.009: Clear Persistence
- T1071.001: Web Protocols
- T1071.004: DNS
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1112: Modify Registry
- T1124: System Time Discovery
- T1132.001: Standard Encoding
- T1218.011: Rundll32
- T1497.001: System Checks
- T1497.003: Time Based Checks
- T1518.001: Security Software Discovery
- T1546.012: Image File Execution Options Injection
- T1553.002: Code Signing
- T1568: Dynamic Resolution
- T1573.001: Symmetric Cryptography
- T1685: Disable or Modify Tools
