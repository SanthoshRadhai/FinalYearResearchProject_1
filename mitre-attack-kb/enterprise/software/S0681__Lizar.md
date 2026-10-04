# S0681: Lizar

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0681  
**Aliases:** Lizar, Tirion, Icebot, DiceLoader  
**Platforms:** Windows  

## Description
[Lizar](https://attack.mitre.org/software/S0681) is a modular remote access tool written using the .NET Framework that shares structural similarities to [Carbanak](https://attack.mitre.org/software/S0030). It has likely been used by [FIN7](https://attack.mitre.org/groups/G0046) since at least February 2021.(Citation: BiZone Lizar May 2021)(Citation: Threatpost Lizar May 2021)(Citation: Gemini FIN7 Oct 2021)

## Techniques Used
- T1003.001: LSASS Memory
- T1016: System Network Configuration Discovery
- T1027: Obfuscated Files or Information
- T1033: System Owner/User Discovery
- T1049: System Network Connections Discovery
- T1055: Process Injection
- T1055.001: Dynamic-link Library Injection
- T1055.002: Portable Executable Injection
- T1057: Process Discovery
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.006: Python
- T1082: System Information Discovery
- T1087.003: Email Account
- T1095: Non-Application Layer Protocol
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1113: Screen Capture
- T1132.002: Non-Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1217: Browser Information Discovery
- T1518.001: Security Software Discovery
- T1555.003: Credentials from Web Browsers
- T1555.004: Windows Credential Manager
- T1560: Archive Collected Data
- T1573: Encrypted Channel
- T1588.002: Tool
- T1620: Reflective Code Loading
