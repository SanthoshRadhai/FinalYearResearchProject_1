# S9043: Mini Shai-Hulud

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9043  
**Aliases:** Mini Shai-Hulud  
**Platforms:** Containers, IaaS, Linux, macOS, SaaS, Windows  

## Description
[Mini Shai-Hulud](https://attack.mitre.org/software/S9043) is a credential stealer and self-replicating supply chain worm, derived from [Shai-Hulud](https://attack.mitre.org/software/S9008), that has been used by [TeamPCP](https://attack.mitre.org/groups/G1056) to target Continuous Integration and Continuous Delivery/Deployment (CI/CD) workflows since at least 2026. [Mini Shai-Hulud](https://attack.mitre.org/software/S9043) can compromise credentials across multiple cloud, container, and AI configuration file paths and can use stolen npm and GitHub OIDC tokens to spread to other packages maintained by the compromised user.  [Mini Shai-Hulud](https://attack.mitre.org/software/S9043) also has a targeted wiper component and has used multiple C2 and data exfiltration mechanisms.(Citation: Wiz Mini Shai-Hulud MAY 2026)(Citation: Trend Micro TeamPCP MAY 2026)(Citation: Hunt.io TeamPCP Toolkit MAY 2026)(Citation: Phoenix TeamPCP 20 MAY 2026)(Citation: Flashpoint Mini Shai-Hulud MAY 2026)(Citation: FBI TeamPCP JUL 2026)

## Techniques Used
- T1003.007: Proc Filesystem
- T1008: Fallback Channels
- T1016: System Network Configuration Discovery
- T1021.007: Cloud Services
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1053.006: Systemd Timers
- T1059.006: Python
- T1059.007: JavaScript
- T1059.013: Container CLI/API
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1078.004: Cloud Accounts
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087.004: Cloud Account
- T1090.003: Multi-hop Proxy
- T1102.001: Dead Drop Resolver
- T1105: Ingress Tool Transfer
- T1119: Automated Collection
- T1124: System Time Discovery
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1195.001: Compromise Software Dependencies and Development Tools
- T1205: Traffic Signaling
- T1213.003: Code Repositories
- T1480: Execution Guardrails
- T1485: Data Destruction
- T1497: Virtualization/Sandbox Evasion
- T1497.001: System Checks
- T1528: Steal Application Access Token
- T1543.001: Launch Agent
- T1543.002: Systemd Service
- T1546: Event Triggered Execution
- T1546.018: Python Startup Hooks
- T1550.001: Application Access Token
- T1552.001: Credentials In Files
- T1552.004: Private Keys
- T1552.005: Cloud Instance Metadata API
- T1552.007: Container API
- T1554: Compromise Host Software Binary
- T1555.005: Password Managers
- T1555.006: Cloud Secrets Management Stores
- T1559: Inter-Process Communication
- T1560: Archive Collected Data
- T1560.001: Archive via Utility
- T1564.011: Ignore Process Interrupts
- T1567.001: Exfiltration to Code Repository
- T1609: Container Administration Command
- T1614: System Location Discovery
- T1614.001: System Language Discovery
- T1649: Steal or Forge Authentication Certificates
- T1677: Poisoned Pipeline Execution
