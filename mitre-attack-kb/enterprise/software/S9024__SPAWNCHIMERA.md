# S9024: SPAWNCHIMERA

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9024  
**Aliases:** SPAWNCHIMERA  
**Platforms:** Linux, Network Devices  

## Description
[SPAWNCHIMERA](https://attack.mitre.org/software/S9024) is a backdoor that supports command and control and can inject malicious components into native processes.(Citation: CISA SPAWNCHIMERA RESURGE February 2026)(Citation: Google UNC5221 BRICKSTORM SPAWNCHIMERA April 2024)(Citation: JPCERT SPAWNCHIMERA Ivanti February 2025)  [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) It incorporates capabilities from multiple tools within the SPAWN malware family, including SPAWNANT, SPAWNMOLE, and SPAWNSNAIL.(Citation: Google UNC5221 Ivanti January 2025)(Citation: Google UNC5221 BRICKSTORM SPAWNCHIMERA April 2024)(Citation: JPCERT SPAWNCHIMERA Ivanti February 2025)  [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) was first reported in April 2024.(Citation: Google UNC5221 BRICKSTORM SPAWNCHIMERA April 2024) [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has been observed in activity attributed to People's Republic of China (PRC) state-sponsored threat actors, including UNC5221..(Citation: Google UNC5221 Ivanti January 2025)(Citation: Google UNC5221 Ivanti April 2025)(Citation: Google UNC5221 BRICKSTORM SPAWNCHIMERA April 2024)(Citation: Picus Security UNC5221 Ivanti May 2025)

## Techniques Used
- T1005: Data from Local System
- T1027.013: Encrypted/Encoded File
- T1037: Boot or Logon Initialization Scripts
- T1040: Network Sniffing
- T1055.002: Portable Executable Injection
- T1057: Process Discovery
- T1059.006: Python
- T1070.004: File Deletion
- T1070.006: Timestomp
- T1082: System Information Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1480.002: Mutual Exclusion
- T1505.003: Web Shell
- T1518.001: Security Software Discovery
- T1553.002: Code Signing
- T1559: Inter-Process Communication
- T1571: Non-Standard Port
- T1572: Protocol Tunneling
- T1574: Hijack Execution Flow
- T1574.006: Dynamic Linker Hijacking
- T1678: Delay Execution
- T1685: Disable or Modify Tools
- T1690: Prevent Command History Logging
