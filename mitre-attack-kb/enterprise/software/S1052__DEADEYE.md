# S1052: DEADEYE

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1052  
**Aliases:** DEADEYE, DEADEYE.EMBED, DEADEYE.APPEND  
**Platforms:** Windows  

## Description
[DEADEYE](https://attack.mitre.org/software/S1052) is a malware launcher that has been used by [APT41](https://attack.mitre.org/groups/G0096) since at least May 2021. [DEADEYE](https://attack.mitre.org/software/S1052) has variants that can either embed a payload inside a compiled binary (DEADEYE.EMBED) or append it to the end of a file (DEADEYE.APPEND).(Citation: Mandiant APT41)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1027.009: Embedded Payloads
- T1027.013: Encrypted/Encoded File
- T1036.004: Masquerade Task or Service
- T1059.003: Windows Command Shell
- T1082: System Information Discovery
- T1106: Native API
- T1140: Deobfuscate/Decode Files or Information
- T1218.007: Msiexec
- T1218.011: Rundll32
- T1480: Execution Guardrails
- T1564.004: NTFS File Attributes
