# S9042: CanisterWorm

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9042  
**Aliases:** CanisterWorm  
**Platforms:** Containers, Linux  

## Description
[CanisterWorm](https://attack.mitre.org/software/S9042) is a self-propagating malware that has been used by [TeamPCP](https://attack.mitre.org/groups/G1056) in credential harvesting and software supply chain campaigns since at least 2026. [CanisterWorm](https://attack.mitre.org/software/S9042) has used npm credentials to infect software packages and propagate across developer ecosystems. [CanisterWorm](https://attack.mitre.org/software/S9042) has a targeted wiper component and can use decentralized C2 infrastructure implemented via an Internet Computer Protocol (ICP) blockchain canister.(Citation: Aikido TeamPCP Telnyx MAR 2026)(Citation: Palo Alto TeamPCP MAR 2026)(Citation: Aikido CanisterWorm MAR 2026)(Citation: Aikido TeamPCP Trivy MAR 2026)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1018: Remote System Discovery
- T1027.009: Embedded Payloads
- T1033: System Owner/User Discovery
- T1036.004: Masquerade Task or Service
- T1036.005: Match Legitimate Resource Name or Location
- T1053.006: Systemd Timers
- T1059.004: Unix Shell
- T1059.006: Python
- T1059.007: JavaScript
- T1070.004: File Deletion
- T1083: File and Directory Discovery
- T1102.001: Dead Drop Resolver
- T1105: Ingress Tool Transfer
- T1124: System Time Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1195.001: Compromise Software Dependencies and Development Tools
- T1480: Execution Guardrails
- T1485: Data Destruction
- T1497.003: Time Based Checks
- T1528: Steal Application Access Token
- T1529: System Shutdown/Reboot
- T1543: Create or Modify System Process
- T1548.003: Sudo and Sudo Caching
- T1550.001: Application Access Token
- T1552.004: Private Keys
- T1555.006: Cloud Secrets Management Stores
- T1569.003: Systemctl
- T1609: Container Administration Command
- T1613: Container and Resource Discovery
- T1614.001: System Language Discovery
- T1677: Poisoned Pipeline Execution
