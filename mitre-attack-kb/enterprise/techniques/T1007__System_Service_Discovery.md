# T1007: System Service Discovery


**ATT&CK ID:** T1007  
**Domain:** Mitre Attack  
**Tactic(s):** Discovery  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1007  

## Description
Adversaries may try to gather information about registered local system services. Adversaries may obtain information about services using tools as well as OS utility commands such as <code>sc query</code>, <code>tasklist /svc</code>, <code>systemctl --type=service</code>, and <code>net start</code>. Adversaries may also gather information about schedule tasks via commands such as `schtasks` on Windows or `crontab -l` on Linux and macOS.(Citation: Elastic Security Labs GOSAR 2024)(Citation: SentinelLabs macOS Malware 2021)(Citation: Splunk Linux Gormir 2024)(Citation: Aquasec Kinsing 2020)

Adversaries may use the information from [System Service Discovery](https://attack.mitre.org/techniques/T1007) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

## Known Threat Groups Using This Technique
- G0006: APT1
- G0143: Aquatic Panda
- G0060: BRONZE BUTLER
- G0114: Chimera
- G1006: Earth Lusca
- G0119: Indrik Spider
- G0004: Ke3chang
- G0094: Kimsuky
- G1054: MirrorFace
- G0049: OilRig
- G0033: Poseidon Group
- G0139: TeamTNT
- G0010: Turla
- G1017: Volt Typhoon
- G0018: admin@338

## Known Software Using This Technique
- S0127: BBSRAT
- S0638: Babuk
- S0570: BitPaymer
- S1070: Black Basta
- S0572: Caterpillar WebShell
- S0154: Cobalt Strike
- S0244: Comnie
- S0625: Cuba
- S1066: DarkTortilla
- S0024: Dyre
- S0081: Elise
- S1247: Embargo
- S0082: Emissary
- S0091: Epic
- S0049: GeminiDuke
- S0237: GravityRAT
- S0342: GreyEnergy
- S1027: Heyoka Backdoor
- S0431: HotCroissant
- S0203: Hydraq
- S0398: HyperBro
- S0260: InvisiMole
- S0015: Ixeshe
- S0201: JPIN
- S0236: Kwampirs
- S9035: LAMEHUG
- S0582: LookBack
- S1244: Medusa Ransomware
- S0039: Net
- S1228: PUBLOAD
- S0378: PoshC2
- S1242: Qilin
- S0241: RATANKBA
- S0496: REvil
- S0629: RainyDay
- S0085: S-Type
- S0692: SILENTTRINITY
- S0533: SLOTHFULMEDIA
- S0559: SUNBURST
- S1085: Sardonic
- S0615: SombRAT
- S0018: Sykipot
- S0242: SynAck
- S0663: SysUpdate
- S0057: Tasklist
- S0266: TrickBot
- S0386: Ursnif
- S0180: Volgmer
- S0219: WINERACK
- S0086: ZLib
- S0412: ZxShell
- S0283: jRAT
