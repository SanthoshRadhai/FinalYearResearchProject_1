# S0129: AutoIt backdoor

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0129  
**Aliases:** AutoIt backdoor  
**Platforms:** Windows  

## Description
[AutoIt backdoor](https://attack.mitre.org/software/S0129) is malware that has been used by the actors responsible for the MONSOON campaign. The actors frequently used it in weaponized .pps files exploiting CVE-2014-6352. (Citation: Forcepoint Monsoon) This malware makes use of the legitimate scripting language for Windows GUI automation with the same name.

## Techniques Used
- T1059.001: PowerShell
- T1083: File and Directory Discovery
- T1132.001: Standard Encoding
- T1548.002: Bypass User Account Control
