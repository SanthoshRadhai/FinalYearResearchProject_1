# M0947: Audit

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0947  

## Description
Perform audits or scans of systems, permissions, insecure software, insecure configurations, etc. to identify potential weaknesses. Perform periodic integrity checks of the device to validate the correctness of the firmware, software, programs, and configurations. Integrity checks, which typically include cryptographic hashes or digital signatures, should be compared to those obtained at known valid states, especially after events like device reboots, program downloads, or program restarts.

## Techniques Mitigated
- T0811: Data from Information Repositories
- T0821: Modify Controller Tasking
- T0830: Adversary-in-the-Middle
- T0836: Modify Parameter
- T0843: Program Download
- T0843.001: Download All
- T0843.002: Online Edit
- T0843.003: Program Append
- T0851: Rootkit
- T0859: Valid Accounts
- T0862: Supply Chain Compromise
- T0864: Transient Cyber Asset
- T0873: Project File Infection
- T0873.001: Siemens Project File Format
- T0874: Hooking
- T0889: Modify Program
- T1693: Modify Firmware
- T1693.001: System Firmware
- T1693.002: Module Firmware
