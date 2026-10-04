# S1131: NPPSPY

**Type:** tool  
**Reference:** https://attack.mitre.org/software/S1131  
**Aliases:** NPPSPY  
**Platforms:** Windows  

## Description
NPPSPY is an implementation of a theoretical mechanism first presented in 2004 for capturing credentials submitted to a Windows system via a rogue Network Provider API item. NPPSPY captures credentials following submission and writes them to a file on the victim system for follow-on exfiltration.(Citation: Huntress NPPSPY 2022)(Citation: Polak NPPSPY 2004)

## Techniques Used
- T1005: Data from Local System
- T1056: Input Capture
- T1112: Modify Registry
- T1119: Automated Collection
- T1552: Unsecured Credentials
- T1557: Adversary-in-the-Middle
- T1684.001: Impersonation
