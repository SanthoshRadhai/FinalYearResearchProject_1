# S0607: KillDisk

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0607  
**Aliases:** KillDisk, Win32/KillDisk.NBI, Win32/KillDisk.NBH, Win32/KillDisk.NBD, Win32/KillDisk.NBC, Win32/KillDisk.NBB  
**Platforms:** Linux, Windows  

## Description
[KillDisk](https://attack.mitre.org/software/S0607) is a disk-wiping tool designed to overwrite files with random data to render the OS unbootable. It was first observed as a component of [BlackEnergy](https://attack.mitre.org/software/S0089) malware during cyber attacks against Ukraine in 2015. [KillDisk](https://attack.mitre.org/software/S0607) has since evolved into stand-alone malware used by a variety of threat actors against additional targets in Europe and Latin America; in 2016 a ransomware component was also incorporated into some [KillDisk](https://attack.mitre.org/software/S0607) variants.(Citation: KillDisk Ransomware)(Citation: ESEST Black Energy Jan 2016)(Citation: Trend Micro KillDisk 1)(Citation: Trend Micro KillDisk 2)

## Techniques Used
- T1027: Obfuscated Files or Information
- T1036.004: Masquerade Task or Service
- T1057: Process Discovery
- T1070.004: File Deletion
- T1083: File and Directory Discovery
- T1106: Native API
- T1129: Shared Modules
- T1134: Access Token Manipulation
- T1485: Data Destruction
- T1486: Data Encrypted for Impact
- T1489: Service Stop
- T1529: System Shutdown/Reboot
- T1561.002: Disk Structure Wipe
- T1680: Local Storage Discovery
- T1685.005: Clear Windows Event Logs
