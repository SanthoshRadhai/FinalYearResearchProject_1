# S1235: CorKLOG

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1235  
**Aliases:** CorKLOG  
**Platforms:** Windows  

## Description
[CorKLOG](https://attack.mitre.org/software/S1235) is a keylogger known to be leveraged by [Mustang Panda](https://attack.mitre.org/groups/G0129) and was first observed utilized in 2024. [CorKLOG](https://attack.mitre.org/software/S1235) is delivered through a RAR archive (e.g., src.rar), which contains two files: an executable (lcommute.exe) and the [CorKLOG](https://attack.mitre.org/software/S1235) DLL (mscorsvc.dll).  [CorKLOG](https://attack.mitre.org/software/S1235) has established persistence on the system by creating services or with scheduled tasks.(Citation: Zscaler PAKLOG CorkLog SplatCloak Splatdropper April 2025)

## Techniques Used
- T1027.013: Encrypted/Encoded File
- T1053.005: Scheduled Task
- T1056.001: Keylogging
- T1074.001: Local Data Staging
- T1140: Deobfuscate/Decode Files or Information
- T1543.003: Windows Service
- T1553.002: Code Signing
- T1574.001: DLL
