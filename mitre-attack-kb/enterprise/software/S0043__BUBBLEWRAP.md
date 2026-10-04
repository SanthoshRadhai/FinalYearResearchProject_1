# S0043: BUBBLEWRAP

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0043  
**Aliases:** BUBBLEWRAP, Backdoor.APT.FakeWinHTTPHelper  
**Platforms:** Windows  

## Description
[BUBBLEWRAP](https://attack.mitre.org/software/S0043) is a full-featured, second-stage backdoor used by the [admin@338](https://attack.mitre.org/groups/G0018) group. It is set to run when the system boots and includes functionality to check, upload, and register plug-ins that can further enhance its capabilities. (Citation: FireEye admin@338)

## Techniques Used
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1095: Non-Application Layer Protocol
