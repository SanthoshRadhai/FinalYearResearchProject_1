# S1231: GodFather

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1231  
**Aliases:** GodFather  
**Platforms:** Android  

## Description
[GodFather](https://attack.mitre.org/software/S1231) is an Android banking malware that uses virtualization to mimic legitimate applications and abuses accessibility services and other permissions to evade detection and exfiltrate sensitive data. First identified in 2020, [GodFather](https://attack.mitre.org/software/S1231) targets nearly 500 banking applications, cryptocurrency wallets, and exchanges worldwide; however, its virtualization-based attacks have primarily focused on several Turkish financial institutions. This capability enables threat actors to steal banking credentials and other sensitive account information. (Citation: ZimperiumOrtegaPratapagiri_GodFather_Jun2025)(Citation: MerkleScience_Godfather_April2023)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1417: Input Capture
- T1417.001: Keylogging
- T1418: Software Discovery
- T1422: System Network Configuration Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1437.001: Web Protocols
- T1453: Abuse Accessibility Features
- T1516: Input Injection
- T1544: Ingress Tool Transfer
- T1575: Native API
- T1582: SMS Control
- T1603: Scheduled Task/Job
- T1616: Call Control
- T1617: Hooking
- T1624: Event Triggered Execution
- T1629: Impair Defenses
- T1629.001: Prevent Application Removal
- T1630: Indicator Removal on Host
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1646: Exfiltration Over C2 Channel
- T1655.001: Match Legitimate Name or Location
- T1660: Phishing
- T1670: Virtualization Solution
