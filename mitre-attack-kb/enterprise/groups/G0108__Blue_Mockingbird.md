# G0108: Blue Mockingbird

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0108  
**Aliases:** Blue Mockingbird  

## Description
[Blue Mockingbird](https://attack.mitre.org/groups/G0108) is a cluster of observed activity involving Monero cryptocurrency-mining payloads in dynamic-link library (DLL) form on Windows systems. The earliest observed Blue Mockingbird tools were created in December 2019.(Citation: RedCanary Mockingbird May 2020)

## Techniques Used
- T1003.001: LSASS Memory
- T1021.001: Remote Desktop Protocol
- T1021.002: SMB/Windows Admin Shares
- T1027.013: Encrypted/Encoded File
- T1036.005: Match Legitimate Resource Name or Location
- T1047: Windows Management Instrumentation
- T1053.005: Scheduled Task
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1082: System Information Discovery
- T1090: Proxy
- T1112: Modify Registry
- T1134: Access Token Manipulation
- T1190: Exploit Public-Facing Application
- T1218.010: Regsvr32
- T1218.011: Rundll32
- T1496.001: Compute Hijacking
- T1543.003: Windows Service
- T1546.003: Windows Management Instrumentation Event Subscription
- T1569.002: Service Execution
- T1574.012: COR_PROFILER
- T1588.002: Tool
