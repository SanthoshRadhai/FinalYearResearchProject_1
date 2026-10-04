# S0056: Net Crawler

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0056  
**Aliases:** Net Crawler, NetC  
**Platforms:** Windows  

## Description
[Net Crawler](https://attack.mitre.org/software/S0056) is an intranet worm capable of extracting credentials using credential dumpers and spreading to systems on a network over SMB by brute forcing accounts with recovered passwords and using [PsExec](https://attack.mitre.org/software/S0029) to execute a copy of [Net Crawler](https://attack.mitre.org/software/S0056). (Citation: Cylance Cleaver)

## Techniques Used
- T1003.001: LSASS Memory
- T1021.002: SMB/Windows Admin Shares
- T1110.002: Password Cracking
- T1569.002: Service Execution
