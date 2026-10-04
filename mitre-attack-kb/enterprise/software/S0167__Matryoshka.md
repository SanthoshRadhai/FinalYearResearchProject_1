# S0167: Matryoshka

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0167  
**Aliases:** Matryoshka  
**Platforms:** Windows  

## Description
[Matryoshka](https://attack.mitre.org/software/S0167) is a malware framework used by [CopyKittens](https://attack.mitre.org/groups/G0052) that consists of a dropper, loader, and RAT. It has multiple versions; v1 was seen in the wild from July 2016 until January 2017. v2 has fewer commands and other minor differences. (Citation: ClearSky Wilted Tulip July 2017) (Citation: CopyKittens Nov 2015)

## Techniques Used
- T1027: Obfuscated Files or Information
- T1053.005: Scheduled Task
- T1055.001: Dynamic-link Library Injection
- T1056.001: Keylogging
- T1059: Command and Scripting Interpreter
- T1071.004: DNS
- T1113: Screen Capture
- T1218.011: Rundll32
- T1547.001: Registry Run Keys / Startup Folder
- T1555: Credentials from Password Stores
