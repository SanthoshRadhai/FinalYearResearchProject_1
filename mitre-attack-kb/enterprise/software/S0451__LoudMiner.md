# S0451: LoudMiner

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0451  
**Aliases:** LoudMiner  
**Platforms:** macOS, Windows  

## Description
[LoudMiner](https://attack.mitre.org/software/S0451) is a cryptocurrency miner which uses virtualization software to siphon system resources. The miner has been bundled with pirated copies of Virtual Studio Technology (VST) for Windows and macOS.(Citation: ESET LoudMiner June 2019)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1027.010: Command Obfuscation
- T1027.013: Encrypted/Encoded File
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1059.004: Unix Shell
- T1070.004: File Deletion
- T1082: System Information Discovery
- T1105: Ingress Tool Transfer
- T1189: Drive-by Compromise
- T1218.007: Msiexec
- T1496.001: Compute Hijacking
- T1543.003: Windows Service
- T1543.004: Launch Daemon
- T1564.001: Hidden Files and Directories
- T1564.006: Run Virtual Instance
- T1569.001: Launchctl
- T1569.002: Service Execution
