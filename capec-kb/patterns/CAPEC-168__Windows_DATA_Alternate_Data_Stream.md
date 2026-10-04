# CAPEC-168: Windows ::DATA Alternate Data Stream

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/168.html  

## Description
An attacker exploits the functionality of Microsoft NTFS Alternate Data Streams (ADS) to undermine system security. ADS allows multiple "files" to be stored in one directory entry referenced as filename:streamname. One or more alternate data streams may be stored in any file or directory. Normal Microsoft utilities do not show the presence of an ADS stream attached to a file. The additional space for the ADS is not recorded in the displayed file size. The additional space for ADS is accounted for in the used space on the volume. An ADS can be any type of file. ADS are copied by standard Microsoft utilities between NTFS volumes. ADS can be used by an attacker or intruder to hide tools, scripts, and data from detection by normal system utilities. Many anti-virus programs do not check for or scan ADS. Windows Vista does have a switch (-R) on the command line DIR command that will display alternate streams.

## Related Attack Patterns
- ChildOf: CAPEC-636

## Prerequisites
- The target must be running the Microsoft NTFS file system.

## Resources Required
- The attacker must have command line or programmatic access to the target's files system with write/read permissions.

## Mitigations
- Design: Use FAT file systems which do not support Alternate Data Streams.
- Implementation: Use Vista dir with the -R switch or utility to find Alternate Data Streams and take appropriate action with those discovered.
- Implementation: Use products that are Alternate Data Stream aware for virus scanning and system security operations.

## Related Weaknesses (CWE)
- CWE-212
- CWE-69
