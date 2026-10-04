# T1614: System Location Discovery


**ATT&CK ID:** T1614  
**Domain:** Mitre Attack  
**Tactic(s):** Discovery  
**Platforms:** IaaS, Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1614  

## Description
Adversaries may gather information in an attempt to calculate the geographical location of a victim host. Adversaries may use the information from [System Location Discovery](https://attack.mitre.org/techniques/T1614) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Adversaries may attempt to infer the location of a system using various system checks, such as time zone, keyboard layout, and/or language settings.(Citation: FBI Ragnar Locker 2020)(Citation: Sophos Geolocation 2016)(Citation: Bleepingcomputer RAT malware 2020) Windows API functions such as <code>GetLocaleInfoW</code> can also be used to determine the locale of the host.(Citation: FBI Ragnar Locker 2020) In cloud environments, an instance's availability zone may also be discovered by accessing the instance metadata service from the instance.(Citation: AWS Instance Identity Documents)(Citation: Microsoft Azure Instance Metadata 2021)

Adversaries may also attempt to infer the location of a victim host using IP addressing, such as via online geolocation IP-lookup services.(Citation: Securelist Trasparent Tribe 2020)(Citation: Sophos Geolocation 2016)

## Sub-techniques
- T1614.001: System Language Discovery

## Known Threat Groups Using This Technique
- G1008: SideCopy
- G1017: Volt Typhoon

## Known Software Using This Technique
- S1025: Amadey
- S9031: AshTag
- S0115: Crimson
- S1153: Cuckoo Stealer
- S1111: DarkGate
- S0673: DarkWatchman
- S9010: GlassWorm
- S1138: Gootloader
- S0632: GrimAgent
- S1249: HexEval Loader
- S1245: InvisibleFerret
- S9043: Mini Shai-Hulud
- S0013: PlugX
- S9019: PureCrypter
- S0262: QuasarRAT
- S1148: Raccoon Stealer
- S0481: Ragnar Locker
- S1240: RedLine Stealer
- S0332: Remcos
- S0461: SDBbot
- S1018: Saint Bot
- S9030: SameCoin
- S1124: SocGholish
- S9034: Tsundere Botnet
- S1248: XORIndex Loader
