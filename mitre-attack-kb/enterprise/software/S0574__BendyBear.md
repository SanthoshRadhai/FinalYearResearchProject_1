# S0574: BendyBear

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0574  
**Aliases:** BendyBear  
**Platforms:** Windows  

## Description
[BendyBear](https://attack.mitre.org/software/S0574) is an x64 shellcode for a stage-zero implant designed to download malware from a C2 server. First discovered in August 2020, [BendyBear](https://attack.mitre.org/software/S0574) shares a variety of features with [Waterbear](https://attack.mitre.org/software/S0579), malware previously attributed to the Chinese cyber espionage group [BlackTech](https://attack.mitre.org/groups/G0098).(Citation: Unit42 BendyBear Feb 2021)

## Techniques Used
- T1001.001: Junk Data
- T1012: Query Registry
- T1027.013: Encrypted/Encoded File
- T1027.014: Polymorphic Code
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1124: System Time Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1497.003: Time Based Checks
- T1571: Non-Standard Port
- T1573.001: Symmetric Cryptography
