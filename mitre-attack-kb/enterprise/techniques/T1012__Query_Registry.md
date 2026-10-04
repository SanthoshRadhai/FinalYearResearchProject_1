# T1012: Query Registry


**ATT&CK ID:** T1012  
**Domain:** Mitre Attack  
**Tactic(s):** Discovery  
**Platforms:** Windows  
**Reference:** https://attack.mitre.org/techniques/T1012  

## Description
Adversaries may interact with the Windows Registry to gather information about the system, configuration, and installed software.

The Registry contains a significant amount of information about the operating system, configuration, software, and security.(Citation: Wikipedia Windows Registry) Information can easily be queried using the [Reg](https://attack.mitre.org/software/S0075) utility, though other means to access the Registry exist. Some of the information may help adversaries to further their operation within a network. Adversaries may use the information from [Query Registry](https://attack.mitre.org/techniques/T1012) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

## Known Threat Groups Using This Technique
- G0050: APT32
- G0087: APT39
- G0096: APT41
- G1043: BlackByte
- G0114: Chimera
- G1034: Daggerfly
- G0035: Dragonfly
- G0117: Fox Kitten
- G0047: Gamaredon Group
- G0119: Indrik Spider
- G0094: Kimsuky
- G0032: Lazarus Group
- G0030: Lotus Blossom
- G0049: OilRig
- G0038: Stealth Falcon
- G0027: Threat Group-3390
- G0010: Turla
- G1017: Volt Typhoon
- G0128: ZIRCONIUM

## Known Software Using This Technique
- S0045: ADVSTORESHELL
- S0438: Attor
- S0344: Azorult
- S0031: BACKSPACE
- S0414: BabyShark
- S0239: Bankshot
- S0534: Bazar
- S0574: BendyBear
- S0268: Bisonal
- S0570: BitPaymer
- S1180: BlackByte Ransomware
- S0252: Brave Prince
- S1039: Bumblebee
- S0023: CHOPSTICK
- S0030: Carbanak
- S0484: Carberp
- S0335: Carbon
- S0348: Cardinal RAT
- S0674: CharmPower
- S0660: Clambling
- S0154: Cobalt Strike
- S0126: ComRAT
- S0115: Crimson
- S1159: DUSTTRAP
- S0673: DarkWatchman
- S0354: Denis
- S0021: Derusbi
- S0186: DownPaper
- S0567: Dtrack
- S0091: Epic
- S0267: FELIXROOT
- S0512: FatDuke
- S0182: FinFisher
- S1044: FunnyDream
- S0666: Gelsemium
- S0249: Gold Dragon
- S0376: HOPLIGHT
- S0203: Hydraq
- S0604: Industroyer
- S0260: InvisiMole
- S0201: JPIN
- S1190: Kapeka
- S0513: LiteDuke
- S0680: LitePower
- S0532: Lucifer
- S1060: Mafalda
- S1015: Milan
- S1047: Mori
- S0165: OSInfo
- S0145: POWERSOURCE
- S0184: POWRUNER
- S1228: PUBLOAD
- S1050: PcShare
- S0517: Pillowmint
- S0013: PlugX
- S0194: PowerSploit
- S0238: Proxysvc
- S0269: QUADAGENT
- S1076: QUIETCANARY
- S1242: Qilin
- S0241: RATANKBA
- S0496: REvil
- S0240: ROKRAT
- S1148: Raccoon Stealer
- S0172: Reaver
- S1240: RedLine Stealer
- S0075: Reg
- S0332: Remcos
- S0448: Rising Sun
- S0692: SILENTTRINITY
- S0559: SUNBURST
- S1064: SVCReady
- S1018: Saint Bot
- S1099: Samurai
- S0140: Shamoon
- S1019: Shark
- S0589: Sibot
- S0627: SodaMaster
- S0380: StoneDrill
- S0603: Stuxnet
- S0242: SynAck
- S0560: TEARDROP
- S1201: TRANSLATEXT
- S0011: Taidoor
- S0668: TinyTurla
- S0022: Uroburos
- S0386: Ursnif
- S0476: Valak
- S0180: Volgmer
- S0155: WINDSHIELD
- S0612: WastedLocker
- S0579: Waterbear
- S1065: Woody RAT
- S0251: Zebrocy
- S0330: Zeus Panda
- S0412: ZxShell
- S1013: ZxxZ
- S0032: gh0st RAT
- S0385: njRAT
