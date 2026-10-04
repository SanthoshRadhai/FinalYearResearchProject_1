# S0698: HermeticWizard

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0698  
**Aliases:** HermeticWizard  
**Platforms:** Windows  

## Description
[HermeticWizard](https://attack.mitre.org/software/S0698) is a worm that has been used to spread [HermeticWiper](https://attack.mitre.org/software/S0697) in attacks against organizations in Ukraine since at least 2022.(Citation: ESET Hermetic Wizard March 2022)

## Techniques Used
- T1018: Remote System Discovery
- T1021.002: SMB/Windows Admin Shares
- T1027.013: Encrypted/Encoded File
- T1036.005: Match Legitimate Resource Name or Location
- T1046: Network Service Discovery
- T1047: Windows Management Instrumentation
- T1059.003: Windows Command Shell
- T1106: Native API
- T1110.001: Password Guessing
- T1218.010: Regsvr32
- T1218.011: Rundll32
- T1553.002: Code Signing
- T1559.001: Component Object Model
- T1569.002: Service Execution
- T1570: Lateral Tool Transfer
- T1685.005: Clear Windows Event Logs
