# S1170: ODAgent

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1170  
**Aliases:** ODAgent  
**Platforms:** Windows  

## Description
[ODAgent](https://attack.mitre.org/software/S1170) is a C#/.NET downloader that has been used by [OilRig](https://attack.mitre.org/groups/G0049) since at least 2022 including against target organizations in Israel to download and execute payloads and to exfiltrate staged files.(Citation: ESET OilRig Downloaders DEC 2023)

## Techniques Used
- T1041: Exfiltration Over C2 Channel
- T1059.003: Windows Command Shell
- T1070.004: File Deletion
- T1083: File and Directory Discovery
- T1102.002: Bidirectional Communication
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1140: Deobfuscate/Decode Files or Information
- T1567.002: Exfiltration to Cloud Storage
