# T1678: Delay Execution


**ATT&CK ID:** T1678  
**Domain:** Mitre Attack  
**Tactic(s):** Stealth  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1678  

## Description
Adversaries may employ various time-based methods to evade detection and analysis. These techniques often exploit system clocks, delays, or timing mechanisms to obscure malicious activity, blend in with benign activity, and avoid scrutiny. Adversaries can perform this behavior within virtualization/sandbox environments or natively on host systems. 

Adversaries may utilize programmatic `sleep` commands or native system scheduling functionality, for example [Scheduled Task/Job](https://attack.mitre.org/techniques/T1053). Benign commands or other operations may also be used to delay malware execution or ensure prior commands have had time to execute properly. Loops or otherwise needless repetitions of commands, such as `ping`, may be used to delay malware execution and potentially exceed time thresholds of automated analysis environments.(Citation: Revil Independence Day)(Citation: Netskope Nitol) Another variation, commonly referred to as API hammering, involves making various calls to Native API functions in order to delay execution (while also potentially overloading analysis environments with junk data).(Citation: Joe Sec Nymaim)(Citation: Joe Sec Trickbot)

## Known Threat Groups Using This Technique
- G0094: Kimsuky
- G0129: Mustang Panda

## Known Software Using This Technique
- S9031: AshTag
- S9015: BRICKSTORM
- S9038: DynoWiper
- S9033: Fooder
- S9010: GlassWorm
- S1230: HIUPAN
- S9032: MuddyViper
- S9014: PHASEJAM
- S9019: PureCrypter
- S1242: Qilin
- S9037: RustyWater
- S9024: SPAWNCHIMERA
- S9008: Shai-Hulud
- S9001: SystemBC
- S1239: TONESHELL
- S9041: TeamPCP Cloud Stealer
- S0275: UPPERCUT
