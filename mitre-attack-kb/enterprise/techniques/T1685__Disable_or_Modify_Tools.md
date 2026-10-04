# T1685: Disable or Modify Tools


**ATT&CK ID:** T1685  
**Domain:** Mitre Attack  
**Tactic(s):** Defense Impairment  
**Platforms:** Containers, ESXi, IaaS, Linux, macOS, Network Devices, Windows  
**Reference:** https://attack.mitre.org/techniques/T1685  

## Description
Adversaries may disable, degrade, or tamper with security tools or applications (e.g., endpoint detection and response (EDR) tools, intrusion detection systems (IDS), antivirus, logging agents, sensors, etc.) to impair or reduce visibility of defensive capabilities. This may include stopping specific services, killing processes, modifying or deleting tool configuration files and Registry keys, or preventing tools from updating. This may also include impairing defenses more broadly by disrupting preventative, detection, and response mechanisms across host, network, and cloud environments.(Citation: SCADAfence_ransomware) 

In addition to directly targeting tools, adversaries may block or manipulate indicators and telemetry used for detection. This includes maliciously disabling or redirecting sensors such as Event Tracing for Windows (ETW), modifying event log configurations (e.g., redirecting Security logs), or interfering with logging pipelines and forwarding mechanisms (e.g., SIEM ingestion).(Citation: Microsoft Lamin Sept 2017)(Citation: ETW Palantir)

More advanced techniques include leveraging legitimate drivers or debugging mechanisms to render tools non-functional, bypassing anti-tampering protections, and targeting specific defenses such as Sysmon or cloud monitoring agents. Adversaries may also disrupt broader defensive operations, including update mechanisms, logging infrastructure (e.g., syslog), or event aggregation, further degrading an organization’s ability to detect and respond to malicious activity.(Citation: Cocomazzi FIN7 Reboot)

## Sub-techniques
- T1685.001: Disable or Modify Windows Event Log
- T1685.002: Disable or Modify Cloud Log
- T1685.003: Modify or Spoof Tool UI
- T1685.004: Disable or Modify Linux Audit System Log
- T1685.005: Clear Windows Event Logs
- T1685.006: Clear Linux or Mac System Logs

## Mitigations
- M1018: User Account Management
- M1022: Restrict File and Directory Permissions
- M1024: Restrict Registry Permissions
- M1038: Execution Prevention
- M1042: Disable or Remove Feature or Program
- M1047: Audit
- M1054: Software Configuration

## Known Threat Groups Using This Technique
- G0082: APT38
- G0096: APT41
- G1023: APT5
- G1030: Agrius
- G1024: Akira
- G0143: Aquatic Panda
- G0060: BRONZE BUTLER
- G1043: BlackByte
- G1052: Contagious Interview
- G0037: FIN6
- G0047: Gamaredon Group
- G0078: Gorgon Group
- G1032: INC Ransom
- G0119: Indrik Spider
- G0094: Kimsuky
- G0032: Lazarus Group
- G0059: Magic Hound
- G1051: Medusa Group
- G1054: MirrorFace
- G0069: MuddyWater
- G1040: Play
- G0024: Putter Panda
- G0106: Rocke
- G1031: Saint Bear
- G1015: Scattered Spider
- G1018: TA2541
- G0092: TA505
- G0139: TeamTNT
- G0010: Turla
- G1048: UNC3886
- G1047: Velvet Ant
- G0102: Wizard Spider

## Known Software Using This Technique
- S0331: Agent Tesla
- S0640: Avaddon
- S1184: BOLDMOVE
- S0638: Babuk
- S0534: Bazar
- S1180: BlackByte Ransomware
- S0252: Brave Prince
- S1063: Brute Ratel C4
- S0482: Bundlore
- S0484: Carberp
- S0144: ChChes
- S0611: Clop
- S0154: Cobalt Strike
- S0608: Conficker
- S9017: DCRAT
- S9013: DRYHOOK
- S0334: DarkComet
- S1111: DarkGate
- S0659: Diavol
- S0695: Donut
- S0605: EKANS
- S0377: Ebury
- S0554: Egregor
- S0249: Gold Dragon
- S0477: Goopy
- S0531: Grandoreiro
- S0132: H1N1
- S0061: HDoor
- S1097: HUI Loader
- S0697: HermeticWiper
- S0601: Hildegard
- S0434: Imminent Monitor
- S0201: JPIN
- S1206: JumbledPath
- S0669: KOCTOPUS
- S9039: LazyWiper
- S1199: LockBit 2.0
- S1202: LockBit 3.0
- S0372: LockerGoga
- S1213: Lumma Stealer
- S1169: Mango
- S0449: Maze
- S1244: Medusa Ransomware
- S0576: MegaCortex
- S0455: Metamorfo
- S0688: Meteor
- S1135: MultiLayer Wiper
- S0228: NanHaiShu
- S0336: NanoCore
- S0457: Netwalker
- S9014: PHASEJAM
- S0223: POWERSTATS
- S0279: Proton
- S9019: PureCrypter
- S0583: Pysa
- S0650: QakBot
- S1242: Qilin
- S0496: REvil
- S0481: Ragnar Locker
- S1130: Raspberry Robin
- S1240: RedLine Stealer
- S0400: RobbinHood
- S0253: RunningRAT
- S0446: Ryuk
- S0692: SILENTTRINITY
- S9024: SPAWNCHIMERA
- S0559: SUNBURST
- S9008: Shai-Hulud
- S1178: ShrinkLocker
- S0468: Skidmap
- S1234: SplatCloak
- S0058: SslMM
- S1200: StealBit
- S0491: StrongPity
- S0603: Stuxnet
- S0595: ThiefQuest
- S0004: TinyZBot
- S0266: TrickBot
- S0130: Unknown Logger
- S0670: WarzoneRAT
- S0579: Waterbear
- S0689: WhisperGate
- S1065: Woody RAT
- S1207: XLoader
- S1114: ZIPLINE
- S0412: ZxShell
- S1048: macOS.OSAMiner
