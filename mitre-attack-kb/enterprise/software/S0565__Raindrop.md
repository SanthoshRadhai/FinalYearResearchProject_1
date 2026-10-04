# S0565: Raindrop

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0565  
**Aliases:** Raindrop  
**Platforms:** Windows  

## Description
[Raindrop](https://attack.mitre.org/software/S0565) is a loader used by [APT29](https://attack.mitre.org/groups/G0016) that was discovered on some victim machines during investigations related to the [SolarWinds Compromise](https://attack.mitre.org/campaigns/C0024). It was discovered in January 2021 and was likely used since at least May 2020.(Citation: Symantec RAINDROP January 2021)(Citation: Microsoft Deep Dive Solorigate January 2021)

## Techniques Used
- T1027.002: Software Packing
- T1027.003: Steganography
- T1027.013: Encrypted/Encoded File
- T1036: Masquerading
- T1036.005: Match Legitimate Resource Name or Location
- T1140: Deobfuscate/Decode Files or Information
- T1497.003: Time Based Checks
