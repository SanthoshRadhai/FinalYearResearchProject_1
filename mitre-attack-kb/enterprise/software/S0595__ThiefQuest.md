# S0595: ThiefQuest

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0595  
**Aliases:** ThiefQuest, MacRansom.K, EvilQuest  
**Platforms:** macOS  

## Description
[ThiefQuest](https://attack.mitre.org/software/S0595) is a virus, data stealer, and wiper that presents itself as ransomware targeting macOS systems. [ThiefQuest](https://attack.mitre.org/software/S0595) was first seen in 2020 distributed via trojanized pirated versions of popular macOS software on Russian forums sharing torrent links.(Citation: Reed thiefquest fake ransom) Even though [ThiefQuest](https://attack.mitre.org/software/S0595) presents itself as ransomware, since the dynamically generated encryption key is never sent to the attacker it may be more appropriately thought of as a form of wiper malware.(Citation: wardle evilquest partii)(Citation: reed thiefquest ransomware analysis)

## Techniques Used
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1056.001: Keylogging
- T1057: Process Discovery
- T1059.002: AppleScript
- T1071.001: Web Protocols
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1486: Data Encrypted for Impact
- T1497.003: Time Based Checks
- T1518.001: Security Software Discovery
- T1543.001: Launch Agent
- T1543.004: Launch Daemon
- T1554: Compromise Host Software Binary
- T1564.001: Hidden Files and Directories
- T1620: Reflective Code Loading
- T1622: Debugger Evasion
- T1685: Disable or Modify Tools
