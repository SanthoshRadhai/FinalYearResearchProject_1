# S9034: Tsundere Botnet

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9034  
**Aliases:** Tsundere Botnet, DinDoor  
**Platforms:** Linux, macOS, Windows  

## Description
[Tsundere Botnet](https://attack.mitre.org/software/S9034) is a botnet first reported in mid-2025 that is delivered via MSI installer or a PowerShell script. It leverages Node.js and JavaScript for payload delivery and execution, and uses smart contracts on the blockchain to host command and control (C2) addresses. [Tsundere Botnet](https://attack.mitre.org/software/S9034) is attributed to a likely Russian-speaking threat actor.

A variant named DinDoor has been linked to [MuddyWater](https://attack.mitre.org/groups/G0069) operations and uses the Deno runtime for execution rather than Node.js.(Citation: Checkpoint_MOISCyberCrime_Mar2026)(Citation: SOCRadar_MuddyWaterDindoor_Mar2026)(Citation: CAL_MuddyWater_Mar2026)(Citation: SecureListUbiedo_Tsundere_Nov2025)

## Techniques Used
- T1027.010: Command Obfuscation
- T1027.013: Encrypted/Encoded File
- T1036.005: Match Legitimate Resource Name or Location
- T1059.001: PowerShell
- T1059.007: JavaScript
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1102.001: Dead Drop Resolver
- T1105: Ingress Tool Transfer
- T1140: Deobfuscate/Decode Files or Information
- T1195.001: Compromise Software Dependencies and Development Tools
- T1218.007: Msiexec
- T1480: Execution Guardrails
- T1547.001: Registry Run Keys / Startup Folder
- T1564.003: Hidden Window
- T1567.002: Exfiltration to Cloud Storage
- T1614: System Location Discovery
