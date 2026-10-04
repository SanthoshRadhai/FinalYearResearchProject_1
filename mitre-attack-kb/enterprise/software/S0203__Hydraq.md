# S0203: Hydraq

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0203  
**Aliases:** Hydraq, Roarur, MdmBot, HomeUnix, Homux, HidraQ, HydraQ, McRat, Aurora, 9002 RAT  
**Platforms:** Windows  

## Description
[Hydraq](https://attack.mitre.org/software/S0203) is a data-theft trojan first used by [Elderwood](https://attack.mitre.org/groups/G0066) in the 2009 Google intrusion known as Operation Aurora, though variations of this trojan have been used in more recent campaigns by other Chinese actors, possibly including [APT17](https://attack.mitre.org/groups/G0025).(Citation: MicroFocus 9002 Aug 2016)(Citation: Symantec Elderwood Sept 2012)(Citation: Symantec Trojan.Hydraq Jan 2010)(Citation: ASERT Seven Pointed Dagger Aug 2015)(Citation: FireEye DeputyDog 9002 November 2013)(Citation: ProofPoint GoT 9002 Aug 2017)(Citation: FireEye Sunshop Campaign May 2013)(Citation: PaloAlto 3102 Sept 2015)

## Techniques Used
- T1005: Data from Local System
- T1007: System Service Discovery
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1027: Obfuscated Files or Information
- T1048: Exfiltration Over Alternative Protocol
- T1057: Process Discovery
- T1070.004: File Deletion
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1112: Modify Registry
- T1113: Screen Capture
- T1129: Shared Modules
- T1134: Access Token Manipulation
- T1543.003: Windows Service
- T1569.002: Service Execution
- T1573.001: Symmetric Cryptography
- T1685.005: Clear Windows Event Logs
