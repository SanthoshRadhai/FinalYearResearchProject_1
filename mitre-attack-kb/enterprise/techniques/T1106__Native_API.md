# T1106: Native API


**ATT&CK ID:** T1106  
**Domain:** Mitre Attack  
**Tactic(s):** Execution  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1106  

## Description
Adversaries may interact with the native OS application programming interface (API) to execute behaviors. Native APIs provide a controlled means of calling low-level OS services within the kernel, such as those involving hardware/devices, memory, and processes.(Citation: NT API Windows)(Citation: Linux Kernel API) These native APIs are leveraged by the OS during system boot (when other system components are not yet initialized) as well as carrying out tasks and requests during routine operations.

Adversaries may abuse these OS API functions as a means of executing behaviors. Similar to [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059), the native API and its hierarchy of interfaces provide mechanisms to interact with and utilize various components of a victimized system.

Native API functions (such as <code>NtCreateProcess</code>) may be directed invoked via system calls / syscalls, but these features are also often exposed to user-mode applications via interfaces and libraries.(Citation: OutFlank System Calls)(Citation: CyberBit System Calls)(Citation: MDSec System Calls) For example, functions such as the Windows API <code>CreateProcess()</code> or GNU <code>fork()</code> will allow programs and scripts to start other processes.(Citation: Microsoft CreateProcess)(Citation: GNU Fork) This may allow API callers to execute a binary, run a CLI command, load modules, etc. as thousands of similar API functions exist for various system operations.(Citation: Microsoft Win32)(Citation: LIBC)(Citation: GLIBC)

Higher level software frameworks, such as Microsoft .NET and macOS Cocoa, are also available to interact with native APIs. These frameworks typically provide language wrappers/abstractions to API functionalities and are designed for ease-of-use/portability of code.(Citation: Microsoft NET)(Citation: Apple Core Services)(Citation: MACOS Cocoa)(Citation: macOS Foundation)

Adversaries may use assembly to directly or in-directly invoke syscalls in an attempt to subvert defensive sensors and detection signatures such as user mode API-hooks.(Citation: Redops Syscalls) Adversaries may also attempt to tamper with sensors and defensive tools associated with API monitoring, such as unhooking monitored functions via [Disable or Modify Tools](https://attack.mitre.org/techniques/T1685).

## Mitigations
- M1038: Execution Prevention
- M1040: Behavior Prevention on Endpoint

## Known Threat Groups Using This Technique
- G0067: APT37
- G0082: APT38
- G0098: BlackTech
- G0114: Chimera
- G0047: Gamaredon Group
- G0078: Gorgon Group
- G0126: Higaisa
- G0094: Kimsuky
- G0032: Lazarus Group
- G1051: Medusa Group
- G0129: Mustang Panda
- G0034: Sandworm Team
- G1008: SideCopy
- G0091: Silence
- G0092: TA505
- G1022: ToddyCat
- G0081: Tropic Trooper
- G0010: Turla
- G0090: WIRTE
- G0045: menuPass

## Known Software Using This Technique
- S0045: ADVSTORESHELL
- S9027: ANELLDR
- S1129: Akira
- S1025: Amadey
- S0622: AppleSeed
- S0456: Aria-body
- S1087: AsyncRAT
- S0438: Attor
- S0640: Avaddon
- S1053: AvosLocker
- S1081: BADHATCH
- S0128: BADNEWS
- S0470: BBK
- S1226: BOOKWORM
- S0638: Babuk
- S0475: BackConfig
- S0606: Bad Rabbit
- S0234: Bandook
- S0239: Bankshot
- S0534: Bazar
- S0574: BendyBear
- S0268: Bisonal
- S0570: BitPaymer
- S1070: Black Basta
- S1180: BlackByte Ransomware
- S0521: BloodHound
- S0651: BoxCaon
- S1063: Brute Ratel C4
- S1039: Bumblebee
- S1237: CANONSTAGER
- S1149: CHIMNEYSWEEP
- S1236: CLAIMLOADER
- S0693: CaddyWiper
- S9016: Caminho
- S0484: Carberp
- S0631: Chaes
- S0667: Chrommme
- S0611: Clop
- S0154: Cobalt Strike
- S0126: ComRAT
- S0575: Conti
- S0614: CostaBricks
- S0625: Cuba
- S0687: Cyclops Blink
- S1033: DCSrv
- S1052: DEADEYE
- S9021: DOWNIISSA
- S0694: DRATzarus
- S1111: DarkGate
- S1066: DarkTortilla
- S0354: Denis
- S0659: Diavol
- S0695: Donut
- S0384: Dridex
- S9038: DynoWiper
- S0554: Egregor
- S1247: Embargo
- S0367: Emotet
- S0363: Empire
- S0396: EvilBunny
- S1179: Exbyte
- S0569: Explosive
- S0512: FatDuke
- S0696: Flagpro
- S0661: FoggyWeb
- S9033: Fooder
- S1044: FunnyDream
- S0666: Gelsemium
- S0493: GoldenSpy
- S0477: Goopy
- S0531: Grandoreiro
- S0632: GrimAgent
- S0561: GuLoader
- S0391: HAWKBALL
- S9007: HTTPTroy
- S0499: Hancitor
- S1229: Havoc
- S9018: HeartCrypt
- S0697: HermeticWiper
- S0698: HermeticWizard
- S0431: HotCroissant
- S0398: HyperBro
- S0537: HyperStack
- S1152: IMAPLoader
- S1139: INC Ransomware
- S0483: IcedID
- S0434: Imminent Monitor
- S0259: InnaputRAT
- S0260: InvisiMole
- S0669: KOCTOPUS
- S0356: KONNI
- S1190: Kapeka
- S1020: Kevin
- S0607: KillDisk
- S9020: LODEINFO
- S9036: LP-Notes
- S1160: Latrodectus
- S0395: LightNeuron
- S0680: LitePower
- S0681: Lizar
- S1202: LockBit 3.0
- S0447: Lokibot
- S1016: MacMa
- S1060: Mafalda
- S1169: Mango
- S0652: MarkiRAT
- S0449: Maze
- S1244: Medusa Ransomware
- S0576: MegaCortex
- S0455: Metamorfo
- S0688: Meteor
- S1015: Milan
- S0084: Mis-Type
- S0083: Misdat
- S1122: Mispadu
- S0256: Mosquito
- S9032: MuddyViper
- S0198: NETWIRE
- S9025: NOOPLDR
- S0630: Nebulae
- S0457: Netwalker
- S1090: NightClub
- S1100: Ninja
- S1170: ODAgent
- S1172: OilBooster
- S1233: PAKLOG
- S0435: PLEAD
- S1228: PUBLOAD
- S1050: PcShare
- S1145: Pikabot
- S0517: Pillowmint
- S0501: PipeMon
- S0013: PlugX
- S0518: PolyglotDuke
- S0453: Pony
- S1058: Prestige
- S0147: Pteranodon
- S1076: QUIETCANARY
- S0650: QakBot
- S1242: Qilin
- S0662: RCSession
- S0416: RDFSNIFFER
- S0496: REvil
- S0240: ROKRAT
- S0148: RTM
- S0629: RainyDay
- S0458: Ramsay
- S0448: Rising Sun
- S1078: RotaJakiro
- S1073: Royal
- S9037: RustyWater
- S0446: Ryuk
- S0085: S-Type
- S0692: SILENTTRINITY
- S0562: SUNSPOT
- S1064: SVCReady
- S1210: Sagerunex
- S1018: Saint Bot
- S1099: Samurai
- S1085: Sardonic
- S1089: SharpDisco
- S0444: ShimRat
- S0445: ShimRatReporter
- S0610: SideTwist
- S0623: Siloscape
- S0627: SodaMaster
- S0615: SombRAT
- S1234: SplatCloak
- S1232: SplatDropper
- S1227: StarProxy
- S1200: StealBit
- S1034: StrifeWater
- S0603: Stuxnet
- S0242: SynAck
- S0663: SysUpdate
- S9001: SystemBC
- S1239: TONESHELL
- S9012: TRAILBLAZE
- S0011: Taidoor
- S0595: ThiefQuest
- S0668: TinyTurla
- S0678: Torisma
- S0266: TrickBot
- S0022: Uroburos
- S0386: Ursnif
- S0180: Volgmer
- S0670: WarzoneRAT
- S0612: WastedLocker
- S0579: Waterbear
- S0689: WhisperGate
- S0466: WindTail
- S0141: Winnti for Windows
- S1065: Woody RAT
- S0161: XAgentOSX
- S1207: XLoader
- S1151: ZeroCleare
- S0412: ZxShell
- S1013: ZxxZ
- S0471: build_downer
- S0032: gh0st RAT
- S1059: metaMain
- S0385: njRAT
- S0653: xCaon
