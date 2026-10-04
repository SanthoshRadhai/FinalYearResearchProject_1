# G0129: Mustang Panda

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0129  
**Aliases:** Mustang Panda, TA416, RedDelta, BRONZE PRESIDENT, STATELY TAURUS, FIREANT, CAMARO DRAGON, EARTH PRETA, HIVE0154, TWILL TYPHOON, TANTALUM, LUMINOUS MOTH, UNC6384, TEMP.Hex, Red Lich, ClumsyToad  

## Description
[Mustang Panda](https://attack.mitre.org/groups/G0129) is a China-based cyber espionage threat actor that has been conducting operations since at least 2012. [Mustang Panda](https://attack.mitre.org/groups/G0129) has been known to use tailored phishing lures and decoy documents to deliver malicious payloads.  [Mustang Panda](https://attack.mitre.org/groups/G0129) has targeted government, diplomatic, and non-governmental organizations, including think tanks, religious institutions, and research entities, across the United States, Europe, and Asia, with notable activity in Russia, Mongolia, Myanmar, Pakistan, and Vietnam. (Citation: BlackBerry MUSTANG PANDA October 2022)(Citation: Eset PlugX Korplug Mustang Panda March 2022)(Citation: Anomali MUSTANG PANDA October 2019)(Citation: Cisco Talos MUSTANG PANDA PLUGX PUBLOAD MAY 2022)(Citation: Secureworks BRONZE PRESIDENT December 2019)(Citation: DOJ Affidavit Search and Seizure PlugX December 2024)(Citation: EclecticIQ Mustang Panda PlugX)(Citation: ATTACKIQ MUSTANG PANDA TONESHELL March 2023)(Citation: Crowdstrike MUSTANG PANDA June 2018)(Citation: Palo Alto Networks, Unit 42)(Citation: Sophos PlugX September 2022)(Citation: Sophos Mustang Panda PLUGX)(Citation: Zscaler)

## Techniques Used
- T1001.003: Protocol or Service Impersonation
- T1003: OS Credential Dumping
- T1003.001: LSASS Memory
- T1003.003: NTDS
- T1003.006: DCSync
- T1016: System Network Configuration Discovery
- T1018: Remote System Discovery
- T1027: Obfuscated Files or Information
- T1027.007: Dynamic API Resolution
- T1027.012: LNK Icon Smuggling
- T1027.016: Junk Code Insertion
- T1036.005: Match Legitimate Resource Name or Location
- T1036.007: Double File Extension
- T1036.008: Masquerade File Type
- T1041: Exfiltration Over C2 Channel
- T1046: Network Service Discovery
- T1047: Windows Management Instrumentation
- T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol
- T1049: System Network Connections Discovery
- T1052.001: Exfiltration over USB
- T1053.005: Scheduled Task
- T1057: Process Discovery
- T1059: Command and Scripting Interpreter
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1059.007: JavaScript
- T1069.002: Domain Groups
- T1070: Indicator Removal
- T1070.004: File Deletion
- T1070.006: Timestomp
- T1071.001: Web Protocols
- T1072: Software Deployment Tools
- T1074.001: Local Data Staging
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087.002: Domain Account
- T1091: Replication Through Removable Media
- T1095: Non-Application Layer Protocol
- T1102: Web Service
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1119: Automated Collection
- T1129: Shared Modules
- T1140: Deobfuscate/Decode Files or Information
- T1176.002: IDE Extensions
- T1203: Exploitation for Client Execution
- T1204.001: Malicious Link
- T1204.002: Malicious File
- T1205: Traffic Signaling
- T1218.004: InstallUtil
- T1218.005: Mshta
- T1219.001: IDE Tunneling
- T1219.002: Remote Desktop Software
- T1505.003: Web Shell
- T1518: Software Discovery
- T1546.003: Windows Management Instrumentation Event Subscription
- T1547.001: Registry Run Keys / Startup Folder
- T1553.002: Code Signing
- T1557: Adversary-in-the-Middle
- T1560.001: Archive via Utility
- T1560.003: Archive via Custom Method
- T1564.001: Hidden Files and Directories
- T1566.001: Spearphishing Attachment
- T1566.002: Spearphishing Link
- T1567.002: Exfiltration to Cloud Storage
- T1572: Protocol Tunneling
- T1573.001: Symmetric Cryptography
- T1574.001: DLL
- T1574.005: Executable Installer File Permissions Weakness
- T1583.001: Domains
- T1583.006: Web Services
- T1585.002: Email Accounts
- T1586.002: Email Accounts
- T1587.001: Malware
- T1588.002: Tool
- T1588.003: Code Signing Certificates
- T1588.004: Digital Certificates
- T1593: Search Open Websites/Domains
- T1598.003: Spearphishing Link
- T1608: Stage Capabilities
- T1608.001: Upload Malware
- T1622: Debugger Evasion
- T1654: Log Enumeration
- T1678: Delay Execution
