# T1518: Software Discovery


**ATT&CK ID:** T1518  
**Domain:** Mitre Attack  
**Tactic(s):** Discovery  
**Platforms:** ESXi, IaaS, Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1518  

## Description
Adversaries may attempt to get a listing of software and software versions that are installed on a system or in a cloud environment. Adversaries may use the information from [Software Discovery](https://attack.mitre.org/techniques/T1518) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Such software may be deployed widely across the environment for configuration management or security reasons, such as [Software Deployment Tools](https://attack.mitre.org/techniques/T1072), and may allow adversaries broad access to infect devices or move laterally.

Adversaries may attempt to enumerate software for a variety of reasons, such as figuring out what security measures are present or if the compromised system has a version of software that is vulnerable to [Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068).

## Sub-techniques
- T1518.001: Security Software Discovery
- T1518.002: Backup Software Discovery

## Known Threat Groups Using This Technique
- G0060: BRONZE BUTLER
- G1001: HEXANE
- G0100: Inception
- G0069: MuddyWater
- G0129: Mustang Panda
- G1008: SideCopy
- G0121: Sidewinder
- G0081: Tropic Trooper
- G1017: Volt Typhoon
- G0124: Windigo
- G0112: Windshift

## Known Software Using This Technique
- S0534: Bazar
- S0482: Bundlore
- S0674: CharmPower
- S0154: Cobalt Strike
- S0126: ComRAT
- S1153: Cuckoo Stealer
- S0384: Dridex
- S0062: DustySky
- S0024: Dyre
- S9010: GlassWorm
- S0431: HotCroissant
- S0260: InvisiMole
- S1245: InvisibleFerret
- S9029: IronWind
- S0526: KGH_SPY
- S1185: LightSpy
- S1141: LunarWeb
- S0652: MarkiRAT
- S0455: Metamorfo
- S0229: Orz
- S0598: P.A.S. Webshell
- S1228: PUBLOAD
- S0650: QakBot
- S0148: RTM
- S1148: Raccoon Stealer
- S1240: RedLine Stealer
- S1042: SUGARDUMP
- S1064: SVCReady
- S1099: Samurai
- S0445: ShimRatReporter
- S0623: Siloscape
- S1124: SocGholish
- S0646: SpicyOmelette
- S1183: StrelaStealer
- S0467: TajMahal
- S9041: TeamPCP Cloud Stealer
- S1065: Woody RAT
- S0658: XCSSET
- S0472: down_new
