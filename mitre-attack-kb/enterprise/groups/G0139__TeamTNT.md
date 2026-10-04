# G0139: TeamTNT

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0139  
**Aliases:** TeamTNT  

## Description
[TeamTNT](https://attack.mitre.org/groups/G0139) is a threat group that has primarily targeted cloud and containerized environments. The group as been active since at least October 2019 and has mainly focused its efforts on leveraging cloud and container resources to deploy cryptocurrency miners in victim environments.(Citation: Palo Alto Black-T October 2020)(Citation: Lacework TeamTNT May 2021)(Citation: Intezer TeamTNT September 2020)(Citation: Cado Security TeamTNT Worm August 2020)(Citation: Unit 42 Hildegard Malware)(Citation: Trend Micro TeamTNT)(Citation: ATT TeamTNT Chimaera September 2020)(Citation: Aqua TeamTNT August 2020)(Citation: Intezer TeamTNT Explosion September 2021)

## Techniques Used
- T1007: System Service Discovery
- T1014: Rootkit
- T1016: System Network Configuration Discovery
- T1021.004: SSH
- T1027.002: Software Packing
- T1027.013: Encrypted/Encoded File
- T1036: Masquerading
- T1036.005: Match Legitimate Resource Name or Location
- T1046: Network Service Discovery
- T1048: Exfiltration Over Alternative Protocol
- T1049: System Network Connections Discovery
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.004: Unix Shell
- T1059.009: Cloud API
- T1059.013: Container CLI/API
- T1070.003: Clear Command History
- T1070.004: File Deletion
- T1071: Application Layer Protocol
- T1071.001: Web Protocols
- T1074.001: Local Data Staging
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1098.004: SSH Authorized Keys
- T1102: Web Service
- T1105: Ingress Tool Transfer
- T1120: Peripheral Device Discovery
- T1133: External Remote Services
- T1136.001: Local Account
- T1140: Deobfuscate/Decode Files or Information
- T1204.003: Malicious Image
- T1219: Remote Access Tools
- T1222.002: Linux and Mac Permissions
- T1496.001: Compute Hijacking
- T1518.001: Security Software Discovery
- T1543.002: Systemd Service
- T1543.003: Windows Service
- T1547.001: Registry Run Keys / Startup Folder
- T1552.001: Credentials In Files
- T1552.004: Private Keys
- T1552.005: Cloud Instance Metadata API
- T1569.003: Systemctl
- T1583.001: Domains
- T1587.001: Malware
- T1595.001: Scanning IP Blocks
- T1595.002: Vulnerability Scanning
- T1608.001: Upload Malware
- T1609: Container Administration Command
- T1610: Deploy Container
- T1611: Escape to Host
- T1613: Container and Resource Discovery
- T1680: Local Storage Discovery
- T1685: Disable or Modify Tools
- T1685.006: Clear Linux or Mac System Logs
- T1686: Disable or Modify System Firewall
