# S0599: Kinsing

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0599  
**Aliases:** Kinsing  
**Platforms:** Containers, Linux  

## Description
[Kinsing](https://attack.mitre.org/software/S0599) is Golang-based malware that runs a cryptocurrency miner and attempts to spread itself to other hosts in the victim environment. (Citation: Aqua Kinsing April 2020)(Citation: Sysdig Kinsing November 2020)(Citation: Aqua Security Cloud Native Threat Report June 2021)

## Techniques Used
- T1018: Remote System Discovery
- T1021.004: SSH
- T1053.003: Cron
- T1057: Process Discovery
- T1059.004: Unix Shell
- T1071.001: Web Protocols
- T1078: Valid Accounts
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1110: Brute Force
- T1133: External Remote Services
- T1222.002: Linux and Mac Permissions
- T1496.001: Compute Hijacking
- T1552.003: Shell History
- T1552.004: Private Keys
- T1609: Container Administration Command
- T1610: Deploy Container
