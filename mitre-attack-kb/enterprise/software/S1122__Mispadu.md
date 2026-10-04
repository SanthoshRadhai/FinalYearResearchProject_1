# S1122: Mispadu

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1122  
**Aliases:** Mispadu  
**Platforms:** Windows  

## Description
[Mispadu](https://attack.mitre.org/software/S1122) is a banking trojan written in Delphi that was first observed in 2019 and uses a Malware-as-a-Service (MaaS) business model.(Citation: ESET Security Mispadu Facebook Ads 2019)(Citation: SCILabs Malteiro 2021) This malware is operated, managed, and sold by the [Malteiro](https://attack.mitre.org/groups/G1026) cybercriminal group.(Citation: SCILabs Malteiro 2021) [Mispadu](https://attack.mitre.org/software/S1122) has mainly been used to target victims in Brazil and Mexico, and has also had confirmed operations throughout Latin America and Europe.(Citation: SCILabs Malteiro 2021)(Citation: SCILabs URSA/Mispadu Evolution 2023)(Citation: Segurança Informática URSA Sophisticated Loader 2020)

## Techniques Used
- T1027.013: Encrypted/Encoded File
- T1041: Exfiltration Over C2 Channel
- T1055: Process Injection
- T1056.001: Keylogging
- T1056.002: GUI Input Capture
- T1057: Process Discovery
- T1059.005: Visual Basic
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1106: Native API
- T1113: Screen Capture
- T1115: Clipboard Data
- T1140: Deobfuscate/Decode Files or Information
- T1176.001: Browser Extensions
- T1204.002: Malicious File
- T1217: Browser Information Discovery
- T1218.007: Msiexec
- T1218.011: Rundll32
- T1497.001: System Checks
- T1518.001: Security Software Discovery
- T1547.001: Registry Run Keys / Startup Folder
- T1555: Credentials from Password Stores
- T1555.003: Credentials from Web Browsers
- T1566.002: Spearphishing Link
- T1573.002: Asymmetric Cryptography
- T1614.001: System Language Discovery
