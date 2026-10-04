# G1015: Scattered Spider

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G1015  
**Aliases:** Scattered Spider, Roasted 0ktapus, Octo Tempest, Storm-0875, UNC3944  

## Description
[Scattered Spider](https://attack.mitre.org/groups/G1015) is a native English-speaking cybercriminal group active since at least 2022. (Citation: CrowdStrike Scattered Spider Profile) (Citation: MSTIC Octo Tempest Operations October 2023) The group initially targeted customer relationship management (CRM) providers, business process outsourcing (BPO) firms, and telecommunications and technology companies before expanding in 2023 to gaming, hospitality, retail, managed service provider (MSP), manufacturing, and financial sectors. (Citation: MSTIC Octo Tempest Operations October 2023)
[Scattered Spider](https://attack.mitre.org/groups/G1015) relies heavily on social engineering, including impersonating IT and help-desk staff, to gain initial access, bypass multi-factor authentication (MFA), and compromise enterprise networks. The group has adapted its tooling to evade endpoint detection and response (EDR) defenses and used ransomware for financial gain. (Citation: CISA Scattered Spider Advisory November 2023) (Citation: CrowdStrike Scattered Spider BYOVD January 2023) (Citation: Crowdstrike TELCO BPO Campaign December 2022)
[Scattered Spider](https://attack.mitre.org/groups/G1015) had expanded into hybrid cloud and identity environments, using help-desk impersonation and MFA bypass to obtain administrator access in Okta, AWS, and Office 365. (Citation: Mandiant UNC3944 May 2025)

## Techniques Used
- T1003.003: NTDS
- T1006: Direct Volume Access
- T1016: System Network Configuration Discovery
- T1018: Remote System Discovery
- T1021.001: Remote Desktop Protocol
- T1021.004: SSH
- T1021.007: Cloud Services
- T1041: Exfiltration Over C2 Channel
- T1059.001: PowerShell
- T1059.004: Unix Shell
- T1068: Exploitation for Privilege Escalation
- T1069: Permission Groups Discovery
- T1069.002: Domain Groups
- T1070.008: Clear Mailbox Data
- T1074: Data Staged
- T1078: Valid Accounts
- T1078.004: Cloud Accounts
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087: Account Discovery
- T1087.002: Domain Account
- T1090: Proxy
- T1098: Account Manipulation
- T1098.003: Additional Cloud Roles
- T1105: Ingress Tool Transfer
- T1114: Email Collection
- T1114.003: Email Forwarding Rule
- T1133: External Remote Services
- T1136: Create Account
- T1204: User Execution
- T1213.003: Code Repositories
- T1213.005: Messaging Applications
- T1217: Browser Information Discovery
- T1219.002: Remote Desktop Software
- T1484.002: Trust Modification
- T1486: Data Encrypted for Impact
- T1490: Inhibit System Recovery
- T1530: Data from Cloud Storage
- T1538: Cloud Service Dashboard
- T1539: Steal Web Session Cookie
- T1543.002: Systemd Service
- T1552.001: Credentials In Files
- T1552.004: Private Keys
- T1553.002: Code Signing
- T1555.005: Password Managers
- T1556.006: Multi-Factor Authentication
- T1556.009: Conditional Access Policies
- T1564.008: Email Hiding Rules
- T1567.002: Exfiltration to Cloud Storage
- T1572: Protocol Tunneling
- T1578.002: Create Cloud Instance
- T1580: Cloud Infrastructure Discovery
- T1583.001: Domains
- T1585.001: Social Media Accounts
- T1588.001: Malware
- T1588.002: Tool
- T1589: Gather Victim Identity Information
- T1598: Phishing for Information
- T1598.003: Spearphishing Link
- T1598.004: Spearphishing Voice
- T1621: Multi-Factor Authentication Request Generation
- T1657: Financial Theft
- T1684.001: Impersonation
- T1685: Disable or Modify Tools
