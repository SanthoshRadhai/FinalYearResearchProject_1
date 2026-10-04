# S1048: macOS.OSAMiner

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1048  
**Aliases:** macOS.OSAMiner  
**Platforms:** macOS  

## Description
[macOS.OSAMiner](https://attack.mitre.org/software/S1048) is a Monero mining trojan that was first observed in 2018; security researchers assessed [macOS.OSAMiner](https://attack.mitre.org/software/S1048) may have been circulating since at least 2015. [macOS.OSAMiner](https://attack.mitre.org/software/S1048) is known for embedding one run-only AppleScript into another, which helped the malware evade full analysis for five years due to a lack of Apple event (AEVT) analysis tools.(Citation: SentinelLabs reversing run-only applescripts 2021)(Citation: VMRay OSAMiner dynamic analysis 2021)

## Techniques Used
- T1027.008: Stripped Payloads
- T1027.009: Embedded Payloads
- T1057: Process Discovery
- T1059.002: AppleScript
- T1082: System Information Discovery
- T1105: Ingress Tool Transfer
- T1497.001: System Checks
- T1543.001: Launch Agent
- T1569.001: Launchctl
- T1680: Local Storage Discovery
- T1685: Disable or Modify Tools
