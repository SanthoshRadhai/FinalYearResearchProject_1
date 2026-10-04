# S1185: LightSpy

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1185  
**Aliases:** LightSpy  
**Platforms:** Android, Windows, iOS, macOS  

## Description
First observed in 2018, LightSpy is a modular malware family that initially targeted iOS devices in Southern Asia before expanding to Android and macOS platforms. It consists of a downloader, a main executable that manages network communications, and functionality-specific modules, typically implemented as `.dylib` files (iOS, macOS) or `.apk` files (Android). LightSpy can collect VoIP call recordings, SMS messages, and credential stores, which are then exfiltrated to a command and control (C2) server.(Citation: MelikovBlackBerry LightSpy 2024)

## Techniques Used
- T1398: Boot or Logon Initialization Scripts
- T1404: Exploitation for Privilege Escalation
- T1406: Obfuscated Files or Information
- T1409: Stored Application Data
- T1418: Software Discovery
- T1421: System Network Connections Discovery
- T1422: System Network Configuration Discovery
- T1422.002: Wi-Fi Discovery
- T1423: Network Service Scanning
- T1424: Process Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1437.001: Web Protocols
- T1456: Drive-By Compromise
- T1509: Non-Standard Port
- T1512: Video Capture
- T1513: Screen Capture
- T1532: Archive Collected Data
- T1533: Data from Local System
- T1544: Ingress Tool Transfer
- T1575: Native API
- T1582: SMS Control
- T1623: Command and Scripting Interpreter
- T1631: Process Injection
- T1634.001: Keychain
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1642: Endpoint Denial of Service
- T1646: Exfiltration Over C2 Channel
- T1655: Masquerading
- T1658: Exploitation for Client Execution
- T1660: Phishing
- T1662: Data Destruction
