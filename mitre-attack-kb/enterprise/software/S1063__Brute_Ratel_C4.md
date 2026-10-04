# S1063: Brute Ratel C4

**Type:** tool  
**Reference:** https://attack.mitre.org/software/S1063  
**Aliases:** Brute Ratel C4, BRc4  
**Platforms:** Windows  

## Description
[Brute Ratel C4](https://attack.mitre.org/software/S1063) is a commercial red-teaming and adversarial attack simulation tool that first appeared in December 2020. [Brute Ratel C4](https://attack.mitre.org/software/S1063) was specifically designed to avoid detection by endpoint detection and response (EDR) and antivirus (AV) capabilities, and deploys agents called badgers to enable arbitrary command execution for lateral movement, privilege escalation, and persistence. In September 2022, a cracked version of [Brute Ratel C4](https://attack.mitre.org/software/S1063) was leaked in the cybercriminal underground, leading to its use by threat actors.(Citation: Dark Vortex Brute Ratel C4)(Citation: Palo Alto Brute Ratel July 2022)(Citation: MDSec Brute Ratel August 2022)(Citation: SANS Brute Ratel October 2022)(Citation: Trend Micro Black Basta October 2022)

## Techniques Used
- T1005: Data from Local System
- T1021: Remote Services
- T1021.002: SMB/Windows Admin Shares
- T1021.006: Windows Remote Management
- T1027: Obfuscated Files or Information
- T1027.007: Dynamic API Resolution
- T1036.005: Match Legitimate Resource Name or Location
- T1036.008: Masquerade File Type
- T1046: Network Service Discovery
- T1047: Windows Management Instrumentation
- T1055.002: Portable Executable Injection
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1069.002: Domain Groups
- T1071.001: Web Protocols
- T1071.004: DNS
- T1087.002: Domain Account
- T1095: Non-Application Layer Protocol
- T1102: Web Service
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1113: Screen Capture
- T1140: Deobfuscate/Decode Files or Information
- T1204.002: Malicious File
- T1482: Domain Trust Discovery
- T1497.003: Time Based Checks
- T1518.001: Security Software Discovery
- T1558.003: Kerberoasting
- T1569.002: Service Execution
- T1572: Protocol Tunneling
- T1574.001: DLL
- T1620: Reflective Code Loading
- T1685: Disable or Modify Tools
