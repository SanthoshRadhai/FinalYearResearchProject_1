# S0368: NotPetya

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0368  
**Aliases:** NotPetya, ExPetr, Diskcoder.C, GoldenEye, Petrwrap, Nyetya  
**Platforms:** Windows  

## Description
[NotPetya](https://attack.mitre.org/software/S0368) is malware that was used by [Sandworm Team](https://attack.mitre.org/groups/G0034) in a worldwide attack starting on June 27, 2017. While [NotPetya](https://attack.mitre.org/software/S0368) appears as a form of ransomware, its main purpose was to destroy data and disk structures on compromised systems; the attackers never intended to make the encrypted data recoverable. As such, [NotPetya](https://attack.mitre.org/software/S0368) may be more appropriately thought of as a form of wiper malware. [NotPetya](https://attack.mitre.org/software/S0368) contains worm-like features to spread itself across a computer network using the SMBv1 exploits EternalBlue and EternalRomance.(Citation: Talos Nyetya June 2017)(Citation: US-CERT NotPetya 2017)(Citation: ESET Telebots June 2017)(Citation: US District Court Indictment GRU Unit 74455 October 2020)

## Techniques Used
- T1003.001: LSASS Memory
- T1021.002: SMB/Windows Admin Shares
- T1036: Masquerading
- T1047: Windows Management Instrumentation
- T1053.005: Scheduled Task
- T1078.003: Local Accounts
- T1083: File and Directory Discovery
- T1210: Exploitation of Remote Services
- T1218.011: Rundll32
- T1486: Data Encrypted for Impact
- T1518.001: Security Software Discovery
- T1529: System Shutdown/Reboot
- T1569.002: Service Execution
- T1685.005: Clear Windows Event Logs
