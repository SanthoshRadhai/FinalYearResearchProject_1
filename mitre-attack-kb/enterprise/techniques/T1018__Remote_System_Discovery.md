# T1018: Remote System Discovery


**ATT&CK ID:** T1018  
**Domain:** Mitre Attack  
**Tactic(s):** Discovery  
**Platforms:** ESXi, Linux, macOS, Network Devices, Windows  
**Reference:** https://attack.mitre.org/techniques/T1018  

## Description
Adversaries may attempt to get a listing of other systems by IP address, hostname, or other logical identifier on a network that may be used for Lateral Movement from the current system. Functionality could exist within remote access tools to enable this, but utilities available on the operating system could also be used such as  [Ping](https://attack.mitre.org/software/S0097), <code>net view</code> using [Net](https://attack.mitre.org/software/S0039), or, on ESXi servers, `esxcli network diag ping`.

Adversaries may also analyze data from local host files (ex: <code>C:\Windows\System32\Drivers\etc\hosts</code> or <code>/etc/hosts</code>) or other passive means (such as local [Arp](https://attack.mitre.org/software/S0099) cache entries) in order to discover the presence of remote systems in an environment.

Adversaries may also target discovery of network infrastructure as well as leverage [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) commands on network devices to gather detailed information about systems within a network (e.g. <code>show cdp neighbors</code>, <code>show arp</code>).(Citation: US-CERT-TA18-106A)(Citation: CISA AR21-126A FIVEHANDS May 2021)

## Known Threat Groups Using This Technique
- G0022: APT3
- G0050: APT32
- G0087: APT39
- G0096: APT41
- G1030: Agrius
- G1024: Akira
- G0060: BRONZE BUTLER
- G1043: BlackByte
- G0114: Chimera
- G0009: Deep Panda
- G0035: Dragonfly
- G1006: Earth Lusca
- G1003: Ember Bear
- G0053: FIN5
- G0037: FIN6
- G0061: FIN8
- G0117: Fox Kitten
- G0093: GALLIUM
- G0125: HAFNIUM
- G1001: HEXANE
- G0119: Indrik Spider
- G0004: Ke3chang
- G0077: Leafminer
- G0030: Lotus Blossom
- G0059: Magic Hound
- G1051: Medusa Group
- G1054: MirrorFace
- G0129: Mustang Panda
- G0019: Naikon
- G1040: Play
- G0106: Rocke
- G0034: Sandworm Team
- G1015: Scattered Spider
- G1057: ShinyHunters
- G0091: Silence
- G0027: Threat Group-3390
- G1022: ToddyCat
- G0010: Turla
- G1017: Volt Typhoon
- G0102: Wizard Spider
- G0045: menuPass

## Known Software Using This Technique
- S0552: AdFind
- S0099: Arp
- S1081: BADHATCH
- S0093: Backdoor.Oldrea
- S0534: Bazar
- S0570: BitPaymer
- S1070: Black Basta
- S1068: BlackCat
- S0521: BloodHound
- S9042: CanisterWorm
- S0335: Carbon
- S0154: Cobalt Strike
- S0244: Comnie
- S0575: Conti
- S0488: CrackMapExec
- S0694: DRATzarus
- S1159: DUSTTRAP
- S0659: Diavol
- S0091: Epic
- S0696: Flagpro
- S1044: FunnyDream
- S1198: Gomir
- S1229: Havoc
- S0698: HermeticWizard
- S0604: Industroyer
- S0599: Kinsing
- S0236: Kwampirs
- S9020: LODEINFO
- S0233: MURKYTOP
- S1146: MgBot
- S0590: NBTscan
- S0039: Net
- S0359: Nltest
- S0165: OSInfo
- S0365: Olympic Destroyer
- S0097: Ping
- S0428: PoetRAT
- S0650: QakBot
- S1242: Qilin
- S0241: RATANKBA
- S0684: ROADTools
- S1212: RansomHub
- S0125: Remsec
- S0063: SHOTPUT
- S0692: SILENTTRINITY
- S0140: Shamoon
- S0646: SpicyOmelette
- S0018: Sykipot
- S0586: TAINTEDSCRIBE
- S0266: TrickBot
- S0452: USBferry
- S0366: WannaCry
- S0385: njRAT
- S0248: yty
