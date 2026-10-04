# S0145: POWERSOURCE

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0145  
**Aliases:** POWERSOURCE, DNSMessenger  
**Platforms:** Windows  

## Description
[POWERSOURCE](https://attack.mitre.org/software/S0145) is a PowerShell backdoor that is a heavily obfuscated and modified version of the publicly available tool DNS_TXT_Pwnage. It was observed in February 2017 in spearphishing campaigns against personnel involved with United States Securities and Exchange Commission (SEC) filings at various organizations. The malware was delivered when macros were enabled by the victim and a VBS script was dropped. (Citation: FireEye FIN7 March 2017) (Citation: Cisco DNSMessenger March 2017)

## Techniques Used
- T1012: Query Registry
- T1059.001: PowerShell
- T1071.004: DNS
- T1105: Ingress Tool Transfer
- T1547.001: Registry Run Keys / Startup Folder
- T1564.004: NTFS File Attributes
