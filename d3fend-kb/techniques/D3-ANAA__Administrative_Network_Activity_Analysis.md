# D3-ANAA: Administrative Network Activity Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-ANAA/  

## Definition
Detection of unauthorized use of administrative network protocols by analyzing network activity against a baseline.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** Intranet Administrative Network Traffic
- **created:** 2020-08-05T00:00:00
- **kb-reference:** Reference - Method and system for detecting suspicious administrative activity - Vectra Networks Inc
- **kb-reference:** Reference - CAR-2014-11-005: Remote Registry - MITRE
- **kb-reference:** Reference - CAR-2014-11-006: Windows Remote Management (WinRM) - MITRE

## Knowledge Base Article
## How it works
Network protocols such as RDP, IPMI, SSH, SNMP, VNC, MOSH, NX, TeamViewer, SPICE, PCoIP, and others are used by system administrators to remotely manage servers. Defenders monitor administrative network activity to determine if the use of remote protocols is malicious. Attackers can abuse administrative protocols and leverage them for initial access to various endpoints. For example, an attacker with valid credentials will remotely SSH or RDP into a server and attempt to blend in with existing traffic from system administrators. By monitoring the traffic activity, it is possible to detect when the protocols are behaving differently from a known baseline of system administration activity.

## Considerations
* Administrative traffic can be encrypted, making network protocol analysis a challenge
* False alarms can be mitigated by integration with inventory management systems
