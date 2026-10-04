# S1245: InvisibleFerret

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1245  
**Aliases:** InvisibleFerret  
**Platforms:** Linux, macOS, Windows  

## Description
[InvisibleFerret](https://attack.mitre.org/software/S1245) is a modular python malware that is leveraged for data exfiltration and remote access capabilities.(Citation: ESET Contagious Interview BeaverTail InvisibleFerret February 2025)(Citation: Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024)(Citation: PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023)   [InvisibleFerret](https://attack.mitre.org/software/S1245) consists of four modules: main, payload, browser, and AnyDesk.(Citation: ESET Contagious Interview BeaverTail InvisibleFerret February 2025)  [InvisibleFerret](https://attack.mitre.org/software/S1245) malware has been leveraged by North Korea-affiliated threat actors identified as DeceptiveDevelopment or [Contagious Interview](https://attack.mitre.org/groups/G1052) since 2023.(Citation: Recorded Future Contagious Inteview BeaverTail InvisibleFerret OtterCookie February 2025)(Citation: Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024)(Citation: PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023)(Citation: PaloAlto Unit42 ContagiousInterview BeaverTail InvisibileFerret October 2024)  [InvisibleFerret](https://attack.mitre.org/software/S1245) has historically been introduced to the victim environment through the use of the [BeaverTail](https://attack.mitre.org/software/S1246) malware.(Citation: Esentire ContagiousInterview BeaverTail InvisibleFerret November 2024)(Citation: ESET Contagious Interview BeaverTail InvisibleFerret February 2025)(Citation: Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024)(Citation: PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023)(Citation: PaloAlto Unit42 ContagiousInterview BeaverTail InvisibileFerret October 2024)

## Techniques Used
- T1005: Data from Local System
- T1016: System Network Configuration Discovery
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1041: Exfiltration Over C2 Channel
- T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol
- T1056: Input Capture
- T1056.001: Keylogging
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.006: Python
- T1071.001: Web Protocols
- T1074.001: Local Data Staging
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087.001: Local Account
- T1095: Non-Application Layer Protocol
- T1105: Ingress Tool Transfer
- T1115: Clipboard Data
- T1140: Deobfuscate/Decode Files or Information
- T1219: Remote Access Tools
- T1489: Service Stop
- T1518: Software Discovery
- T1543.001: Launch Agent
- T1547.001: Registry Run Keys / Startup Folder
- T1547.013: XDG Autostart Entries
- T1555.003: Credentials from Web Browsers
- T1555.005: Password Managers
- T1560.001: Archive via Utility
- T1564.003: Hidden Window
- T1567: Exfiltration Over Web Service
- T1571: Non-Standard Port
- T1614: System Location Discovery
- T1657: Financial Theft
- T1679: Selective Exclusion
