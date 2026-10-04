# S1011: Tarrask

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1011  
**Aliases:** Tarrask  
**Platforms:** Windows  

## Description
[Tarrask](https://attack.mitre.org/software/S1011) is malware that has been used by [HAFNIUM](https://attack.mitre.org/groups/G0125) since at least August 2021. [Tarrask](https://attack.mitre.org/software/S1011) was designed to evade digital defenses and maintain persistence by generating concealed scheduled tasks.(Citation: Tarrask scheduled task)

## Techniques Used
- T1036.004: Masquerade Task or Service
- T1036.005: Match Legitimate Resource Name or Location
- T1053.005: Scheduled Task
- T1059.003: Windows Command Shell
- T1112: Modify Registry
- T1134.001: Token Impersonation/Theft
- T1564: Hide Artifacts
