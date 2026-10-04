# S0658: XCSSET

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0658  
**Aliases:** XCSSET, OSX.DubRobber  
**Platforms:** macOS  

## Description
[XCSSET](https://attack.mitre.org/software/S0658) is a modular macOS malware family delivered through infected Xcode projects and executed when the project is compiled. Active since August 2020, it has been observed installing backdoors, spoofed browsers, collecting data, and encrypting user files. It is composed of SHC-compiled shell scripts and run-only AppleScripts, often hiding in apps that mimic system tools (such as Xcode, Mail, or Notes) or use familiar icons (like Launchpad) to avoid detection.(Citation: trendmicro xcsset xcode project 2020)(Citation: April 2021 TrendMicro XCSSET)(Citation: Microsoft March 2025 XCSSET)

## Techniques Used
- T1005: Data from Local System
- T1027.013: Encrypted/Encoded File
- T1036: Masquerading
- T1041: Exfiltration Over C2 Channel
- T1056.002: GUI Input Capture
- T1059.004: Unix Shell
- T1068: Exploitation for Privilege Escalation
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087: Account Discovery
- T1098.004: SSH Authorized Keys
- T1105: Ingress Tool Transfer
- T1113: Screen Capture
- T1195.001: Compromise Software Dependencies and Development Tools
- T1222.002: Linux and Mac Permissions
- T1486: Data Encrypted for Impact
- T1497.003: Time Based Checks
- T1518: Software Discovery
- T1518.001: Security Software Discovery
- T1539: Steal Web Session Cookie
- T1543.004: Launch Daemon
- T1546: Event Triggered Execution
- T1546.004: Unix Shell Configuration Modification
- T1548.006: TCC Manipulation
- T1553.001: Gatekeeper Bypass
- T1554: Compromise Host Software Binary
- T1560: Archive Collected Data
- T1564.001: Hidden Files and Directories
- T1569.001: Launchctl
- T1573.001: Symmetric Cryptography
- T1574.006: Dynamic Linker Hijacking
- T1614.001: System Language Discovery
- T1647: Plist File Modification
