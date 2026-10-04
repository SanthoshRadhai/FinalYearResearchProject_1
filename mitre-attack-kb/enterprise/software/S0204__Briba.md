# S0204: Briba

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0204  
**Aliases:** Briba  
**Platforms:** Windows  

## Description
[Briba](https://attack.mitre.org/software/S0204) is a trojan used by [Elderwood](https://attack.mitre.org/groups/G0066) to open a backdoor and download files on to compromised hosts. (Citation: Symantec Elderwood Sept 2012) (Citation: Symantec Briba May 2012)

## Techniques Used
- T1105: Ingress Tool Transfer
- T1218.011: Rundll32
- T1543.003: Windows Service
- T1547.001: Registry Run Keys / Startup Folder
