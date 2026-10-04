# S1143: LunarLoader

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1143  
**Aliases:** LunarLoader  
**Platforms:** Windows  

## Description
[LunarLoader](https://attack.mitre.org/software/S1143) is the loader component for the [LunarWeb](https://attack.mitre.org/software/S1141) and [LunarMail](https://attack.mitre.org/software/S1142) backdoors that has been used by [Turla](https://attack.mitre.org/groups/G0010) since at least 2020 including against a European ministry of foreign affairs (MFA). [LunarLoader](https://attack.mitre.org/software/S1143) has been observed as a standalone and as a part of trojanized open-source software such as AdmPwd.(Citation: ESET Turla Lunar toolset May 2024)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1137.006: Add-ins
- T1140: Deobfuscate/Decode Files or Information
- T1480: Execution Guardrails
- T1620: Reflective Code Loading
