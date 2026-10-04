# S1185: LightSpy

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1185  
**Aliases:** LightSpy  
**Platforms:** Android, Windows, iOS, macOS  

## Description
First observed in 2018, LightSpy is a modular malware family that initially targeted iOS devices in Southern Asia before expanding to Android and macOS platforms. It consists of a downloader, a main executable that manages network communications, and functionality-specific modules, typically implemented as `.dylib` files (iOS, macOS) or `.apk` files (Android). LightSpy can collect VoIP call recordings, SMS messages, and credential stores, which are then exfiltrated to a command and control (C2) server.(Citation: MelikovBlackBerry LightSpy 2024)

## Techniques Used
- T1027.001: Binary Padding
- T1027.013: Encrypted/Encoded File
- T1041: Exfiltration Over C2 Channel
- T1046: Network Service Discovery
- T1057: Process Discovery
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1113: Screen Capture
- T1123: Audio Capture
- T1129: Shared Modules
- T1217: Browser Information Discovery
- T1480: Execution Guardrails
- T1518: Software Discovery
- T1555.001: Keychain
