# S9008: Shai-Hulud

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9008  
**Aliases:** Shai-Hulud  
**Platforms:** Linux, SaaS, Windows  

## Description
[Shai-Hulud](https://attack.mitre.org/software/S9008) is a supply chain worm, first reported in September 2025, that spreads through code repositories, including GitHub and NPM packages. It exploits CI/CD pipeline dependencies to propagate to victims and poisons the supply chain by publishing malicious packages. Once inside a victim environment, [Shai-Hulud](https://attack.mitre.org/software/S9008) steals credentials and access tokens from compromised repository accounts and exfiltrates them to attacker-controlled servers via encoded GitHub Actions workflows.(Citation: Palo Alto Unit 42 Shai-Hulud November 2025)(Citation: Microsoft Shai-Hulud December 2025)(Citation: Socket Shai-Hulud November 2025)(Citation: Socket Shai-Hulud Trufflehog September 2025)(Citation: Aikido Shai-Hulud September 2025)(Citation: Netskope Shai-Hulud November 2025)(Citation: Wiz Shai-Hulud September 2025)

## Techniques Used
- T1027: Obfuscated Files or Information
- T1036.005: Match Legitimate Resource Name or Location
- T1036.009: Break Process Trees
- T1041: Exfiltration Over C2 Channel
- T1059.001: PowerShell
- T1059.004: Unix Shell
- T1059.007: JavaScript
- T1071.001: Web Protocols
- T1078.004: Cloud Accounts
- T1082: System Information Discovery
- T1098: Account Manipulation
- T1105: Ingress Tool Transfer
- T1119: Automated Collection
- T1195.001: Compromise Software Dependencies and Development Tools
- T1213.003: Code Repositories
- T1485: Data Destruction
- T1528: Steal Application Access Token
- T1543.002: Systemd Service
- T1546.016: Installer Packages
- T1548.003: Sudo and Sudo Caching
- T1550.001: Application Access Token
- T1552.001: Credentials In Files
- T1552.005: Cloud Instance Metadata API
- T1553: Subvert Trust Controls
- T1555.006: Cloud Secrets Management Stores
- T1564.011: Ignore Process Interrupts
- T1567.001: Exfiltration to Code Repository
- T1567.004: Exfiltration Over Webhook
- T1593.003: Code Repositories
- T1608.001: Upload Malware
- T1677: Poisoned Pipeline Execution
- T1678: Delay Execution
- T1685: Disable or Modify Tools
