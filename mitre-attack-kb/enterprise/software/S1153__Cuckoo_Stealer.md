# S1153: Cuckoo Stealer

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1153  
**Aliases:** Cuckoo Stealer  
**Platforms:** macOS  

## Description
[Cuckoo Stealer](https://attack.mitre.org/software/S1153) is a macOS malware with characteristics of spyware and an infostealer that has been in use since at least 2024. [Cuckoo Stealer](https://attack.mitre.org/software/S1153) is a universal Mach-O binary that can run on Intel or ARM-based Macs and has been spread through trojanized versions of various potentially unwanted programs or PUP's such as converters, cleaners, and uninstallers.(Citation: Kandji Cuckoo April 2024)(Citation: SentinelOne Cuckoo Stealer May 2024)

## Techniques Used
- T1027.008: Stripped Payloads
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1056.002: GUI Input Capture
- T1057: Process Discovery
- T1059.002: AppleScript
- T1059.004: Unix Shell
- T1071.001: Web Protocols
- T1074.001: Local Data Staging
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1095: Non-Application Layer Protocol
- T1113: Screen Capture
- T1140: Deobfuscate/Decode Files or Information
- T1217: Browser Information Discovery
- T1518: Software Discovery
- T1543.001: Launch Agent
- T1553.001: Gatekeeper Bypass
- T1555.001: Keychain
- T1564.001: Hidden Files and Directories
- T1569.001: Launchctl
- T1614: System Location Discovery
- T1614.001: System Language Discovery
- T1647: Plist File Modification
