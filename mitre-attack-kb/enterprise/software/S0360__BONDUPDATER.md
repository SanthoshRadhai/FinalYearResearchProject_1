# S0360: BONDUPDATER

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0360  
**Aliases:** BONDUPDATER  
**Platforms:** Windows  

## Description
[BONDUPDATER](https://attack.mitre.org/software/S0360) is a PowerShell backdoor used by [OilRig](https://attack.mitre.org/groups/G0049). It was first observed in November 2017 during targeting of a Middle Eastern government organization, and an updated version was observed in August 2018 being used to target a government organization with spearphishing emails.(Citation: FireEye APT34 Dec 2017)(Citation: Palo Alto OilRig Sep 2018)

## Techniques Used
- T1053.005: Scheduled Task
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1071.004: DNS
- T1105: Ingress Tool Transfer
- T1564.003: Hidden Window
- T1568.002: Domain Generation Algorithms
