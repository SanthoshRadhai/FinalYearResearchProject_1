# S1171: OilCheck

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1171  
**Aliases:** OilCheck  
**Platforms:** Windows  

## Description
[OilCheck](https://attack.mitre.org/software/S1171) is a C#/.NET downloader that has been used by [OilRig](https://attack.mitre.org/groups/G0049) since at least 2022 including against targets in Israel. [OilCheck](https://attack.mitre.org/software/S1171) uses draft messages created in a shared email account for C2 communication.(Citation: ESET OilRig Downloaders DEC 2023)

## Techniques Used
- T1102.002: Bidirectional Communication
- T1105: Ingress Tool Transfer
- T1567: Exfiltration Over Web Service
