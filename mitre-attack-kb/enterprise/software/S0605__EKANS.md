# S0605: EKANS

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0605  
**Aliases:** EKANS, SNAKEHOSE  
**Platforms:** Windows  

## Description
[EKANS](https://attack.mitre.org/software/S0605) is ransomware variant written in Golang that first appeared in mid-December 2019 and has been used against multiple sectors, including energy, healthcare, and automotive manufacturing, which in some cases resulted in significant operational disruptions. [EKANS](https://attack.mitre.org/software/S0605) has used a hard-coded kill-list of processes, including some associated with common ICS software platforms (e.g., GE Proficy, Honeywell HMIWeb, etc), similar to those defined in [MegaCortex](https://attack.mitre.org/software/S0576).(Citation: Dragos EKANS)(Citation: Palo Alto Unit 42 EKANS)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1027: Obfuscated Files or Information
- T1036.005: Match Legitimate Resource Name or Location
- T1047: Windows Management Instrumentation
- T1057: Process Discovery
- T1486: Data Encrypted for Impact
- T1489: Service Stop
- T1490: Inhibit System Recovery
- T1685: Disable or Modify Tools
