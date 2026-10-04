# T1119: Automated Collection


**ATT&CK ID:** T1119  
**Domain:** Mitre Attack  
**Tactic(s):** Collection  
**Platforms:** IaaS, Linux, macOS, Office Suite, SaaS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1119  

## Description
Once established within a system or network, an adversary may use automated techniques for collecting internal data. Methods for performing this technique could include use of a [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059) to search for and copy information fitting set criteria such as file type, location, or name at specific time intervals. 

In cloud-based environments, adversaries may also use cloud APIs, data pipelines, command line interfaces, or extract, transform, and load (ETL) services to automatically collect data.(Citation: Mandiant UNC3944 SMS Phishing 2023) 

This functionality could also be built into remote access tools. 

This technique may incorporate use of other techniques such as [File and Directory Discovery](https://attack.mitre.org/techniques/T1083) and [Lateral Tool Transfer](https://attack.mitre.org/techniques/T1570) to identify and move files, as well as [Cloud Service Dashboard](https://attack.mitre.org/techniques/T1538) and [Cloud Storage Object Discovery](https://attack.mitre.org/techniques/T1619) to identify resources in cloud environments.

## Mitigations
- M1029: Remote Data Storage
- M1041: Encrypt Sensitive Information

## Known Threat Groups Using This Technique
- G0006: APT1
- G0007: APT28
- G1030: Agrius
- G0114: Chimera
- G0142: Confucius
- G1003: Ember Bear
- G0053: FIN5
- G0037: FIN6
- G0047: Gamaredon Group
- G0125: HAFNIUM
- G0004: Ke3chang
- G0129: Mustang Panda
- G0049: OilRig
- G0040: Patchwork
- G1039: RedCurl
- G0121: Sidewinder
- G0027: Threat Group-3390
- G0081: Tropic Trooper
- G1055: VOID MANTICORE
- G1035: Winter Vivern
- G0045: menuPass

## Known Software Using This Technique
- S0622: AppleSeed
- S0438: Attor
- S0128: BADNEWS
- S0239: Bankshot
- S0244: Comnie
- S0538: Crutch
- S1111: DarkGate
- S0363: Empire
- S1044: FunnyDream
- S0597: GoldFinder
- S0170: Helminth
- S0260: InvisiMole
- S9035: LAMEHUG
- S0395: LightNeuron
- S1101: LoFiSe
- S1213: Lumma Stealer
- S0443: MESSAGETAP
- S0455: Metamorfo
- S0339: Micropsia
- S9043: Mini Shai-Hulud
- S0699: Mythic
- S0198: NETWIRE
- S1131: NPPSPY
- S1017: OutSteel
- S1109: PACEMAKER
- S1091: Pacu
- S0428: PoetRAT
- S0378: PoshC2
- S0238: Proxysvc
- S0684: ROADTools
- S0148: RTM
- S1148: Raccoon Stealer
- S0458: Ramsay
- S1078: RotaJakiro
- S0090: Rover
- S9008: Shai-Hulud
- S0445: ShimRatReporter
- S1183: StrelaStealer
- S0491: StrongPity
- S0098: T9000
- S0467: TajMahal
- S9041: TeamPCP Cloud Stealer
- S0136: USBStealer
- S0257: VERMIN
- S0476: Valak
- S0466: WindTail
- S0251: Zebrocy
- S1043: ccf32
