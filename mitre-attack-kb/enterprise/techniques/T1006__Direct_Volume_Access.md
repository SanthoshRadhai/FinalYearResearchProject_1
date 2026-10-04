# T1006: Direct Volume Access


**ATT&CK ID:** T1006  
**Domain:** Mitre Attack  
**Tactic(s):** Stealth  
**Platforms:** Network Devices, Windows  
**Reference:** https://attack.mitre.org/techniques/T1006  

## Description
Adversaries may directly access a volume to bypass file access controls and file system monitoring. Windows allows programs to have direct access to logical volumes. Programs with direct access may read and write files directly from the drive by analyzing file system data structures. This technique may bypass Windows file access controls as well as file system monitoring tools.(Citation: Hakobyan 2009)

Utilities, such as `NinjaCopy`, exist to perform these actions in PowerShell.(Citation: Github PowerSploit Ninjacopy) Adversaries may also use built-in or third-party utilities (such as `vssadmin`, `wbadmin`, and [esentutl](https://attack.mitre.org/software/S0404)) to create shadow copies or backups of data from system volumes.(Citation: LOLBAS Esentutl)

## Mitigations
- M1018: User Account Management
- M1040: Behavior Prevention on Endpoint

## Known Threat Groups Using This Technique
- G1015: Scattered Spider
- G1017: Volt Typhoon

## Known Software Using This Technique
- S0404: esentutl
