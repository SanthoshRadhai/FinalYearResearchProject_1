# S0486: Bonadan

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0486  
**Aliases:** Bonadan  
**Platforms:** Linux  

## Description
[Bonadan](https://attack.mitre.org/software/S0486) is a malicious version of OpenSSH which acts as a custom backdoor. [Bonadan](https://attack.mitre.org/software/S0486) has been active since at least 2018 and combines a new cryptocurrency-mining module with the same credential-stealing module used by the Onderon family of backdoors.(Citation: ESET ForSSHe December 2018)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1033: System Owner/User Discovery
- T1057: Process Discovery
- T1059: Command and Scripting Interpreter
- T1082: System Information Discovery
- T1105: Ingress Tool Transfer
- T1496.001: Compute Hijacking
- T1554: Compromise Host Software Binary
- T1573.001: Symmetric Cryptography
