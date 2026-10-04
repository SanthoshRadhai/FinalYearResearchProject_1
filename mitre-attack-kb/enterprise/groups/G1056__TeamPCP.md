# G1056: TeamPCP

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G1056  
**Aliases:** TeamPCP, PCPCat, ShellForce, DeadCatx3, SHADOW-WATER-058, UNC6780  

## Description
[TeamPCP](https://attack.mitre.org/groups/G1056) is a financially-motivated, cloud-native threat group that has been active since at least September 2025. Initially focused on ransomware and cryptocurrency theft, [TeamPCP](https://attack.mitre.org/groups/G1056) shifted in early 2026 to systematic, worm-driven credential theft and software supply chain attacks targeting Continuous Integration and Continuous Delivery (CI/CD) workflows. [TeamPCP](https://attack.mitre.org/groups/G1056) has monetized access through extortion and through partnerships with ransomware actors including Vect and CipherForce.(Citation: Wiz TeamPCP Profile MAY 2026)(Citation: Wiz Trivy Compromise MAR 2026)(Citation: Aqua Security Trivy Compromise MAR 2026)(Citation: Aqua Security Blog Trivy Compromise APR 2026)(Citation: Palo Alto TeamPCP MAR 2026)(Citation: Trend Micro TeamPCP MAY 2026)

## Techniques Used
- T1005: Data from Local System
- T1027.003: Steganography
- T1036.005: Match Legitimate Resource Name or Location
- T1059.004: Unix Shell
- T1059.006: Python
- T1059.007: JavaScript
- T1059.013: Container CLI/API
- T1078: Valid Accounts
- T1078.004: Cloud Accounts
- T1098: Account Manipulation
- T1105: Ingress Tool Transfer
- T1176.002: IDE Extensions
- T1190: Exploit Public-Facing Application
- T1195.001: Compromise Software Dependencies and Development Tools
- T1485: Data Destruction
- T1486: Data Encrypted for Impact
- T1528: Steal Application Access Token
- T1543.002: Systemd Service
- T1546.016: Installer Packages
- T1547.001: Registry Run Keys / Startup Folder
- T1550.001: Application Access Token
- T1552.004: Private Keys
- T1553.002: Code Signing
- T1555.006: Cloud Secrets Management Stores
- T1564.001: Hidden Files and Directories
- T1583: Acquire Infrastructure
- T1583.001: Domains
- T1583.004: Server
- T1583.006: Web Services
- T1585.001: Social Media Accounts
- T1587.001: Malware
- T1608.001: Upload Malware
- T1657: Financial Theft
- T1677: Poisoned Pipeline Execution
- T1683.001: Written Content
- T1684.001: Impersonation
