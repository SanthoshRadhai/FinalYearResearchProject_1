# S0445: ShimRatReporter

**Type:** tool  
**Reference:** https://attack.mitre.org/software/S0445  
**Aliases:** ShimRatReporter  
**Platforms:** Windows  

## Description
[ShimRatReporter](https://attack.mitre.org/software/S0445) is a tool used by suspected Chinese adversary [Mofang](https://attack.mitre.org/groups/G0103) to automatically conduct initial discovery. The details from this discovery are used to customize follow-on payloads (such as [ShimRat](https://attack.mitre.org/software/S0444)) as well as set up faux infrastructure which mimics the adversary's targets. [ShimRatReporter](https://attack.mitre.org/software/S0445) has been used in campaigns targeting multiple countries and sectors including government, military, critical infrastructure, automobile, and weapons development.(Citation: FOX-IT May 2016 Mofang)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1020: Automated Exfiltration
- T1027: Obfuscated Files or Information
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1049: System Network Connections Discovery
- T1057: Process Discovery
- T1069: Permission Groups Discovery
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1087: Account Discovery
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1119: Automated Collection
- T1518: Software Discovery
- T1560: Archive Collected Data
