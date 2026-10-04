# S9010: GlassWorm

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9010  
**Aliases:** GlassWorm  
**Platforms:** macOS, Windows  

## Description
[GlassWorm](https://attack.mitre.org/software/S9010) is a worm that propagated through supply chain attacks by compromising repository credentials from victim environments and having malicious payloads added to those compromised accounts for distribution to victims across the various development ecosystems.(Citation: Koi Glassworm InvisibleCode October 2025)(Citation: Aikido GlassWorm October 2025)(Citation: Socket GlassWorm January 2026)   [GlassWorm](https://attack.mitre.org/software/S9010) has numerous variants, including Rust binaries, encrypted JavaScript and a variant leveraging invisible Unicode characters that made reverse engineering difficult.(Citation: Koi Glassworm New Tricks December 2025)(Citation: Koi Glassworm InvisibleCode October 2025)(Citation: Koi GlassWorm Rust December 2025)  [GlassWorm](https://attack.mitre.org/software/S9010) has employed a unique command and control (C2) methodology using Solana blockchain.(Citation: Koi Glassworm Extensions November 2025)(Citation: Koi Glassworm InvisibleCode October 2025)   [GlassWorm](https://attack.mitre.org/software/S9010) was first reported in October 2025.(Citation: Koi Glassworm Extensions November 2025)(Citation: Koi Glassworm InvisibleCode October 2025)(Citation: Socket GlassWorm January 2026)

## Techniques Used
- T1005: Data from Local System
- T1008: Fallback Channels
- T1027.013: Encrypted/Encoded File
- T1027.018: Invisible Unicode
- T1036: Masquerading
- T1059.002: AppleScript
- T1059.007: JavaScript
- T1071.001: Web Protocols
- T1074.001: Local Data Staging
- T1082: System Information Discovery
- T1090.001: Internal Proxy
- T1102.001: Dead Drop Resolver
- T1105: Ingress Tool Transfer
- T1124: System Time Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1195.001: Compromise Software Dependencies and Development Tools
- T1213.003: Code Repositories
- T1213.006: Databases
- T1217: Browser Information Discovery
- T1480: Execution Guardrails
- T1518: Software Discovery
- T1539: Steal Web Session Cookie
- T1543.001: Launch Agent
- T1547.001: Registry Run Keys / Startup Folder
- T1554: Compromise Host Software Binary
- T1555.001: Keychain
- T1555.003: Credentials from Web Browsers
- T1560.001: Archive via Utility
- T1564.003: Hidden Window
- T1565.002: Transmitted Data Manipulation
- T1571: Non-Standard Port
- T1602.002: Network Device Configuration Dump
- T1614: System Location Discovery
- T1614.001: System Language Discovery
- T1657: Financial Theft
- T1678: Delay Execution
