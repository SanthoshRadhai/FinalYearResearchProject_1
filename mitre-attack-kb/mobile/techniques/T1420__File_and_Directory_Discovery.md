# T1420: File and Directory Discovery


**ATT&CK ID:** T1420  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Discovery  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1420  

## Description
Adversaries may enumerate files and directories or search in specific device locations for desired information within a filesystem. Adversaries may use the information from [File and Directory Discovery](https://attack.mitre.org/techniques/T1420) during automated discovery to shape follow-on behaviors, including deciding if the adversary should fully infect the target and/or attempt specific actions. 

On Android, Linux file permissions and SELinux policies typically stringently restrict what can be accessed by apps without taking advantage of a privilege escalation exploit. The contents of the external storage directory are generally visible, which could present concerns if sensitive data is inappropriately stored there. iOS's security architecture generally restricts the ability to perform any type of [File and Directory Discovery](https://attack.mitre.org/techniques/T1420) without use of escalated privileges.

## Mitigations
- M1006: Use Recent OS Version

## Known Threat Groups Using This Technique
- G0112: Windshift

## Known Software Using This Technique
- S1095: AhRat
- S0529: CarbonSteal
- S1225: CherryBlos
- S0505: Desert Scorpion
- S9005: DocSwap
- S0550: DoubleAgent
- S1092: Escobar
- S0577: FrozenCell
- S0535: Golden Cup
- S0551: GoldenEagle
- S1077: Hornbill
- S1241: RatMilad
- S9030: SameCoin
- S0549: SilkBean
- S0558: Tiktok Pro
- S1216: TriangleDB
- S9006: VajraSpy
