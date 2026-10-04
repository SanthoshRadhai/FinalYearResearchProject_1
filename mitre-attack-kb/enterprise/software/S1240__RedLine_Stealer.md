# S1240: RedLine Stealer

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1240  
**Aliases:** RedLine Stealer  
**Platforms:** Windows  

## Description
[RedLine Stealer](https://attack.mitre.org/software/S1240) is an information-stealer malware variant first identified in 2020.(Citation: ESET RedLine Stealer November 2024)(Citation: Proofpoint RedLine Stealer March 2020)(Citation: Splunk RedLine Stealer June 2023)  [RedLine Stealer](https://attack.mitre.org/software/S1240) is a Malware as a Service (MaaS) and was reportedly sold as either a one-time purchase or a monthly subscription service.(Citation: ESET RedLine Stealer November 2024)(Citation: Veriti RedLine Stealer MAAS April 2023)   Information obtained from [RedLine Stealer](https://attack.mitre.org/software/S1240) has been known to be sold on the deep and dark web to Initial Access Brokers (IABs), who use or resell the stolen credentials for further intrusions.(Citation: Kroll RedLine Stealer August 2024)(Citation: Veriti RedLine Stealer MAAS April 2023)

## Techniques Used
- T1005: Data from Local System
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1027.002: Software Packing
- T1027.010: Command Obfuscation
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1036: Masquerading
- T1041: Exfiltration Over C2 Channel
- T1053.005: Scheduled Task
- T1059.003: Windows Command Shell
- T1059.011: Lua
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1087.001: Local Account
- T1102: Web Service
- T1105: Ingress Tool Transfer
- T1113: Screen Capture
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1204.002: Malicious File
- T1217: Browser Information Discovery
- T1218.007: Msiexec
- T1480: Execution Guardrails
- T1497: Virtualization/Sandbox Evasion
- T1518: Software Discovery
- T1518.001: Security Software Discovery
- T1539: Steal Web Session Cookie
- T1553.002: Code Signing
- T1555: Credentials from Password Stores
- T1555.003: Credentials from Web Browsers
- T1614: System Location Discovery
- T1614.001: System Language Discovery
- T1657: Financial Theft
- T1685: Disable or Modify Tools
