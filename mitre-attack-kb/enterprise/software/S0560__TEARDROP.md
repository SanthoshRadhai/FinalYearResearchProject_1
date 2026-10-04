# S0560: TEARDROP

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0560  
**Aliases:** TEARDROP  
**Platforms:** Windows  

## Description
[TEARDROP](https://attack.mitre.org/software/S0560) is a memory-only dropper that was discovered on some victim machines during investigations related to the [SolarWinds Compromise](https://attack.mitre.org/campaigns/C0024). It was likely used by [APT29](https://attack.mitre.org/groups/G0016) since at least May 2020.(Citation: FireEye SUNBURST Backdoor December 2020)(Citation: Microsoft Deep Dive Solorigate January 2021)

## Techniques Used
- T1012: Query Registry
- T1027: Obfuscated Files or Information
- T1036.005: Match Legitimate Resource Name or Location
- T1112: Modify Registry
- T1140: Deobfuscate/Decode Files or Information
- T1543.003: Windows Service
