# G0032: Lazarus Group

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0032  
**Aliases:** Lazarus Group, Labyrinth Chollima, HIDDEN COBRA, Guardians of Peace, ZINC, NICKEL ACADEMY, Diamond Sleet  

## Description
[Lazarus Group](https://attack.mitre.org/groups/G0032) is a North Korean state-sponsored cyber threat group attributed to the Reconnaissance General Bureau (RGB). (Citation: US-CERT HIDDEN COBRA June 2017) (Citation: Treasury North Korean Cyber Groups September 2019) [Lazarus Group](https://attack.mitre.org/groups/G0032) has been active since at least 2009 and is reportedly responsible for the November 2014 destructive wiper attack on Sony Pictures Entertainment, identified by Novetta as part of Operation Blockbuster. Malware used by [Lazarus Group](https://attack.mitre.org/groups/G0032) correlates to other reported campaigns, including Operation Flame, Operation 1Mission, Operation Troy, DarkSeoul, and Ten Days of Rain.(Citation: Novetta Blockbuster)

North Korea’s cyber operations have shown a consistent pattern of adaptation, forming and reorganizing units as national priorities shift. These units frequently share personnel, infrastructure, malware, and tradecraft, making it difficult to attribute specific operations with high confidence. Public reporting often uses “Lazarus Group” as an umbrella term for multiple North Korean cyber operators conducting espionage, destructive attacks, and financially motivated campaigns.(Citation: Mandiant DPRK Laz Org Breakdown 2022)(Citation: Mandiant DPRK Groups 2023)(Citation: JPCert Blog Laz Subgroups 2025)

## Techniques Used
- T1001.003: Protocol or Service Impersonation
- T1005: Data from Local System
- T1008: Fallback Channels
- T1010: Application Window Discovery
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1021.001: Remote Desktop Protocol
- T1021.002: SMB/Windows Admin Shares
- T1021.004: SSH
- T1027.007: Dynamic API Resolution
- T1027.009: Embedded Payloads
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1036.003: Rename Legitimate Utilities
- T1036.004: Masquerade Task or Service
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1046: Network Service Discovery
- T1047: Windows Management Instrumentation
- T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol
- T1049: System Network Connections Discovery
- T1053.005: Scheduled Task
- T1055.001: Dynamic-link Library Injection
- T1056.001: Keylogging
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1070: Indicator Removal
- T1070.003: Clear Command History
- T1070.004: File Deletion
- T1070.006: Timestomp
- T1071.001: Web Protocols
- T1074.001: Local Data Staging
- T1078: Valid Accounts
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1090.001: Internal Proxy
- T1090.002: External Proxy
- T1098: Account Manipulation
- T1102.002: Bidirectional Communication
- T1104: Multi-Stage Channels
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1110.003: Password Spraying
- T1124: System Time Discovery
- T1132.001: Standard Encoding
- T1134.002: Create Process with Token
- T1140: Deobfuscate/Decode Files or Information
- T1189: Drive-by Compromise
- T1202: Indirect Command Execution
- T1203: Exploitation for Client Execution
- T1204.002: Malicious File
- T1218: System Binary Proxy Execution
- T1218.005: Mshta
- T1218.011: Rundll32
- T1485: Data Destruction
- T1489: Service Stop
- T1491.001: Internal Defacement
- T1529: System Shutdown/Reboot
- T1542.003: Bootkit
- T1543.003: Windows Service
- T1547.001: Registry Run Keys / Startup Folder
- T1547.009: Shortcut Modification
- T1553.002: Code Signing
- T1557.001: Name Resolution Poisoning and SMB Relay
- T1560: Archive Collected Data
- T1560.002: Archive via Library
- T1560.003: Archive via Custom Method
- T1561.001: Disk Content Wipe
- T1561.002: Disk Structure Wipe
- T1564.001: Hidden Files and Directories
- T1566.001: Spearphishing Attachment
- T1566.002: Spearphishing Link
- T1566.003: Spearphishing via Service
- T1571: Non-Standard Port
- T1573.001: Symmetric Cryptography
- T1574.001: DLL
- T1574.013: KernelCallbackTable
- T1583.001: Domains
- T1583.006: Web Services
- T1584.004: Server
- T1585.001: Social Media Accounts
- T1585.002: Email Accounts
- T1587.001: Malware
- T1588.002: Tool
- T1588.004: Digital Certificates
- T1589.002: Email Addresses
- T1591: Gather Victim Org Information
- T1620: Reflective Code Loading
- T1680: Local Storage Discovery
- T1685: Disable or Modify Tools
- T1686.003: Windows Host Firewall
