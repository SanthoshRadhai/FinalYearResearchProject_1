# S9015: BRICKSTORM

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9015  
**Aliases:** BRICKSTORM  
**Platforms:** ESXi, Linux, Network Devices, Windows  

## Description
[BRICKSTORM](https://attack.mitre.org/software/S9015) is a cross-platform backdoor with variants written in Go and Rust that facilitates command and control, the ingress transfer of other malware, and the exfiltration of data.(Citation: CISA BRICKSTORM UNC5221 AR25-338A February 2026)(Citation: Picus Security BRICKSTORM UNC5221 October 2025)(Citation: Resecurity UNC5221 BRICKSTORM F5 Big-IP October 2025)(Citation: Google BRICKSTORM September 2025) [BRICKSTORM](https://attack.mitre.org/software/S9015) has also been created from a .NET application using ahead-of-time (AOT) compilation to blend in within victim environments.(Citation: CISA BRICKSTORM UNC5221 AR25-338A February 2026)   [BRICKSTORM](https://attack.mitre.org/software/S9015) was first observed in April 2024.(Citation: Google UNC5221 BRICKSTORM SPAWNCHIMERA April 2024) [BRICKSTORM](https://attack.mitre.org/software/S9015) has previously been leveraged by People's Republic of China (PRC) state-nexus actors identified as UNC6201, UNC5221, WARP PANDA, PunyToad, and SYLVANITE.(Citation: Cloudflare 2026 Threat Report New Threat Actors March 2026)(Citation: CrowdStrike BRICKSTORM WARP PANDA UNC5221 December 2025)(Citation: CISA BRICKSTORM UNC5221 AR25-338A February 2026)(Citation: Dragos SYLVANITE MuddyWater Electrum March 2026)(Citation: NVISO BRICKSTORM April 2025)(Citation: Google BRICKSTORM GRIMBOLT UNC5221 UNC6201 February 2026)(Citation: Resecurity UNC5221 BRICKSTORM F5 Big-IP October 2025)(Citation: Google BRICKSTORM September 2025)

## Techniques Used
- T1005: Data from Local System
- T1027: Obfuscated Files or Information
- T1027.013: Encrypted/Encoded File
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1057: Process Discovery
- T1059.004: Unix Shell
- T1070.004: File Deletion
- T1070.010: Relocate Malware
- T1071.001: Web Protocols
- T1071.004: DNS
- T1083: File and Directory Discovery
- T1090.001: Internal Proxy
- T1102: Web Service
- T1105: Ingress Tool Transfer
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1489: Service Stop
- T1543: Create or Modify System Process
- T1568: Dynamic Resolution
- T1572: Protocol Tunneling
- T1573.002: Asymmetric Cryptography
- T1574.007: Path Interception by PATH Environment Variable
- T1678: Delay Execution
- T1690: Prevent Command History Logging
