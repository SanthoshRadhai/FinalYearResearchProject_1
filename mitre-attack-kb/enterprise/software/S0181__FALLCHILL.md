# S0181: FALLCHILL

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0181  
**Aliases:** FALLCHILL  
**Platforms:** Windows  

## Description
[FALLCHILL](https://attack.mitre.org/software/S0181) is a RAT that has been used by [Lazarus Group](https://attack.mitre.org/groups/G0032) since at least 2016 to target the aerospace, telecommunications, and finance industries. It is usually dropped by other [Lazarus Group](https://attack.mitre.org/groups/G0032) malware or delivered when a victim unknowingly visits a compromised website. (Citation: US-CERT FALLCHILL Nov 2017)

## Techniques Used
- T1001.003: Protocol or Service Impersonation
- T1016: System Network Configuration Discovery
- T1070.004: File Deletion
- T1070.006: Timestomp
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1543.003: Windows Service
- T1573.001: Symmetric Cryptography
- T1680: Local Storage Discovery
