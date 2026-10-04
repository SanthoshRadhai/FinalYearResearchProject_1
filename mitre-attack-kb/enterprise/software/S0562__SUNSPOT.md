# S0562: SUNSPOT

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0562  
**Aliases:** SUNSPOT  
**Platforms:** Windows  

## Description
[SUNSPOT](https://attack.mitre.org/software/S0562) is an implant that injected the [SUNBURST](https://attack.mitre.org/software/S0559) backdoor into the SolarWinds Orion software update framework. It was used by [APT29](https://attack.mitre.org/groups/G0016) since at least February 2020.(Citation: CrowdStrike SUNSPOT Implant January 2021)

## Techniques Used
- T1027: Obfuscated Files or Information
- T1036.005: Match Legitimate Resource Name or Location
- T1057: Process Discovery
- T1070.004: File Deletion
- T1083: File and Directory Discovery
- T1106: Native API
- T1134: Access Token Manipulation
- T1140: Deobfuscate/Decode Files or Information
- T1195.002: Compromise Software Supply Chain
- T1480: Execution Guardrails
- T1480.002: Mutual Exclusion
- T1565.001: Stored Data Manipulation
