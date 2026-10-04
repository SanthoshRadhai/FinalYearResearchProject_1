# S1246: BeaverTail

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1246  
**Aliases:** BeaverTail  
**Platforms:** Linux, macOS, Windows  

## Description
[BeaverTail](https://attack.mitre.org/software/S1246) is a malware that has both a JavaScript and C++ variant.  Active since 2022, [BeaverTail](https://attack.mitre.org/software/S1246) is capable of stealing logins from browsers and serves as a downloader for second stage payloads. [BeaverTail](https://attack.mitre.org/software/S1246) has previously been leveraged by North Korea-affiliated actors identified as DeceptiveDevelopment or [Contagious Interview](https://attack.mitre.org/groups/G1052). [BeaverTail](https://attack.mitre.org/software/S1246) has been delivered to victims through code repository sites and has been embedded within malicious attachments.(Citation: PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023)(Citation: Esentire ContagiousInterview BeaverTail InvisibleFerret November 2024)(Citation: ESET Contagious Interview BeaverTail InvisibleFerret February 2025)(Citation: Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024)

## Techniques Used
- T1001.001: Junk Data
- T1005: Data from Local System
- T1027.013: Encrypted/Encoded File
- T1036: Masquerading
- T1041: Exfiltration Over C2 Channel
- T1059.007: JavaScript
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1074.001: Local Data Staging
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1124: System Time Discovery
- T1195.001: Compromise Software Dependencies and Development Tools
- T1204.002: Malicious File
- T1217: Browser Information Discovery
- T1555: Credentials from Password Stores
- T1555.001: Keychain
- T1555.003: Credentials from Web Browsers
- T1560.001: Archive via Utility
- T1571: Non-Standard Port
- T1654: Log Enumeration
- T1657: Financial Theft
