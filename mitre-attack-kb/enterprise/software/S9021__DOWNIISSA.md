# S9021: DOWNIISSA

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9021  
**Aliases:** DOWNIISSA  
**Platforms:** Windows  

## Description
[DOWNIISSA](https://attack.mitre.org/software/S9021) is a shellcode downloader that has been used by [MirrorFace](https://attack.mitre.org/groups/G1054) since at least 2022 to deploy payloads, including the [LODEINFO](https://attack.mitre.org/software/S9020) backdoor.(Citation: Kaspersky LODEINFO OCT 2022)

## Techniques Used
- T1027.013: Encrypted/Encoded File
- T1055: Process Injection
- T1070.004: File Deletion
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1140: Deobfuscate/Decode Files or Information
- T1218.007: Msiexec
