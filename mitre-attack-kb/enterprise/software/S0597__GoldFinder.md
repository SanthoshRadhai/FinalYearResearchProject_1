# S0597: GoldFinder

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0597  
**Aliases:** GoldFinder  
**Platforms:** Windows  

## Description
[GoldFinder](https://attack.mitre.org/software/S0597) is a custom HTTP tracer tool written in Go that logs the route a packet takes between a compromised network and a C2 server. It can be used to inform  threat actors of potential points of discovery or logging of their actions, including C2 related to other malware. [GoldFinder](https://attack.mitre.org/software/S0597) was discovered in early 2021 during an investigation into the [SolarWinds Compromise](https://attack.mitre.org/campaigns/C0024) by [APT29](https://attack.mitre.org/groups/G0016).(Citation: MSTIC NOBELIUM Mar 2021)

## Techniques Used
- T1016.001: Internet Connection Discovery
- T1071.001: Web Protocols
- T1119: Automated Collection
