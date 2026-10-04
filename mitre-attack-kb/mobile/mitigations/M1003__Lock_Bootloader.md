# M1003: Lock Bootloader

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1003  

## Description
On devices that provide the capability to unlock the bootloader (hence allowing any operating system code to be flashed onto the device), perform periodic checks to ensure that the bootloader is locked.

## Techniques Mitigated
- T1398: Boot or Logon Initialization Scripts
- T1458: Replication Through Removable Media
- T1645: Compromise Client Software Binary
