# S1237: CANONSTAGER

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1237  
**Aliases:** CANONSTAGER  
**Platforms:** Windows  

## Description
[CANONSTAGER](https://attack.mitre.org/software/S1237) is a loader known to be leveraged by [Mustang Panda](https://attack.mitre.org/groups/G0129) and was first observed utilized in 2025.  [Mustang Panda](https://attack.mitre.org/groups/G0129) utilizes DLL side-loading to execute within the victim environment prior to delivering a follow-on malicious encrypted payload.  [CANONSTAGER](https://attack.mitre.org/software/S1237) leverages Thread Local Storage (TLS) and Native Windows APIs within the victim environment to elude detections. [CANONSTAGER](https://attack.mitre.org/software/S1237) also hides its code utilizing window procedures and message queues.(Citation: Google Threat Intelligence Group MUSTANG PANDA PLUGX August 2025)

## Techniques Used
- T1027.007: Dynamic API Resolution
- T1036.005: Match Legitimate Resource Name or Location
- T1055.005: Thread Local Storage
- T1106: Native API
- T1564.003: Hidden Window
- T1574.001: DLL
