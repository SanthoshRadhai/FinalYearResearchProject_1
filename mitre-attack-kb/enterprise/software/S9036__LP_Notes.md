# S9036: LP-Notes

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9036  
**Aliases:** LP-Notes  
**Platforms:** Windows  

## Description
[LP-Notes](https://attack.mitre.org/software/S9036) is a C/C++ Windows credential stealer used by [MuddyWater](https://attack.mitre.org/groups/G0069). [LP-Notes](https://attack.mitre.org/software/S9036) was named after the `lp-notes.txt` file that is used to store stolen credentials.(Citation: ESET_MuddyWater_Dec2025)

## Techniques Used
- T1027.007: Dynamic API Resolution
- T1027.013: Encrypted/Encoded File
- T1056.002: GUI Input Capture
- T1057: Process Discovery
- T1059.001: PowerShell
- T1074.001: Local Data Staging
- T1078: Valid Accounts
- T1106: Native API
- T1134.001: Token Impersonation/Theft
- T1140: Deobfuscate/Decode Files or Information
- T1560: Archive Collected Data
