# T1047: Windows Management Instrumentation


**ATT&CK ID:** T1047  
**Domain:** Mitre Attack  
**Tactic(s):** Execution  
**Platforms:** Windows  
**Reference:** https://attack.mitre.org/techniques/T1047  

## Description
Adversaries may abuse Windows Management Instrumentation (WMI) to execute malicious commands and payloads. WMI is designed for programmers and is the infrastructure for management data and operations on Windows systems.(Citation: WMI 1-3) WMI is an administration feature that provides a uniform environment to access Windows system components.

The WMI service enables both local and remote access, though the latter is facilitated by [Remote Services](https://attack.mitre.org/techniques/T1021) such as [Distributed Component Object Model](https://attack.mitre.org/techniques/T1021/003) and [Windows Remote Management](https://attack.mitre.org/techniques/T1021/006).(Citation: WMI 1-3) Remote WMI over DCOM operates using port 135, whereas WMI over WinRM operates over port 5985 when using HTTP and 5986 for HTTPS.(Citation: WMI 1-3) (Citation: Mandiant WMI)

An adversary can use WMI to interact with local and remote systems and use it as a means to execute various behaviors, such as gathering information for [Discovery](https://attack.mitre.org/tactics/TA0007) as well as [Execution](https://attack.mitre.org/tactics/TA0002) of commands and payloads.(Citation: Mandiant WMI) For example, `wmic.exe` can be abused by an adversary to delete shadow copies with the command `wmic.exe Shadowcopy Delete` (i.e., [Inhibit System Recovery](https://attack.mitre.org/techniques/T1490)).(Citation: WMI 6)

**Note:** `wmic.exe` is deprecated as of January of 2024, with the WMIC feature being “disabled by default” on Windows 11+. WMIC will be removed from subsequent Windows releases and replaced by [PowerShell](https://attack.mitre.org/techniques/T1059/001) as the primary WMI interface.(Citation: WMI 7,8) In addition to PowerShell and tools like `wbemtool.exe`, COM APIs can also be used to programmatically interact with WMI via C++, .NET, VBScript, etc.(Citation: WMI 7,8)

## Mitigations
- M1018: User Account Management
- M1026: Privileged Account Management
- M1038: Execution Prevention
- M1040: Behavior Prevention on Endpoint

## Known Threat Groups Using This Technique
- G0099: APT-C-36
- G0016: APT29
- G0050: APT32
- G0096: APT41
- G1044: APT42
- G0143: Aquatic Panda
- G1043: BlackByte
- G0108: Blue Mockingbird
- G0114: Chimera
- G1021: Cinnamon Tempest
- G0009: Deep Panda
- G1006: Earth Lusca
- G1003: Ember Bear
- G1016: FIN13
- G0037: FIN6
- G0046: FIN7
- G0061: FIN8
- G0093: GALLIUM
- G0047: Gamaredon Group
- G1032: INC Ransom
- G0119: Indrik Spider
- G0032: Lazarus Group
- G0065: Leviathan
- G0030: Lotus Blossom
- G0059: Magic Hound
- G1051: Medusa Group
- G1054: MirrorFace
- G0069: MuddyWater
- G0129: Mustang Panda
- G0019: Naikon
- G0049: OilRig
- G0034: Sandworm Team
- G0038: Stealth Falcon
- G1018: TA2541
- G0027: Threat Group-3390
- G1022: ToddyCat
- G1055: VOID MANTICORE
- G1047: Velvet Ant
- G1017: Volt Typhoon
- G0112: Windshift
- G0102: Wizard Spider
- G0045: menuPass

## Known Software Using This Technique
- S1028: Action RAT
- S0331: Agent Tesla
- S1129: Akira
- S9031: AshTag
- S0373: Astaroth
- S0640: Avaddon
- S1081: BADHATCH
- S0534: Bazar
- S1070: Black Basta
- S1068: BlackCat
- S0089: BlackEnergy
- S1063: Brute Ratel C4
- S1039: Bumblebee
- S0674: CharmPower
- S0154: Cobalt Strike
- S1155: Covenant
- S0488: CrackMapExec
- S0616: DEATHRANSOM
- S1111: DarkGate
- S1066: DarkTortilla
- S0673: DarkWatchman
- S0062: DustySky
- S0605: EKANS
- S0568: EVILNUM
- S0367: Emotet
- S0363: Empire
- S0396: EvilBunny
- S0267: FELIXROOT
- S0618: FIVEHANDS
- S0381: FlawedAmmyy
- S1044: FunnyDream
- S0237: GravityRAT
- S0151: HALFBAKED
- S0617: HELLOKITTY
- S0376: HOPLIGHT
- S0698: HermeticWizard
- S1152: IMAPLoader
- S1139: INC Ransomware
- S0483: IcedID
- S0357: Impacket
- S0156: KOMPROGO
- S0265: Kazuar
- S0250: Koadic
- S9035: LAMEHUG
- S9020: LODEINFO
- S1160: Latrodectus
- S1199: LockBit 2.0
- S0532: Lucifer
- S1141: LunarWeb
- S0449: Maze
- S0688: Meteor
- S0339: Micropsia
- S0553: MoleNet
- S0256: Mosquito
- S0457: Netwalker
- S0368: NotPetya
- S0340: Octopus
- S0365: Olympic Destroyer
- S0264: OopsIE
- S0223: POWERSTATS
- S0184: POWRUNER
- S1228: PUBLOAD
- S0378: PoshC2
- S0194: PowerSploit
- S0654: ProLock
- S1032: PyDCrypt
- S0650: QakBot
- S1242: Qilin
- S0241: RATANKBA
- S0496: REvil
- S9026: ROAMINGHOUSE
- S1130: Raspberry Robin
- S0375: Remexi
- S0270: RogueRobin
- S0692: SILENTTRINITY
- S0559: SUNBURST
- S1064: SVCReady
- S1085: Sardonic
- S0546: SharpStage
- S1178: ShrinkLocker
- S0589: Sibot
- S1086: Snip3
- S1124: SocGholish
- S0380: StoneDrill
- S0603: Stuxnet
- S0663: SysUpdate
- S1193: TAMECAT
- S1239: TONESHELL
- S0386: Ursnif
- S0476: Valak
- S0366: WannaCry
- S0251: Zebrocy
- S0283: jRAT
