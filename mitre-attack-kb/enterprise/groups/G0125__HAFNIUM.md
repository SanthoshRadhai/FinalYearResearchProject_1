# G0125: HAFNIUM

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0125  
**Aliases:** HAFNIUM, Operation Exchange Marauder, Silk Typhoon  

## Description
[HAFNIUM](https://attack.mitre.org/groups/G0125) is a likely state-sponsored cyber espionage group operating out of China that has been active since at least January 2021. [HAFNIUM](https://attack.mitre.org/groups/G0125) primarily targets entities in the US across a number of industry sectors, including infectious disease researchers, law firms, higher education institutions, defense contractors, policy think tanks, and NGOs. [HAFNIUM](https://attack.mitre.org/groups/G0125) has targeted remote management tools and cloud software for intial access and has demonstrated an ability to quickly operationalize exploits for identified vulnerabilities in edge devices.(Citation: Microsoft HAFNIUM March 2020)(Citation: Volexity Exchange Marauder March 2021)(Citation: Microsoft Silk Typhoon MAR 2025)

## Techniques Used
- T1003.001: LSASS Memory
- T1003.003: NTDS
- T1005: Data from Local System
- T1016: System Network Configuration Discovery
- T1016.001: Internet Connection Discovery
- T1018: Remote System Discovery
- T1033: System Owner/User Discovery
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1068: Exploitation for Privilege Escalation
- T1071.001: Web Protocols
- T1078.003: Local Accounts
- T1078.004: Cloud Accounts
- T1083: File and Directory Discovery
- T1095: Non-Application Layer Protocol
- T1098: Account Manipulation
- T1105: Ingress Tool Transfer
- T1110.003: Password Spraying
- T1114.002: Remote Email Collection
- T1119: Automated Collection
- T1132.001: Standard Encoding
- T1136.002: Domain Account
- T1190: Exploit Public-Facing Application
- T1199: Trusted Relationship
- T1213.002: Sharepoint
- T1218.011: Rundll32
- T1505.003: Web Shell
- T1530: Data from Cloud Storage
- T1550.001: Application Access Token
- T1555.006: Cloud Secrets Management Stores
- T1560.001: Archive via Utility
- T1564.001: Hidden Files and Directories
- T1567.002: Exfiltration to Cloud Storage
- T1583.003: Virtual Private Server
- T1583.005: Botnet
- T1583.006: Web Services
- T1584.005: Botnet
- T1589.002: Email Addresses
- T1590: Gather Victim Network Information
- T1590.005: IP Addresses
- T1592.004: Client Configurations
- T1593.003: Code Repositories
- T1685.005: Clear Windows Event Logs
