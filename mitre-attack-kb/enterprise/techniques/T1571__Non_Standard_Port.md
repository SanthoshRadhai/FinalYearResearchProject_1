# T1571: Non-Standard Port


**ATT&CK ID:** T1571  
**Domain:** Mitre Attack  
**Tactic(s):** Command And Control  
**Platforms:** ESXi, Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1571  

## Description
Adversaries may communicate using a protocol and port pairing that are typically not associated. For example, HTTPS over port 8088(Citation: Symantec Elfin Mar 2019) or port 587(Citation: Fortinet Agent Tesla April 2018) as opposed to the traditional port 443. Adversaries may make changes to the standard port used by a protocol to bypass filtering or muddle analysis/parsing of network data.

Adversaries may also make changes to victim systems to abuse non-standard ports. For example, Registry keys and other configuration settings can be used to modify protocol and port pairings.(Citation: change_rdp_port_conti)

## Mitigations
- M1030: Network Segmentation
- M1031: Network Intrusion Prevention

## Known Threat Groups Using This Technique
- G0099: APT-C-36
- G0050: APT32
- G0064: APT33
- G1052: Contagious Interview
- G0105: DarkVishnya
- G1003: Ember Bear
- G0046: FIN7
- G0047: Gamaredon Group
- G0032: Lazarus Group
- G0059: Magic Hound
- G0069: MuddyWater
- G1042: RedEcho
- G0106: Rocke
- G0034: Sandworm Team
- G0091: Silence
- G1047: Velvet Ant
- G0090: WIRTE

## Known Software Using This Technique
- S0245: BADCALL
- S0239: Bankshot
- S1246: BeaverTail
- S0574: BendyBear
- S1155: Covenant
- S0687: Cyclops Blink
- S0021: Derusbi
- S0367: Emotet
- S9010: GlassWorm
- S0493: GoldenSpy
- S0237: GravityRAT
- S0246: HARDRAIN
- S0376: HOPLIGHT
- S1211: Hannotog
- S9023: HiddenFace
- S1245: InvisibleFerret
- S1016: MacMa
- S0455: Metamorfo
- S0149: MoonWind
- S0352: OSX_OCEANLOTUS.D
- S1145: Pikabot
- S1031: PingPull
- S0013: PlugX
- S0428: PoetRAT
- S0262: QuasarRAT
- S0148: RTM
- S1130: Raspberry Robin
- S0153: RedLeaves
- S1078: RotaJakiro
- S9024: SPAWNCHIMERA
- S1049: SUGARUSH
- S1085: Sardonic
- S0491: StrongPity
- S9001: SystemBC
- S0263: TYPEFRAME
- S0266: TrickBot
- S1218: VIRTUALPIE
- S1217: VIRTUALPITA
- S0515: WellMail
- S0412: ZxShell
- S0385: njRAT
