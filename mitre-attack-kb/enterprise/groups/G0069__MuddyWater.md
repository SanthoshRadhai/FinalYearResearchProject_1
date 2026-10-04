# G0069: MuddyWater

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0069  
**Aliases:** MuddyWater, Earth Vetala, MERCURY, Static Kitten, Seedworm, TEMP.Zagros, Mango Sandstorm, TA450, MuddyKrill  

## Description
[MuddyWater](https://attack.mitre.org/groups/G0069) is a cyber espionage group assessed to be a subordinate element within Iran's Ministry of Intelligence and Security (MOIS).(Citation: CYBERCOM Iranian Intel Cyber January 2022) Since at least 2017, [MuddyWater](https://attack.mitre.org/groups/G0069) has targeted a range of government and private organizations across sectors, including telecommunications, local government, finance, defense, and oil and natural gas organizations, in the Middle East (specifically the UAE and Saudi Arabia), Asia, Africa, Europe, and North America. [MuddyWater](https://attack.mitre.org/groups/G0069) has reused domains dating back to October 2025, and has a preference for NameCheap and Hosterdaddy Private Limited (AS136557). In late 2025 and early 2026, [MuddyWater](https://attack.mitre.org/groups/G0069) used commercial satellite internet (i.e., Starlink) for command and control (C2) communication. (Citation: FalconFeeds_Iran_Mar2026)(Citation: Huntio_IranInfra_Mar2026)(Citation: Unit 42 MuddyWater Nov 2017)(Citation: Symantec MuddyWater Dec 2018)(Citation: ClearSky MuddyWater Nov 2018)(Citation: ClearSky MuddyWater June 2019)(Citation: Reaqta MuddyWater November 2017)(Citation: DHS CISA AA22-055A MuddyWater February 2022)(Citation: Talos MuddyWater Jan 2022)(Citation: NaumaanProofpoint_GlobalClickFix_April2025)(Citation: ESET_MuddyWater_Dec2025)(Citation: SymantecCarbonBlack_Seedworm_Mar2026)

## Techniques Used
- T1003.001: LSASS Memory
- T1003.004: LSA Secrets
- T1003.005: Cached Domain Credentials
- T1016: System Network Configuration Discovery
- T1027.003: Steganography
- T1027.004: Compile After Delivery
- T1027.010: Command Obfuscation
- T1033: System Owner/User Discovery
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1047: Windows Management Instrumentation
- T1049: System Network Connections Discovery
- T1053.005: Scheduled Task
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1059.006: Python
- T1059.007: JavaScript
- T1071.001: Web Protocols
- T1074.001: Local Data Staging
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087.002: Domain Account
- T1090: Proxy
- T1090.002: External Proxy
- T1102.002: Bidirectional Communication
- T1104: Multi-Stage Channels
- T1105: Ingress Tool Transfer
- T1113: Screen Capture
- T1132.001: Standard Encoding
- T1137.001: Office Template Macros
- T1140: Deobfuscate/Decode Files or Information
- T1190: Exploit Public-Facing Application
- T1203: Exploitation for Client Execution
- T1204.001: Malicious Link
- T1204.002: Malicious File
- T1204.004: Malicious Copy and Paste
- T1210: Exploitation of Remote Services
- T1218.003: CMSTP
- T1218.005: Mshta
- T1218.011: Rundll32
- T1219.002: Remote Desktop Software
- T1518: Software Discovery
- T1518.001: Security Software Discovery
- T1534: Internal Spearphishing
- T1547.001: Registry Run Keys / Startup Folder
- T1548.002: Bypass User Account Control
- T1552.001: Credentials In Files
- T1555: Credentials from Password Stores
- T1555.003: Credentials from Web Browsers
- T1559.001: Component Object Model
- T1559.002: Dynamic Data Exchange
- T1560.001: Archive via Utility
- T1566: Phishing
- T1566.001: Spearphishing Attachment
- T1566.002: Spearphishing Link
- T1567.002: Exfiltration to Cloud Storage
- T1571: Non-Standard Port
- T1573.001: Symmetric Cryptography
- T1574.001: DLL
- T1583.001: Domains
- T1583.006: Web Services
- T1588.001: Malware
- T1588.002: Tool
- T1590.004: Network Topology
- T1684.001: Impersonation
- T1685: Disable or Modify Tools
