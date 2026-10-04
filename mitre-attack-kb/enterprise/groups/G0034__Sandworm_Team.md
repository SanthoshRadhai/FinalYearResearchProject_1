# G0034: Sandworm Team

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0034  
**Aliases:** Sandworm Team, ELECTRUM, Telebots, IRON VIKING, BlackEnergy (Group), Quedagh, Voodoo Bear, IRIDIUM, Seashell Blizzard, FROZENBARENTS, APT44  

## Description
[Sandworm Team](https://attack.mitre.org/groups/G0034) is a destructive threat group that has been attributed to Russia's General Staff Main Intelligence Directorate (GRU) Main Center for Special Technologies (GTsST) military unit 74455.(Citation: US District Court Indictment GRU Unit 74455 October 2020)(Citation: UK NCSC Olympic Attacks October 2020) This group has been active since at least 2009.(Citation: iSIGHT Sandworm 2014)(Citation: CrowdStrike VOODOO BEAR)(Citation: USDOJ Sandworm Feb 2020)(Citation: NCSC Sandworm Feb 2020)

In October 2020, the US indicted six GRU Unit 74455 officers associated with [Sandworm Team](https://attack.mitre.org/groups/G0034) for the following cyber operations: the 2015 and 2016 attacks against Ukrainian electrical companies and government organizations, the 2017 worldwide [NotPetya](https://attack.mitre.org/software/S0368) attack, targeting of the 2017 French presidential campaign, the 2018 [Olympic Destroyer](https://attack.mitre.org/software/S0365) attack against the Winter Olympic Games, the 2018 operation against the Organisation for the Prohibition of Chemical Weapons, and attacks against the country of Georgia in 2018 and 2019.(Citation: US District Court Indictment GRU Unit 74455 October 2020)(Citation: UK NCSC Olympic Attacks October 2020) Some of these were conducted with the assistance of GRU Unit 26165, which is also referred to as [APT28](https://attack.mitre.org/groups/G0007).(Citation: US District Court Indictment GRU Oct 2018)

## Techniques Used
- T1003.001: LSASS Memory
- T1003.003: NTDS
- T1005: Data from Local System
- T1018: Remote System Discovery
- T1021.002: SMB/Windows Admin Shares
- T1027: Obfuscated Files or Information
- T1027.010: Command Obfuscation
- T1033: System Owner/User Discovery
- T1036: Masquerading
- T1036.005: Match Legitimate Resource Name or Location
- T1040: Network Sniffing
- T1041: Exfiltration Over C2 Channel
- T1047: Windows Management Instrumentation
- T1049: System Network Connections Discovery
- T1053.005: Scheduled Task
- T1056.001: Keylogging
- T1059.001: PowerShell
- T1059.005: Visual Basic
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1072: Software Deployment Tools
- T1078: Valid Accounts
- T1078.002: Domain Accounts
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087.002: Domain Account
- T1087.003: Email Account
- T1090: Proxy
- T1102.002: Bidirectional Communication
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1132.001: Standard Encoding
- T1133: External Remote Services
- T1140: Deobfuscate/Decode Files or Information
- T1190: Exploit Public-Facing Application
- T1195: Supply Chain Compromise
- T1195.002: Compromise Software Supply Chain
- T1199: Trusted Relationship
- T1203: Exploitation for Client Execution
- T1204.001: Malicious Link
- T1204.002: Malicious File
- T1213.006: Databases
- T1218.011: Rundll32
- T1219: Remote Access Tools
- T1485: Data Destruction
- T1486: Data Encrypted for Impact
- T1489: Service Stop
- T1490: Inhibit System Recovery
- T1491.002: External Defacement
- T1499: Endpoint Denial of Service
- T1505.003: Web Shell
- T1539: Steal Web Session Cookie
- T1555.003: Credentials from Web Browsers
- T1561.002: Disk Structure Wipe
- T1566.001: Spearphishing Attachment
- T1566.002: Spearphishing Link
- T1570: Lateral Tool Transfer
- T1571: Non-Standard Port
- T1583: Acquire Infrastructure
- T1583.001: Domains
- T1583.004: Server
- T1584.004: Server
- T1584.005: Botnet
- T1585.001: Social Media Accounts
- T1585.002: Email Accounts
- T1586.001: Social Media Accounts
- T1587.001: Malware
- T1588.002: Tool
- T1588.006: Vulnerabilities
- T1589.002: Email Addresses
- T1589.003: Employee Names
- T1590.001: Domain Properties
- T1591.002: Business Relationships
- T1592.002: Software
- T1593: Search Open Websites/Domains
- T1594: Search Victim-Owned Websites
- T1595.002: Vulnerability Scanning
- T1598.003: Spearphishing Link
- T1608.001: Upload Malware
