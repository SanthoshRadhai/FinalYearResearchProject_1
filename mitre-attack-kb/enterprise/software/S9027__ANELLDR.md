# S9027: ANELLDR

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9027  
**Aliases:** ANELLDR  
**Platforms:** Windows  

## Description
[ANELLDR](https://attack.mitre.org/software/S9027), a loader that has been in use since at least 2018, was designed to decrypt and execute [UPPERCUT](https://attack.mitre.org/software/S0275) in memory. [ANELLDR](https://attack.mitre.org/software/S9027) can use anti-analysis techniques and is known to share code overlap with [HiddenFace](https://attack.mitre.org/software/S9023).(Citation: Trend Micro Earth Kasha Anel NOV 2024)(Citation: ESET MirrorFace 2025)

## Techniques Used
- T1027: Obfuscated Files or Information
- T1027.013: Encrypted/Encoded File
- T1027.016: Junk Code Insertion
- T1083: File and Directory Discovery
- T1106: Native API
- T1140: Deobfuscate/Decode Files or Information
- T1574.001: DLL
- T1622: Debugger Evasion
