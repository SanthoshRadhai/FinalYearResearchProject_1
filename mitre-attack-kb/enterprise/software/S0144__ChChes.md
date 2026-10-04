# S0144: ChChes

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0144  
**Aliases:** ChChes, Scorpion, HAYMAKER  
**Platforms:** Windows  

## Description
[ChChes](https://attack.mitre.org/software/S0144) is a Trojan that appears to be used exclusively by [menuPass](https://attack.mitre.org/groups/G0045). It was used to target Japanese organizations in 2016. Its lack of persistence methods suggests it may be intended as a first-stage tool. (Citation: Palo Alto menuPass Feb 2017) (Citation: JPCERT ChChes Feb 2017) (Citation: PWC Cloud Hopper Technical Annex April 2017)

## Techniques Used
- T1036.005: Match Legitimate Resource Name or Location
- T1057: Process Discovery
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1132.001: Standard Encoding
- T1547.001: Registry Run Keys / Startup Folder
- T1553.002: Code Signing
- T1555.003: Credentials from Web Browsers
- T1573.001: Symmetric Cryptography
- T1685: Disable or Modify Tools
