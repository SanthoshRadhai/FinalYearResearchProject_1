# T1074: Data Staged


**ATT&CK ID:** T1074  
**Domain:** Mitre Attack  
**Tactic(s):** Collection  
**Platforms:** ESXi, IaaS, Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1074  

## Description
Adversaries may stage collected data in a central location or directory prior to Exfiltration. Data may be kept in separate files or combined into one file through techniques such as [Archive Collected Data](https://attack.mitre.org/techniques/T1560). Interactive command shells may be used, and common functionality within [cmd](https://attack.mitre.org/software/S0106) and bash may be used to copy data into a staging location.(Citation: PWC Cloud Hopper April 2017)

In cloud environments, adversaries may stage data within a particular instance or virtual machine before exfiltration. An adversary may [Create Cloud Instance](https://attack.mitre.org/techniques/T1578/002) and stage data in that instance.(Citation: Mandiant M-Trends 2020)

Adversaries may choose to stage data from a victim network in a centralized location prior to Exfiltration to minimize the number of connections made to their C2 server and better evade detection.

## Sub-techniques
- T1074.001: Local Data Staging
- T1074.002: Remote Data Staging

## Known Threat Groups Using This Technique
- G1032: INC Ransom
- G1015: Scattered Spider
- G1055: VOID MANTICORE
- G1017: Volt Typhoon
- G0102: Wizard Spider

## Known Software Using This Technique
- S1020: Kevin
- S0641: Kobalos
- S1076: QUIETCANARY
- S1019: Shark
