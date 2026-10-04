# S1206: JumbledPath

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1206  
**Aliases:** JumbledPath  
**Platforms:** Network Devices  

## Description
[JumbledPath](https://attack.mitre.org/software/S1206) is a custom-built utility written in GO that has been used by [Salt Typhoon](https://attack.mitre.org/groups/G1045) since at least 2024 for packet capture on remote Cisco devices. [JumbledPath](https://attack.mitre.org/software/S1206) is compiled as an ELF binary using x86-64 architecture which makes it potentially useable across Linux operating systems and network devices from multiple vendors.(Citation: Cisco Salt Typhoon FEB 2025)

## Techniques Used
- T1040: Network Sniffing
- T1104: Multi-Stage Channels
- T1560: Archive Collected Data
- T1665: Hide Infrastructure
- T1685: Disable or Modify Tools
- T1685.006: Clear Linux or Mac System Logs
