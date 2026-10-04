# S0182: FinFisher

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0182  
**Aliases:** FinFisher, FinSpy  
**Platforms:** Windows, Android  

## Description
[FinFisher](https://attack.mitre.org/software/S0182) is a government-grade commercial surveillance spyware reportedly sold exclusively to government agencies for use in targeted and lawful criminal investigations. It is heavily obfuscated and uses multiple anti-analysis techniques. It has other variants including [Wingbird](https://attack.mitre.org/software/S0176). (Citation: FinFisher Citation) (Citation: Microsoft SIR Vol 21) (Citation: FireEye FinSpy Sept 2017) (Citation: Securelist BlackOasis Oct 2017) (Citation: Microsoft FinFisher March 2018)

## Techniques Used
- T1012: Query Registry
- T1027: Obfuscated Files or Information
- T1027.002: Software Packing
- T1027.016: Junk Code Insertion
- T1036.005: Match Legitimate Resource Name or Location
- T1055.001: Dynamic-link Library Injection
- T1056.004: Credential API Hooking
- T1057: Process Discovery
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1113: Screen Capture
- T1134.001: Token Impersonation/Theft
- T1140: Deobfuscate/Decode Files or Information
- T1497.001: System Checks
- T1518.001: Security Software Discovery
- T1542.003: Bootkit
- T1543.003: Windows Service
- T1547.001: Registry Run Keys / Startup Folder
- T1548.002: Bypass User Account Control
- T1574.001: DLL
- T1574.013: KernelCallbackTable
- T1685.005: Clear Windows Event Logs
