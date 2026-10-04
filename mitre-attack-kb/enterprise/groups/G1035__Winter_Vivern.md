# G1035: Winter Vivern

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G1035  
**Aliases:** Winter Vivern, TA473, UAC-0114  

## Description
Winter Vivern is a group linked to Russian and Belorussian interests active since at least 2020 targeting various European government and NGO entities, along with sporadic targeting of Indian and US victims. The group leverages a combination of document-based phishing activity and server-side exploitation for initial access, leveraging adversary-controlled and -created infrastructure for follow-on command and control.(Citation: DomainTools WinterVivern 2021)(Citation: SentinelOne WinterVivern 2023)(Citation: CERT-UA WinterVivern 2023)(Citation: ESET WinterVivern 2023)(Citation: Proofpoint WinterVivern 2023)

## Techniques Used
- T1020: Automated Exfiltration
- T1033: System Owner/User Discovery
- T1036: Masquerading
- T1036.004: Masquerade Task or Service
- T1041: Exfiltration Over C2 Channel
- T1053.005: Scheduled Task
- T1056.003: Web Portal Capture
- T1059: Command and Scripting Interpreter
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.007: JavaScript
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1113: Screen Capture
- T1114.001: Local Email Collection
- T1119: Automated Collection
- T1140: Deobfuscate/Decode Files or Information
- T1189: Drive-by Compromise
- T1190: Exploit Public-Facing Application
- T1204.001: Malicious Link
- T1566.001: Spearphishing Attachment
- T1583.001: Domains
- T1583.003: Virtual Private Server
- T1584.006: Web Services
- T1595.002: Vulnerability Scanning
