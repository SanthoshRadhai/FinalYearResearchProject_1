# S0236: Kwampirs

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0236  
**Aliases:** Kwampirs  
**Platforms:** Windows  

## Description
[Kwampirs](https://attack.mitre.org/software/S0236) is a backdoor Trojan used by [Orangeworm](https://attack.mitre.org/groups/G0071). [Kwampirs](https://attack.mitre.org/software/S0236) has been found on machines which had software installed for the use and control of high-tech imaging devices such as X-Ray and MRI machines.(Citation: Symantec Orangeworm April 2018) [Kwampirs](https://attack.mitre.org/software/S0236) has multiple technical overlaps with [Shamoon](https://attack.mitre.org/software/S0140) based on reverse engineering analysis.(Citation: Cylera Kwampirs 2022)

## Techniques Used
- T1007: System Service Discovery
- T1008: Fallback Channels
- T1016: System Network Configuration Discovery
- T1018: Remote System Discovery
- T1021.002: SMB/Windows Admin Shares
- T1027.001: Binary Padding
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1036.004: Masquerade Task or Service
- T1049: System Network Connections Discovery
- T1057: Process Discovery
- T1069.001: Local Groups
- T1069.002: Domain Groups
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087.001: Local Account
- T1105: Ingress Tool Transfer
- T1135: Network Share Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1201: Password Policy Discovery
- T1218.011: Rundll32
- T1543.003: Windows Service
