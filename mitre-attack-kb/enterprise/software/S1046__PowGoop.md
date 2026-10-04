# S1046: PowGoop

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1046  
**Aliases:** PowGoop  
**Platforms:** Windows  

## Description
[PowGoop](https://attack.mitre.org/software/S1046) is a loader that consists of a DLL loader and a PowerShell-based downloader; it has been used by [MuddyWater](https://attack.mitre.org/groups/G0069) as their main loader.(Citation: DHS CISA AA22-055A MuddyWater February 2022)(Citation: CYBERCOM Iranian Intel Cyber January 2022)

## Techniques Used
- T1036: Masquerading
- T1036.005: Match Legitimate Resource Name or Location
- T1059.001: PowerShell
- T1071.001: Web Protocols
- T1132.002: Non-Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1573: Encrypted Channel
- T1574.001: DLL
