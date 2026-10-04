# S0412: ZxShell

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0412  
**Aliases:** ZxShell, Sensocode  
**Platforms:** Windows  

## Description
[ZxShell](https://attack.mitre.org/software/S0412) is a remote administration tool and backdoor that can be downloaded from the Internet, particularly from Chinese hacker websites. It has been used since at least 2004.(Citation: FireEye APT41 Aug 2019)(Citation: Talos ZxShell Oct 2014)

## Techniques Used
- T1005: Data from Local System
- T1007: System Service Discovery
- T1012: Query Registry
- T1021.001: Remote Desktop Protocol
- T1021.005: VNC
- T1033: System Owner/User Discovery
- T1046: Network Service Discovery
- T1055.001: Dynamic-link Library Injection
- T1056.001: Keylogging
- T1056.004: Credential API Hooking
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1071.002: File Transfer Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1090: Proxy
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1112: Modify Registry
- T1113: Screen Capture
- T1125: Video Capture
- T1134.002: Create Process with Token
- T1136.001: Local Account
- T1190: Exploit Public-Facing Application
- T1218.011: Rundll32
- T1499: Endpoint Denial of Service
- T1543.003: Windows Service
- T1569.002: Service Execution
- T1571: Non-Standard Port
- T1685: Disable or Modify Tools
- T1685.005: Clear Windows Event Logs
- T1686: Disable or Modify System Firewall
