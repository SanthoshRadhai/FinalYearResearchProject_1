# S1142: LunarMail

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1142  
**Aliases:** LunarMail  
**Platforms:** Windows  

## Description
[LunarMail](https://attack.mitre.org/software/S1142) is a backdoor that has been used by [Turla](https://attack.mitre.org/groups/G0010) since at least 2020 including in a compromise of a European ministry of foreign affairs (MFA) in conjunction with [LunarLoader](https://attack.mitre.org/software/S1143) and [LunarWeb](https://attack.mitre.org/software/S1141). [LunarMail](https://attack.mitre.org/software/S1142) is designed to be deployed on workstations and can use email messages and [Steganography](https://attack.mitre.org/techniques/T1001/002) in command and control.(Citation: ESET Turla Lunar toolset May 2024)

## Techniques Used
- T1001.002: Steganography
- T1027.013: Encrypted/Encoded File
- T1041: Exfiltration Over C2 Channel
- T1059.005: Visual Basic
- T1070.004: File Deletion
- T1070.008: Clear Mailbox Data
- T1071.003: Mail Protocols
- T1074.001: Local Data Staging
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1095: Non-Application Layer Protocol
- T1113: Screen Capture
- T1114.001: Local Email Collection
- T1137.006: Add-ins
- T1140: Deobfuscate/Decode Files or Information
- T1204.002: Malicious File
- T1543: Create or Modify System Process
