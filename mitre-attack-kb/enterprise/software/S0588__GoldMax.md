# S0588: GoldMax

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0588  
**Aliases:** GoldMax, SUNSHUTTLE  
**Platforms:** Windows, Linux  

## Description
[GoldMax](https://attack.mitre.org/software/S0588) is a second-stage C2 backdoor written in Go with Windows and Linux variants that are nearly identical in functionality. [GoldMax](https://attack.mitre.org/software/S0588) was discovered in early 2021 during the investigation into the [SolarWinds Compromise](https://attack.mitre.org/campaigns/C0024), and has likely been used by [APT29](https://attack.mitre.org/groups/G0016) since at least mid-2019. [GoldMax](https://attack.mitre.org/software/S0588) uses multiple defense evasion techniques, including avoiding virtualization execution and masking malicious traffic.(Citation: MSTIC NOBELIUM Mar 2021)(Citation: FireEye SUNSHUTTLE Mar 2021)(Citation: CrowdStrike StellarParticle January 2022)

## Techniques Used
- T1001.001: Junk Data
- T1016: System Network Configuration Discovery
- T1027.002: Software Packing
- T1027.013: Encrypted/Encoded File
- T1036.004: Masquerade Task or Service
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1053.003: Cron
- T1053.005: Scheduled Task
- T1059.003: Windows Command Shell
- T1071.001: Web Protocols
- T1105: Ingress Tool Transfer
- T1124: System Time Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1497.001: System Checks
- T1497.003: Time Based Checks
- T1564.011: Ignore Process Interrupts
- T1573.002: Asymmetric Cryptography
