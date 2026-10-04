# S0526: KGH_SPY

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0526  
**Aliases:** KGH_SPY  
**Platforms:** Windows  

## Description
[KGH_SPY](https://attack.mitre.org/software/S0526) is a modular suite of tools used by [Kimsuky](https://attack.mitre.org/groups/G0094) for reconnaissance, information stealing, and backdoor capabilities. [KGH_SPY](https://attack.mitre.org/software/S0526) derived its name from PDB paths and internal names found in samples containing "KGH".(Citation: Cybereason Kimsuky November 2020)

## Techniques Used
- T1005: Data from Local System
- T1027.013: Encrypted/Encoded File
- T1036.005: Match Legitimate Resource Name or Location
- T1037.001: Logon Script (Windows)
- T1041: Exfiltration Over C2 Channel
- T1056.001: Keylogging
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1071.001: Web Protocols
- T1074.001: Local Data Staging
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1114.001: Local Email Collection
- T1140: Deobfuscate/Decode Files or Information
- T1204.002: Malicious File
- T1518: Software Discovery
- T1555: Credentials from Password Stores
- T1555.003: Credentials from Web Browsers
- T1555.004: Windows Credential Manager
- T1680: Local Storage Discovery
