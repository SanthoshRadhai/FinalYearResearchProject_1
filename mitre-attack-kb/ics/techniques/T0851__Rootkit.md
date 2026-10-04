# T0851: Rootkit


**ATT&CK ID:** T0851  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Evasion, Inhibit Response Function  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0851  

## Description
Adversaries may deploy rootkits to hide the presence of programs, files, network connections, services, drivers, and other system components. Rootkits are programs that hide the existence of malware by intercepting and modifying operating-system API calls that supply system information. Rootkits or rootkit-enabling functionality may reside at the user or kernel level in the operating system, or lower. (Citation: Enterprise ATT&CK January 2018)   

Firmware rootkits that affect the operating system yield nearly full control of the system. While firmware rootkits are normally developed for the main processing board, they can also be developed for the I/O that is attached to an asset. Compromise of this firmware allows the modification of all of the process variables and functions the module engages in. This may result in commands being disregarded and false information being fed to the main device. By tampering with device processes, an adversary may inhibit its expected response functions and possibly enable [Impact](https://attack.mitre.org/tactics/TA0105).

## Mitigations
- M0945: Code Signing
- M0947: Audit

## Known Software Using This Technique
- S0603: Stuxnet
