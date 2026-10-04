# S1233: PAKLOG

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1233  
**Aliases:** PAKLOG  
**Platforms:** Windows  

## Description
[PAKLOG](https://attack.mitre.org/software/S1233) is a keylogger known to be leveraged by [Mustang Panda](https://attack.mitre.org/groups/G0129) and was first observed utilized in 2024. [PAKLOG](https://attack.mitre.org/software/S1233) is deployed via a RAR archive (e.g., key.rar), which contains two files: a signed, legitimate binary (PACLOUD.exe) and the malicious [PAKLOG](https://attack.mitre.org/software/S1233) DLL (pa_lang2.dll). The PACLOUD.exe binary is used to side-load the [PAKLOG](https://attack.mitre.org/software/S1233) DLL which starts with the keylogger functionality.(Citation: Zscaler PAKLOG CorkLog SplatCloak Splatdropper April 2025)

## Techniques Used
- T1010: Application Window Discovery
- T1027.013: Encrypted/Encoded File
- T1056.001: Keylogging
- T1057: Process Discovery
- T1074.001: Local Data Staging
- T1106: Native API
- T1115: Clipboard Data
- T1124: System Time Discovery
- T1553.002: Code Signing
- T1574.001: DLL
