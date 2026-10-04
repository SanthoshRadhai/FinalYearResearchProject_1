# S0234: Bandook

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0234  
**Aliases:** Bandook  
**Platforms:** Windows  

## Description
[Bandook](https://attack.mitre.org/software/S0234) is a commercially available RAT, written in Delphi and C++, that has been available since at least 2007. It has been used against government, financial, energy, healthcare, education, IT, and legal organizations in the US, South America, Europe, and Southeast Asia. [Bandook](https://attack.mitre.org/software/S0234) has been used by [Dark Caracal](https://attack.mitre.org/groups/G0070), as well as in a separate campaign referred to as "Operation Manul".(Citation: EFF Manul Aug 2016)(Citation: Lookout Dark Caracal Jan 2018)(Citation: CheckPoint Bandook Nov 2020)

## Techniques Used
- T1005: Data from Local System
- T1016: System Network Configuration Discovery
- T1027.003: Steganography
- T1041: Exfiltration Over C2 Channel
- T1055.012: Process Hollowing
- T1056.001: Keylogging
- T1059: Command and Scripting Interpreter
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1059.006: Python
- T1070.004: File Deletion
- T1083: File and Directory Discovery
- T1095: Non-Application Layer Protocol
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1113: Screen Capture
- T1120: Peripheral Device Discovery
- T1123: Audio Capture
- T1125: Video Capture
- T1140: Deobfuscate/Decode Files or Information
- T1204.002: Malicious File
- T1553.002: Code Signing
- T1566.001: Spearphishing Attachment
- T1573.001: Symmetric Cryptography
- T1680: Local Storage Discovery
