# S9014: PHASEJAM

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9014  
**Aliases:** PHASEJAM  
**Platforms:** Linux, Network Devices  

## Description
[PHASEJAM](https://attack.mitre.org/software/S9014) is a dropper written as a bash shell script that modifies Ivanti Connect Secure appliance components. [PHASEJAM](https://attack.mitre.org/software/S9014) was first reported in January 2025. [PHASEJAM](https://attack.mitre.org/software/S9014) has previously been leveraged by People's Republic of China (PRC)- affiliated actors identified as UNC5221 and SYLVANITE.(Citation: Dragos SYLVANITE MuddyWater Electrum March 2026)(Citation: Google UNC5221 Ivanti January 2025)

## Techniques Used
- T1027.010: Command Obfuscation
- T1027.013: Encrypted/Encoded File
- T1036.003: Rename Legitimate Utilities
- T1041: Exfiltration Over C2 Channel
- T1059.008: Network Device CLI
- T1105: Ingress Tool Transfer
- T1140: Deobfuscate/Decode Files or Information
- T1489: Service Stop
- T1505.003: Web Shell
- T1546.004: Unix Shell Configuration Modification
- T1554: Compromise Host Software Binary
- T1565: Data Manipulation
- T1678: Delay Execution
- T1685: Disable or Modify Tools
- T1685.003: Modify or Spoof Tool UI
