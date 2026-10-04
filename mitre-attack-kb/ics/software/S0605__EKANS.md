# S0605: EKANS

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0605  
**Aliases:** EKANS, SNAKEHOSE  
**Platforms:** Windows  

## Description
[EKANS](https://attack.mitre.org/software/S0605) is ransomware variant written in Golang that first appeared in mid-December 2019 and has been used against multiple sectors, including energy, healthcare, and automotive manufacturing, which in some cases resulted in significant operational disruptions. [EKANS](https://attack.mitre.org/software/S0605) has used a hard-coded kill-list of processes, including some associated with common ICS software platforms (e.g., GE Proficy, Honeywell HMIWeb, etc), similar to those defined in [MegaCortex](https://attack.mitre.org/software/S0576).(Citation: Dragos EKANS)(Citation: Palo Alto Unit 42 EKANS)

## Techniques Used
- T0828: Loss of Productivity and Revenue
- T0840: Network Connection Enumeration
- T0849: Masquerading
- T0881: Service Stop
