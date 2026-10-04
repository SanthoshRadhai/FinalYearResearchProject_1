# S1234: SplatCloak

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1234  
**Aliases:** SplatCloak  
**Platforms:** Windows  

## Description
[SplatCloak](https://attack.mitre.org/software/S1234) is a malware that disables EDR-related routines used by Windows Defender and Kaspersky to aid in evading detection.  [SplatCloak](https://attack.mitre.org/software/S1234) has been deployed by [SplatDropper](https://attack.mitre.org/software/S1232) and is known to be leveraged by [Mustang Panda](https://attack.mitre.org/groups/G0129) since 2025.(Citation: Zscaler PAKLOG CorkLog SplatCloak Splatdropper April 2025)

## Techniques Used
- T1036.001: Invalid Code Signature
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1106: Native API
- T1518.001: Security Software Discovery
- T1685: Disable or Modify Tools
