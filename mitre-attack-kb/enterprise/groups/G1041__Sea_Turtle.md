# G1041: Sea Turtle

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G1041  
**Aliases:** Sea Turtle, Teal Kurma, Marbled Dust, Cosmic Wolf, SILICON  

## Description
[Sea Turtle](https://attack.mitre.org/groups/G1041) is a Türkiye-linked threat actor active since at least 2017 performing espionage and service provider compromise operations against victims in Asia, Europe, and North America. [Sea Turtle](https://attack.mitre.org/groups/G1041) is notable for targeting registrars managing ccTLDs and complex DNS-based intrusions where the threat actor compromised DNS providers to hijack DNS resolution for ultimate victims, enabling [Sea Turtle](https://attack.mitre.org/groups/G1041) to spoof log in portals and other applications for credential collection.(Citation: Talos Sea Turtle 2019)(Citation: Talos Sea Turtle 2019_2)(Citation: PWC Sea Turtle 2023)(Citation: Hunt Sea Turtle 2024)

## Techniques Used
- T1027.004: Compile After Delivery
- T1059.004: Unix Shell
- T1071.001: Web Protocols
- T1074.002: Remote Data Staging
- T1078: Valid Accounts
- T1078.003: Local Accounts
- T1114.001: Local Email Collection
- T1133: External Remote Services
- T1190: Exploit Public-Facing Application
- T1199: Trusted Relationship
- T1203: Exploitation for Client Execution
- T1213.006: Databases
- T1505.003: Web Shell
- T1557: Adversary-in-the-Middle
- T1560.001: Archive via Utility
- T1564.011: Ignore Process Interrupts
- T1566: Phishing
- T1583: Acquire Infrastructure
- T1583.001: Domains
- T1583.002: DNS Server
- T1583.003: Virtual Private Server
- T1584.002: DNS Server
- T1588.002: Tool
- T1588.004: Digital Certificates
- T1608.003: Install Digital Certificate
- T1685.006: Clear Linux or Mac System Logs
- T1690: Prevent Command History Logging
