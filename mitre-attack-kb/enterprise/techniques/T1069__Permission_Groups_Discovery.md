# T1069: Permission Groups Discovery


**ATT&CK ID:** T1069  
**Domain:** Mitre Attack  
**Tactic(s):** Discovery  
**Platforms:** Containers, IaaS, Identity Provider, Linux, macOS, Office Suite, SaaS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1069  

## Description
Adversaries may attempt to discover group and permission settings. This information can help adversaries determine which user accounts and groups are available, the membership of users in particular groups, and which users and groups have elevated permissions.

Adversaries may attempt to discover group permission settings in many different ways. This data may provide the adversary with information about the compromised environment that can be used in follow-on activity and targeting.(Citation: CrowdStrike BloodHound April 2018)

## Sub-techniques
- T1069.001: Local Groups
- T1069.002: Domain Groups
- T1069.003: Cloud Groups

## Known Threat Groups Using This Technique
- G0022: APT3
- G0096: APT41
- G1016: FIN13
- G1015: Scattered Spider
- G0092: TA505
- G1017: Volt Typhoon

## Known Software Using This Technique
- S0335: Carbon
- S0483: IcedID
- S0233: MURKYTOP
- S0445: ShimRatReporter
- S0623: Siloscape
- S0266: TrickBot
