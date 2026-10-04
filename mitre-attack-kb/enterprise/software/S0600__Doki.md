# S0600: Doki

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0600  
**Aliases:** Doki  
**Platforms:** Linux, Containers  

## Description
[Doki](https://attack.mitre.org/software/S0600) is a backdoor that uses a unique Dogecoin-based Domain Generation Algorithm and was first observed in July 2020. [Doki](https://attack.mitre.org/software/S0600) was used in conjunction with the [ngrok](https://attack.mitre.org/software/S0508) Mining Botnet in a campaign that targeted Docker servers in cloud platforms. (Citation: Intezer Doki July 20)

## Techniques Used
- T1020: Automated Exfiltration
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1057: Process Discovery
- T1059.004: Unix Shell
- T1071.001: Web Protocols
- T1083: File and Directory Discovery
- T1102: Web Service
- T1105: Ingress Tool Transfer
- T1133: External Remote Services
- T1568.002: Domain Generation Algorithms
- T1573.002: Asymmetric Cryptography
- T1610: Deploy Container
- T1611: Escape to Host
