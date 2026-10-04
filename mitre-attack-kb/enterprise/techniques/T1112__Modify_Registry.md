# T1112: Modify Registry


**ATT&CK ID:** T1112  
**Domain:** Mitre Attack  
**Tactic(s):** Defense Impairment, Persistence  
**Platforms:** Windows  
**Reference:** https://attack.mitre.org/techniques/T1112  

## Description
Adversaries may interact with the Windows Registry as part of a variety of other techniques to aid in defense evasion, persistence, and execution.

Access to specific areas of the Registry depends on account permissions, with some keys requiring administrator-level access. The built-in Windows command-line utility [Reg](https://attack.mitre.org/software/S0075) may be used for local or remote Registry modification.(Citation: Microsoft Reg) Other tools, such as remote access tools, may also contain functionality to interact with the Registry through the Windows API.

The Registry may be modified in order to hide configuration information or malicious payloads via [Obfuscated Files or Information](https://attack.mitre.org/techniques/T1027).(Citation: Unit42 BabyShark Feb 2019)(Citation: Avaddon Ransomware 2021)(Citation: Microsoft BlackCat Jun 2022)(Citation: CISA Russian Gov Critical Infra 2018) The Registry may also be modified to impair defenses, such as by enabling macros for all Microsoft Office products, allowing privilege escalation without alerting the user, increasing the maximum number of allowed outbound requests, and/or modifying systems to store plaintext credentials in memory.(Citation: CISA LockBit 2023)(Citation: Unit42 BabyShark Feb 2019)

The Registry of a remote system may be modified to aid in execution of files as part of lateral movement. It requires the remote Registry service to be running on the target system.(Citation: Microsoft Remote) Often [Valid Accounts](https://attack.mitre.org/techniques/T1078) are required, along with access to the remote system's [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) for RPC communication.

Finally, Registry modifications may also include actions to hide keys, such as prepending key names with a null character, which will cause an error and/or be ignored when read via [Reg](https://attack.mitre.org/software/S0075) or other utilities using the Win32 API.(Citation: Microsoft Reghide NOV 2006) Adversaries may abuse these pseudo-hidden keys to conceal payloads/commands used to maintain persistence.(Citation: TrendMicro POWELIKS AUG 2014)(Citation: SpectorOps Hiding Reg Jul 2017)

## Mitigations
- M1024: Restrict Registry Permissions

## Known Threat Groups Using This Technique
- G0073: APT19
- G0050: APT32
- G0082: APT38
- G0096: APT41
- G1044: APT42
- G0143: Aquatic Panda
- G1043: BlackByte
- G0108: Blue Mockingbird
- G0035: Dragonfly
- G1006: Earth Lusca
- G1003: Ember Bear
- G0061: FIN8
- G0047: Gamaredon Group
- G0078: Gorgon Group
- G0119: Indrik Spider
- G0094: Kimsuky
- G0030: Lotus Blossom
- G1014: LuminousMoth
- G0059: Magic Hound
- G1051: Medusa Group
- G0049: OilRig
- G0040: Patchwork
- G1031: Saint Bear
- G0091: Silence
- G0092: TA505
- G0027: Threat Group-3390
- G0010: Turla
- G1017: Volt Typhoon
- G0102: Wizard Spider

## Known Software Using This Technique
- S0677: AADInternals
- S0045: ADVSTORESHELL
- S0331: Agent Tesla
- S1025: Amadey
- S0438: Attor
- S0640: Avaddon
- S0031: BACKSPACE
- S0245: BADCALL
- S1226: BOOKWORM
- S0239: Bankshot
- S0268: Bisonal
- S0570: BitPaymer
- S1070: Black Basta
- S1181: BlackByte 2.0 Ransomware
- S1180: BlackByte Ransomware
- S1068: BlackCat
- S1149: CHIMNEYSWEEP
- S0023: CHOPSTICK
- S0527: CSPY Downloader
- S0348: Cardinal RAT
- S0261: Catchamas
- S0572: Caterpillar WebShell
- S0631: Chaes
- S0674: CharmPower
- S0660: Clambling
- S0611: Clop
- S0154: Cobalt Strike
- S0126: ComRAT
- S0608: Conficker
- S0488: CrackMapExec
- S0115: Crimson
- S1033: DCSrv
- S0334: DarkComet
- S1066: DarkTortilla
- S0673: DarkWatchman
- S0568: EVILNUM
- S1247: Embargo
- S0343: Exaramel for Windows
- S0569: Explosive
- S0267: FELIXROOT
- S0679: Ferocious
- S0666: Gelsemium
- S0531: Grandoreiro
- S0342: GreyEnergy
- S1230: HIUPAN
- S0376: HOPLIGHT
- S0697: HermeticWiper
- S9023: HiddenFace
- S0203: Hydraq
- S0537: HyperStack
- S1132: IPsec Helper
- S0260: InvisiMole
- S0271: KEYMARBLE
- S0669: KOCTOPUS
- S0356: KONNI
- S1190: Kapeka
- S0397: LoJax
- S1199: LockBit 2.0
- S1202: LockBit 3.0
- S0447: Lokibot
- S1060: Mafalda
- S0576: MegaCortex
- S0455: Metamorfo
- S1047: Mori
- S0256: Mosquito
- S9032: MuddyViper
- S0198: NETWIRE
- S9025: NOOPLDR
- S1131: NPPSPY
- S0205: Naid
- S0336: NanoCore
- S0691: Neoichor
- S0210: Nerex
- S0457: Netwalker
- S1090: NightClub
- S0229: Orz
- S0158: PHOREAL
- S0254: PLAINTEE
- S0664: Pandora
- S1050: PcShare
- S0517: Pillowmint
- S0501: PipeMon
- S0013: PlugX
- S0428: PoetRAT
- S0012: PoisonIvy
- S0518: PolyglotDuke
- S0441: PowerShower
- S1058: Prestige
- S0583: Pysa
- S0269: QUADAGENT
- S0650: QakBot
- S1242: Qilin
- S0262: QuasarRAT
- S0662: RCSession
- S0496: REvil
- S0240: ROKRAT
- S0148: RTM
- S0075: Reg
- S0511: RegDuke
- S0019: Regin
- S0332: Remcos
- S0090: Rover
- S0692: SILENTTRINITY
- S0533: SLOTHFULMEDIA
- S0649: SMOKEDHAM
- S0157: SOUNDBITE
- S0559: SUNBURST
- S1099: Samurai
- S0596: ShadowPad
- S0140: Shamoon
- S0444: ShimRat
- S1178: ShrinkLocker
- S0589: Sibot
- S0142: StreamEx
- S0603: Stuxnet
- S0242: SynAck
- S0663: SysUpdate
- S0560: TEARDROP
- S1201: TRANSLATEXT
- S0263: TYPEFRAME
- S0011: Taidoor
- S0467: TajMahal
- S1011: Tarrask
- S0665: ThreatNeedle
- S0668: TinyTurla
- S0266: TrickBot
- S0022: Uroburos
- S0386: Ursnif
- S0476: Valak
- S0180: Volgmer
- S0670: WarzoneRAT
- S0612: WastedLocker
- S0579: Waterbear
- S0330: Zeus Panda
- S0412: ZxShell
- S0032: gh0st RAT
- S1059: metaMain
- S0385: njRAT
- S0350: zwShell
