# G0106: Rocke

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0106  
**Aliases:** Rocke  

## Description
[Rocke](https://attack.mitre.org/groups/G0106) is an alleged Chinese-speaking adversary whose primary objective appeared to be cryptojacking, or stealing victim system resources for the purposes of mining cryptocurrency. The name [Rocke](https://attack.mitre.org/groups/G0106) comes from the email address "rocke@live.cn" used to create the wallet which held collected cryptocurrency. Researchers have detected overlaps between [Rocke](https://attack.mitre.org/groups/G0106) and the Iron Cybercrime Group, though this attribution has not been confirmed.(Citation: Talos Rocke August 2018)

## Techniques Used
- T1014: Rootkit
- T1018: Remote System Discovery
- T1021.004: SSH
- T1027: Obfuscated Files or Information
- T1027.002: Software Packing
- T1027.004: Compile After Delivery
- T1036.005: Match Legitimate Resource Name or Location
- T1037: Boot or Logon Initialization Scripts
- T1046: Network Service Discovery
- T1053.003: Cron
- T1055.002: Portable Executable Injection
- T1057: Process Discovery
- T1059.004: Unix Shell
- T1059.006: Python
- T1070.004: File Deletion
- T1070.006: Timestomp
- T1071: Application Layer Protocol
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1102: Web Service
- T1102.001: Dead Drop Resolver
- T1105: Ingress Tool Transfer
- T1140: Deobfuscate/Decode Files or Information
- T1190: Exploit Public-Facing Application
- T1222.002: Linux and Mac Permissions
- T1496.001: Compute Hijacking
- T1518.001: Security Software Discovery
- T1543.002: Systemd Service
- T1547.001: Registry Run Keys / Startup Folder
- T1552.004: Private Keys
- T1564.001: Hidden Files and Directories
- T1571: Non-Standard Port
- T1574.006: Dynamic Linker Hijacking
- T1685: Disable or Modify Tools
- T1685.006: Clear Linux or Mac System Logs
- T1686: Disable or Modify System Firewall
