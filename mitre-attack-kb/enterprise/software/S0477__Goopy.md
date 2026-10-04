# S0477: Goopy

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0477  
**Aliases:** Goopy  
**Platforms:** Windows  

## Description
[Goopy](https://attack.mitre.org/software/S0477) is a Windows backdoor and Trojan used by [APT32](https://attack.mitre.org/groups/G0050) and shares several similarities to another backdoor used by the group ([Denis](https://attack.mitre.org/software/S0354)). [Goopy](https://attack.mitre.org/software/S0477) is named for its impersonation of the legitimate Google Updater executable.(Citation: Cybereason Cobalt Kitty 2017)

## Techniques Used
- T1005: Data from Local System
- T1027.001: Binary Padding
- T1027.016: Junk Code Insertion
- T1033: System Owner/User Discovery
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1053.005: Scheduled Task
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1070.008: Clear Mailbox Data
- T1071.001: Web Protocols
- T1071.003: Mail Protocols
- T1071.004: DNS
- T1106: Native API
- T1140: Deobfuscate/Decode Files or Information
- T1574.001: DLL
- T1685: Disable or Modify Tools
