# S0364: RawDisk

**Type:** tool  
**Reference:** https://attack.mitre.org/software/S0364  
**Aliases:** RawDisk  
**Platforms:** Windows  

## Description
[RawDisk](https://attack.mitre.org/software/S0364) is a legitimate commercial driver from the EldoS Corporation that is used for interacting with files, disks, and partitions. The driver allows for direct modification of data on a local computer's hard drive. In some cases, the tool can enact these raw disk modifications from user-mode processes, circumventing Windows operating system security features.(Citation: EldoS RawDisk ITpro)(Citation: Novetta Blockbuster Destructive Malware)

## Techniques Used
- T1485: Data Destruction
- T1561.001: Disk Content Wipe
- T1561.002: Disk Structure Wipe
