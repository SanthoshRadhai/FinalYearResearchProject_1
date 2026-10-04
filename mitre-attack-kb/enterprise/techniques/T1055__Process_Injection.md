# T1055: Process Injection


**ATT&CK ID:** T1055  
**Domain:** Mitre Attack  
**Tactic(s):** Stealth, Privilege Escalation  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1055  

## Description
Adversaries may inject code into processes in order to evade process-based defenses as well as possibly elevate privileges. Process injection is a method of executing arbitrary code in the address space of a separate live process. Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via process injection may also evade detection from security products since the execution is masked under a legitimate process. 

There are many different ways to inject code into a process, many of which abuse legitimate functionalities. These implementations exist for every major OS but are typically platform specific. 

More sophisticated samples may perform multiple process injections to segment modules and further evade detection, utilizing named pipes or other inter-process communication (IPC) mechanisms as a communication channel.

## Sub-techniques
- T1055.001: Dynamic-link Library Injection
- T1055.002: Portable Executable Injection
- T1055.003: Thread Execution Hijacking
- T1055.004: Asynchronous Procedure Call
- T1055.005: Thread Local Storage
- T1055.008: Ptrace System Calls
- T1055.009: Proc Memory
- T1055.011: Extra Window Memory Injection
- T1055.012: Process Hollowing
- T1055.013: Process Doppelgänging
- T1055.014: VDSO Hijacking
- T1055.015: ListPlanting

## Mitigations
- M1026: Privileged Account Management
- M1040: Behavior Prevention on Endpoint

## Known Threat Groups Using This Technique
- G0050: APT32
- G0067: APT37
- G0082: APT38
- G0096: APT41
- G1023: APT5
- G1043: BlackByte
- G0080: Cobalt Group
- G0047: Gamaredon Group
- G0094: Kimsuky
- G0068: PLATINUM
- G0091: Silence
- G1018: TA2541
- G0010: Turla
- G1047: Velvet Ant
- G0102: Wizard Spider

## Known Software Using This Technique
- S0469: ABK
- S1074: ANDROMEDA
- S0331: Agent Tesla
- S0438: Attor
- S0347: AuditCred
- S0473: Avenger
- S1081: BADHATCH
- S0470: BBK
- S0093: Backdoor.Oldrea
- S0534: Bazar
- S1181: BlackByte 2.0 Ransomware
- S1039: Bumblebee
- S1105: COATHANGER
- S0348: Cardinal RAT
- S0660: Clambling
- S0154: Cobalt Strike
- S0614: CostaBricks
- S9021: DOWNIISSA
- S1159: DUSTTRAP
- S0695: Donut
- S0024: Dyre
- S0554: Egregor
- S0363: Empire
- S0168: Gazer
- S0561: GuLoader
- S0376: HOPLIGHT
- S0040: HTRAN
- S9023: HiddenFace
- S0398: HyperBro
- S0260: InvisiMole
- S0581: IronNetInjector
- S0044: JHUHUGIT
- S0201: JPIN
- S9020: LODEINFO
- S0681: Lizar
- S0084: Mis-Type
- S1122: Mispadu
- S0198: NETWIRE
- S9025: NOOPLDR
- S0247: NavRAT
- S1100: Ninja
- S0664: Pandora
- S1050: PcShare
- S0378: PoshC2
- S9019: PureCrypter
- S0650: QakBot
- S0496: REvil
- S0240: ROKRAT
- S0332: Remcos
- S0446: Ryuk
- S0692: SILENTTRINITY
- S0533: SLOTHFULMEDIA
- S0596: ShadowPad
- S0633: Sliver
- S0226: Smoke Loader
- S0380: StoneDrill
- S0436: TSCookie
- S0266: TrickBot
- S0670: WarzoneRAT
- S0579: Waterbear
- S0206: Wiarp
- S0176: Wingbird
- S1065: Woody RAT
- S0032: gh0st RAT
- S1059: metaMain
