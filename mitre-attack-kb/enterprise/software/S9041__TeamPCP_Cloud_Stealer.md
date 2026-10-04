# S9041: TeamPCP Cloud Stealer

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9041  
**Aliases:** TeamPCP Cloud Stealer, SANDCLOCK  
**Platforms:** Containers, Linux, macOS, SaaS, Windows  

## Description
The [TeamPCP Cloud Stealer](https://attack.mitre.org/software/S9041) is a comprehensive filesystem credential stealer that can harvest, encrypt, and exfiltrate credentials from over 50 sensitive file paths across CI/CD, cloud, developer tooling, and container environments. The [TeamPCP Cloud Stealer](https://attack.mitre.org/software/S9041) was the primary payload used by [TeamPCP](https://attack.mitre.org/groups/G1056) in March 2026 during early stages of a cascading supply chain campaign targeting CI/CD workflows.(Citation: Wiz Trivy Compromise MAR 2026)(Citation: Aqua Security Trivy Compromise MAR 2026)(Citation: Aqua Security Blog Trivy Compromise APR 2026)(Citation: Sysdig TeamPCP MAR 2026)(Citation: Wiz TeamPCP KICS MAR 2026)(Citation: Palo Alto TeamPCP MAR 2026)(Citation: Google AI Threat Tracker MAY 2026)(Citation: FBI TeamPCP JUL 2026)

## Techniques Used
- T1003.007: Proc Filesystem
- T1008: Fallback Channels
- T1016: System Network Configuration Discovery
- T1020: Automated Exfiltration
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1049: System Network Connections Discovery
- T1057: Process Discovery
- T1059.004: Unix Shell
- T1059.006: Python
- T1059.007: JavaScript
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1074.001: Local Data Staging
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1119: Automated Collection
- T1140: Deobfuscate/Decode Files or Information
- T1213.003: Code Repositories
- T1213.006: Databases
- T1480: Execution Guardrails
- T1518: Software Discovery
- T1526: Cloud Service Discovery
- T1528: Steal Application Access Token
- T1543.002: Systemd Service
- T1546.016: Installer Packages
- T1546.018: Python Startup Hooks
- T1548.003: Sudo and Sudo Caching
- T1552.001: Credentials In Files
- T1552.003: Shell History
- T1552.004: Private Keys
- T1552.007: Container API
- T1555: Credentials from Password Stores
- T1555.006: Cloud Secrets Management Stores
- T1560.001: Archive via Utility
- T1564.001: Hidden Files and Directories
- T1567.001: Exfiltration to Code Repository
- T1573.001: Symmetric Cryptography
- T1573.002: Asymmetric Cryptography
- T1580: Cloud Infrastructure Discovery
- T1609: Container Administration Command
- T1613: Container and Resource Discovery
- T1657: Financial Theft
- T1678: Delay Execution
