# S1035: Small Sieve

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1035  
**Aliases:** Small Sieve, GRAMDOOR  
**Platforms:** Windows  

## Description
[Small Sieve](https://attack.mitre.org/software/S1035) is a Telegram Bot API-based Python backdoor that has been distributed using a Nullsoft Scriptable Install System (NSIS) Installer; it has been used by [MuddyWater](https://attack.mitre.org/groups/G0069) since at least January 2022.(Citation: DHS CISA AA22-055A MuddyWater February 2022)(Citation: NCSC GCHQ Small Sieve Jan 2022)

Security researchers have also noted [Small Sieve](https://attack.mitre.org/software/S1035)'s use by UNC3313, which may be associated with [MuddyWater](https://attack.mitre.org/groups/G0069).(Citation: Mandiant UNC3313 Feb 2022)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1027: Obfuscated Files or Information
- T1033: System Owner/User Discovery
- T1036.005: Match Legitimate Resource Name or Location
- T1059.003: Windows Command Shell
- T1059.006: Python
- T1071.001: Web Protocols
- T1102.002: Bidirectional Communication
- T1105: Ingress Tool Transfer
- T1132.002: Non-Standard Encoding
- T1480: Execution Guardrails
- T1547.001: Registry Run Keys / Startup Folder
- T1573.002: Asymmetric Cryptography
