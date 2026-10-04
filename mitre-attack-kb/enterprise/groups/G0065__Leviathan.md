# G0065: Leviathan

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0065  
**Aliases:** Leviathan, MUDCARP, Kryptonite Panda, Gadolinium, BRONZE MOHAWK, TEMP.Jumper, APT40, TEMP.Periscope, Gingham Typhoon  

## Description
[Leviathan](https://attack.mitre.org/groups/G0065) is a Chinese state-sponsored cyber espionage group that has been attributed to the Ministry of State Security's (MSS) Hainan State Security Department and an affiliated front company.(Citation: CISA AA21-200A APT40 July 2021) Active since at least 2009, [Leviathan](https://attack.mitre.org/groups/G0065) has targeted the following sectors: academia, aerospace/aviation, biomedical, defense industrial base, government, healthcare, manufacturing, maritime, and transportation across the US, Canada, Australia, Europe, the Middle East, and Southeast Asia.(Citation: CISA AA21-200A APT40 July 2021)(Citation: Proofpoint Leviathan Oct 2017)(Citation: FireEye Periscope March 2018)(Citation: CISA Leviathan 2024)

## Techniques Used
- T1003: OS Credential Dumping
- T1003.001: LSASS Memory
- T1021.001: Remote Desktop Protocol
- T1021.004: SSH
- T1027.001: Binary Padding
- T1027.003: Steganography
- T1027.013: Encrypted/Encoded File
- T1027.015: Compression
- T1041: Exfiltration Over C2 Channel
- T1047: Windows Management Instrumentation
- T1055.001: Dynamic-link Library Injection
- T1059.001: PowerShell
- T1059.005: Visual Basic
- T1074.001: Local Data Staging
- T1074.002: Remote Data Staging
- T1078: Valid Accounts
- T1090.003: Multi-hop Proxy
- T1102.003: One-Way Communication
- T1105: Ingress Tool Transfer
- T1133: External Remote Services
- T1140: Deobfuscate/Decode Files or Information
- T1189: Drive-by Compromise
- T1190: Exploit Public-Facing Application
- T1197: BITS Jobs
- T1203: Exploitation for Client Execution
- T1204.001: Malicious Link
- T1204.002: Malicious File
- T1218.010: Regsvr32
- T1505.003: Web Shell
- T1534: Internal Spearphishing
- T1546.003: Windows Management Instrumentation Event Subscription
- T1547.001: Registry Run Keys / Startup Folder
- T1547.009: Shortcut Modification
- T1553.002: Code Signing
- T1559.002: Dynamic Data Exchange
- T1560: Archive Collected Data
- T1566.001: Spearphishing Attachment
- T1566.002: Spearphishing Link
- T1567.002: Exfiltration to Cloud Storage
- T1572: Protocol Tunneling
- T1583.001: Domains
- T1584.004: Server
- T1584.008: Network Devices
- T1585.001: Social Media Accounts
- T1585.002: Email Accounts
- T1586.001: Social Media Accounts
- T1586.002: Email Accounts
- T1587.004: Exploits
- T1589.001: Credentials
- T1595.002: Vulnerability Scanning
