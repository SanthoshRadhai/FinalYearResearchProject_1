# T1049: System Network Connections Discovery


**ATT&CK ID:** T1049  
**Domain:** Mitre Attack  
**Tactic(s):** Discovery  
**Platforms:** ESXi, IaaS, Linux, macOS, Network Devices, Windows  
**Reference:** https://attack.mitre.org/techniques/T1049  

## Description
Adversaries may attempt to get a listing of network connections to or from the compromised system they are currently accessing or from remote systems by querying for information over the network. 

An adversary who gains access to a system that is part of a cloud-based environment may map out Virtual Private Clouds or Virtual Networks in order to determine what systems and services are connected. The actions performed are likely the same types of discovery techniques depending on the operating system, but the resulting information may include details about the networked cloud environment relevant to the adversary's goals. Cloud providers may have different ways in which their virtual networks operate.(Citation: Amazon AWS VPC Guide)(Citation: Microsoft Azure Virtual Network Overview)(Citation: Google VPC Overview) Similarly, adversaries who gain access to network devices may also perform similar discovery activities to gather information about connected systems and services.

Utilities and commands that acquire this information include [netstat](https://attack.mitre.org/software/S0104), "net use," and "net session" with [Net](https://attack.mitre.org/software/S0039). In Mac and Linux, [netstat](https://attack.mitre.org/software/S0104) and <code>lsof</code> can be used to list current connections. <code>who -a</code> and <code>w</code> can be used to show which users are currently logged in, similar to "net session". Additionally, built-in features native to network devices and [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) may be used (e.g. <code>show ip sockets</code>, <code>show tcp brief</code>).(Citation: US-CERT-TA18-106A) On ESXi servers, the command `esxi network ip connection list` can be used to list active network connections.(Citation: Sygnia ESXi Ransomware 2025)

## Known Threat Groups Using This Technique
- G0006: APT1
- G0022: APT3
- G0050: APT32
- G0082: APT38
- G0096: APT41
- G1023: APT5
- G0138: Andariel
- G0135: BackdoorDiplomacy
- G0114: Chimera
- G1006: Earth Lusca
- G1016: FIN13
- G0093: GALLIUM
- G1001: HEXANE
- G1032: INC Ransom
- G0004: Ke3chang
- G0032: Lazarus Group
- G0030: Lotus Blossom
- G0059: Magic Hound
- G0069: MuddyWater
- G0129: Mustang Panda
- G0049: OilRig
- G0033: Poseidon Group
- G0034: Sandworm Team
- G0139: TeamTNT
- G0027: Threat Group-3390
- G1022: ToddyCat
- G0081: Tropic Trooper
- G0010: Turla
- G1047: Velvet Ant
- G1017: Volt Typhoon
- G0018: admin@338
- G0045: menuPass

## Known Software Using This Technique
- S0456: Aria-body
- S1081: BADHATCH
- S0638: Babuk
- S0089: BlackEnergy
- S0335: Carbon
- S0154: Cobalt Strike
- S0244: Comnie
- S0575: Conti
- S0488: CrackMapExec
- S0625: Cuba
- S0567: Dtrack
- S0038: Duqu
- S0554: Egregor
- S0363: Empire
- S0091: Epic
- S1144: FRP
- S0696: Flagpro
- S0237: GravityRAT
- S0356: KONNI
- S1075: KOPILUWAK
- S0236: Kwampirs
- S0681: Lizar
- S0532: Lucifer
- S1141: LunarWeb
- S0443: MESSAGETAP
- S1060: Mafalda
- S0449: Maze
- S0198: NETWIRE
- S0039: Net
- S0165: OSInfo
- S0439: Okrum
- S0184: POWRUNER
- S1228: PUBLOAD
- S1091: Pacu
- S0013: PlugX
- S0378: PoshC2
- S0192: Pupy
- S1032: PyDCrypt
- S0650: QakBot
- S0241: RATANKBA
- S0458: Ramsay
- S0153: RedLeaves
- S0125: Remsec
- S0063: SHOTPUT
- S0533: SLOTHFULMEDIA
- S1085: Sardonic
- S0445: ShimRatReporter
- S0589: Sibot
- S0633: Sliver
- S0374: SpeakUp
- S0018: Sykipot
- S9041: TeamPCP Cloud Stealer
- S0678: Torisma
- S0094: Trojan.Karagany
- S0452: USBferry
- S0180: Volgmer
- S0579: Waterbear
- S0251: Zebrocy
- S0283: jRAT
- S0102: nbtstat
- S0104: netstat
