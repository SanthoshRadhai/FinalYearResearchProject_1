# S9002: Diskpart

**Type:** tool  
**Reference:** https://attack.mitre.org/software/S9002  
**Aliases:** Diskpart  
**Platforms:** Windows  

## Description
[Diskpart](https://attack.mitre.org/software/S9002) is a Windows command-line utility that is used to manage the computer’s drives, which includes disks, partitions, volumes and virtual hard disks.(Citation: Microsoft_diskpart_Feb2023)  

Adversaries may abuse [Diskpart](https://attack.mitre.org/software/S9002) to perform discovery and destructive actions on a system’s storage. For example, adversaries have been observed using [Diskpart](https://attack.mitre.org/software/S9002) to conduct [Discovery](https://attack.mitre.org/tactics/TA0007) techniques to enumerate disks and volumes to gather information about the host environment, and to execute commands such as `clean all` to remove partition information and overwrite data across disks, resulting in data destruction.(Citation: Trendmicro_RansomHub_Dec2024)

## Techniques Used
- T1059.003: Windows Command Shell
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1222.001: Windows Permissions
- T1561.002: Disk Structure Wipe
