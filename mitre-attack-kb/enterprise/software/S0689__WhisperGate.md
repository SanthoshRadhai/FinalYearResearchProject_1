# S0689: WhisperGate

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0689  
**Aliases:** WhisperGate  
**Platforms:** Windows  

## Description
[WhisperGate](https://attack.mitre.org/software/S0689) is a multi-stage wiper designed to look like ransomware that has been used against multiple government, non-profit, and information technology organizations in Ukraine since at least January 2022.(Citation: Cybereason WhisperGate February 2022)(Citation: Unit 42 WhisperGate January 2022)(Citation: Microsoft WhisperGate January 2022)

## Techniques Used
- T1027.013: Encrypted/Encoded File
- T1036: Masquerading
- T1055.012: Process Hollowing
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.005: Visual Basic
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1083: File and Directory Discovery
- T1102: Web Service
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1134.002: Create Process with Token
- T1135: Network Share Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1218.004: InstallUtil
- T1485: Data Destruction
- T1497.001: System Checks
- T1497.003: Time Based Checks
- T1518.001: Security Software Discovery
- T1529: System Shutdown/Reboot
- T1542.003: Bootkit
- T1561.001: Disk Content Wipe
- T1561.002: Disk Structure Wipe
- T1569.002: Service Execution
- T1620: Reflective Code Loading
- T1680: Local Storage Discovery
- T1685: Disable or Modify Tools
