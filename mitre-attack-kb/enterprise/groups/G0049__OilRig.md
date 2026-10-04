# G0049: OilRig

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0049  
**Aliases:** OilRig, COBALT GYPSY, IRN2, APT34, Helix Kitten, Evasive Serpens, Hazel Sandstorm, EUROPIUM, ITG13, Earth Simnavaz, Crambus, TA452  

## Description
[OilRig](https://attack.mitre.org/groups/G0049) is a suspected Iranian threat group that has targeted Middle Eastern and international victims since at least 2014. The group has targeted a variety of sectors, including financial, government, energy, chemical, and telecommunications. It appears the group carries out supply chain attacks, leveraging the trust relationship between organizations to attack their primary targets. The group works on behalf of the Iranian government based on infrastructure details that contain references to Iran, use of Iranian infrastructure, and targeting that aligns with nation-state interests.(Citation: FireEye APT34 Dec 2017)(Citation: Palo Alto OilRig April 2017)(Citation: ClearSky OilRig Jan 2017)(Citation: Palo Alto OilRig May 2016)(Citation: Palo Alto OilRig Oct 2016)(Citation: Unit42 OilRig Playbook 2023)(Citation: Unit 42 QUADAGENT July 2018)

## Techniques Used
- T1003.001: LSASS Memory
- T1003.004: LSA Secrets
- T1003.005: Cached Domain Credentials
- T1005: Data from Local System
- T1007: System Service Discovery
- T1008: Fallback Channels
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1021.001: Remote Desktop Protocol
- T1021.004: SSH
- T1025: Data from Removable Media
- T1027.005: Indicator Removal from Tools
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1036: Masquerading
- T1036.005: Match Legitimate Resource Name or Location
- T1046: Network Service Discovery
- T1047: Windows Management Instrumentation
- T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol
- T1049: System Network Connections Discovery
- T1053.005: Scheduled Task
- T1056.001: Keylogging
- T1057: Process Discovery
- T1059: Command and Scripting Interpreter
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1068: Exploitation for Privilege Escalation
- T1069.001: Local Groups
- T1069.002: Domain Groups
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1071.004: DNS
- T1078: Valid Accounts
- T1078.002: Domain Accounts
- T1082: System Information Discovery
- T1087.001: Local Account
- T1087.002: Domain Account
- T1105: Ingress Tool Transfer
- T1110: Brute Force
- T1112: Modify Registry
- T1113: Screen Capture
- T1115: Clipboard Data
- T1119: Automated Collection
- T1120: Peripheral Device Discovery
- T1133: External Remote Services
- T1137.004: Outlook Home Page
- T1140: Deobfuscate/Decode Files or Information
- T1195: Supply Chain Compromise
- T1201: Password Policy Discovery
- T1203: Exploitation for Client Execution
- T1204.001: Malicious Link
- T1204.002: Malicious File
- T1218.001: Compiled HTML File
- T1219: Remote Access Tools
- T1497.001: System Checks
- T1505.003: Web Shell
- T1543.003: Windows Service
- T1552.001: Credentials In Files
- T1553.002: Code Signing
- T1555: Credentials from Password Stores
- T1555.003: Credentials from Web Browsers
- T1555.004: Windows Credential Manager
- T1556.002: Password Filter DLL
- T1566.001: Spearphishing Attachment
- T1566.002: Spearphishing Link
- T1566.003: Spearphishing via Service
- T1572: Protocol Tunneling
- T1573.002: Asymmetric Cryptography
- T1583.001: Domains
- T1586.002: Email Accounts
- T1587.001: Malware
- T1588.002: Tool
- T1588.003: Code Signing Certificates
- T1608.001: Upload Malware
- T1686.003: Windows Host Firewall
