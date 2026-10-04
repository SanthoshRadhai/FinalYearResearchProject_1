# S9025: NOOPLDR

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9025  
**Aliases:** NOOPLDR  
**Platforms:** Windows  

## Description
[NOOPLDR](https://attack.mitre.org/software/S9025) is a shellcode loader with XML/C# and DLL versions that has been used by [MirrorFace](https://attack.mitre.org/groups/G1054) to load [HiddenFace](https://attack.mitre.org/software/S9023).(Citation: Trend Micro Earth Kasha NOV 2024)

## Techniques Used
- T1027: Obfuscated Files or Information
- T1027.013: Encrypted/Encoded File
- T1027.016: Junk Code Insertion
- T1055: Process Injection
- T1070.004: File Deletion
- T1082: System Information Discovery
- T1106: Native API
- T1112: Modify Registry
- T1127.001: MSBuild
- T1140: Deobfuscate/Decode Files or Information
- T1564: Hide Artifacts
- T1574.001: DLL
