# T1124: System Time Discovery


**ATT&CK ID:** T1124  
**Domain:** Mitre Attack  
**Tactic(s):** Discovery  
**Platforms:** ESXi, Linux, macOS, Network Devices, Windows  
**Reference:** https://attack.mitre.org/techniques/T1124  

## Description
An adversary may gather the system time and/or time zone settings from a local or remote system. The system time is set and stored by services, such as the Windows Time Service on Windows or <code>systemsetup</code> on macOS.(Citation: MSDN System Time)(Citation: Technet Windows Time Service)(Citation: systemsetup mac time) These time settings may also be synchronized between systems and services in an enterprise network, typically accomplished with a network time server within a domain.(Citation: Mac Time Sync)(Citation: linux system time)

System time information may be gathered in a number of ways, such as with [Net](https://attack.mitre.org/software/S0039) on Windows by performing <code>net time \\hostname</code> to gather the system time on a remote system. The victim's time zone may also be inferred from the current system time or gathered by using <code>w32tm /tz</code>.(Citation: Technet Windows Time Service) In addition, adversaries can discover device uptime through functions such as <code>GetTickCount()</code> to determine how long it has been since the system booted up.(Citation: Virtualization/Sandbox Evasion)

On network devices, [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) commands such as `show clock detail` can be used to see the current time configuration.(Citation: show_clock_detail_cisco_cmd) On ESXi servers, `esxcli system clock get` can be used for the same purpose.

In addition, system calls – such as <code>time()</code> – have been used to collect the current time on Linux devices.(Citation: MAGNET GOBLIN) On macOS systems, adversaries may use commands such as <code>systemsetup -gettimezone</code> or <code>timeIntervalSinceNow</code> to gather current time zone information or current date and time.(Citation: System Information Discovery Technique)(Citation: ESET DazzleSpy Jan 2022)

This information could be useful for performing other techniques, such as executing a file with a [Scheduled Task/Job](https://attack.mitre.org/techniques/T1053)(Citation: RSA EU12 They're Inside), or to discover locality information based on time zone to assist in victim targeting (i.e. [System Location Discovery](https://attack.mitre.org/techniques/T1614)). Adversaries may also use knowledge of system time as part of a time bomb, or delaying execution until a specified date/time.(Citation: AnyRun TimeBomb)

## Known Threat Groups Using This Technique
- G0060: BRONZE BUTLER
- G1012: CURIUM
- G0114: Chimera
- G0012: Darkhotel
- G0046: FIN7
- G0126: Higaisa
- G0094: Kimsuky
- G0032: Lazarus Group
- G0121: Sidewinder
- G0089: The White Company
- G0010: Turla
- G1048: UNC3886
- G1017: Volt Typhoon
- G0128: ZIRCONIUM

## Known Software Using This Technique
- S0331: Agent Tesla
- S0622: AppleSeed
- S0373: Astaroth
- S1087: AsyncRAT
- S1053: AvosLocker
- S0344: Azorult
- S1081: BADHATCH
- S0017: BISCUIT
- S0657: BLUELIGHT
- S0534: Bazar
- S1246: BeaverTail
- S0574: BendyBear
- S0268: Bisonal
- S9042: CanisterWorm
- S0351: Cannon
- S0335: Carbon
- S0660: Clambling
- S0126: ComRAT
- S0608: Conficker
- S0115: Crimson
- S1033: DCSrv
- S1134: DEADWOOD
- S0694: DRATzarus
- S1159: DUSTTRAP
- S1111: DarkGate
- S0673: DarkWatchman
- S0554: Egregor
- S0091: Epic
- S0396: EvilBunny
- S0267: FELIXROOT
- S1044: FunnyDream
- S0417: GRIFFON
- S9010: GlassWorm
- S0588: GoldMax
- S0531: Grandoreiro
- S0237: GravityRAT
- S0690: Green Lambert
- S0376: HOPLIGHT
- S0260: InvisiMole
- S1051: KEYPLUG
- S9020: LODEINFO
- S1244: Medusa Ransomware
- S0455: Metamorfo
- S9043: Mini Shai-Hulud
- S0149: MoonWind
- S0353: NOKKI
- S0039: Net
- S1147: Nightdoor
- S0439: Okrum
- S0264: OopsIE
- S1233: PAKLOG
- S1228: PUBLOAD
- S0501: PipeMon
- S0013: PlugX
- S0139: PowerDuke
- S0238: Proxysvc
- S0650: QakBot
- S0148: RTM
- S1148: Raccoon Stealer
- S0450: SHARPSTATS
- S0692: SILENTTRINITY
- S0559: SUNBURST
- S1064: SVCReady
- S0596: ShadowPad
- S0140: Shamoon
- S1178: ShrinkLocker
- S0615: SombRAT
- S1227: StarProxy
- S0380: StoneDrill
- S1034: StrifeWater
- S0603: Stuxnet
- S9001: SystemBC
- S0098: T9000
- S0586: TAINTEDSCRIBE
- S0011: Taidoor
- S0467: TajMahal
- S0678: Torisma
- S0275: UPPERCUT
- S0466: WindTail
- S0251: Zebrocy
- S0330: Zeus Panda
- S0471: build_downer
- S1043: ccf32
