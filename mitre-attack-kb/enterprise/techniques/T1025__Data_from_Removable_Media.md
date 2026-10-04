# T1025: Data from Removable Media


**ATT&CK ID:** T1025  
**Domain:** Mitre Attack  
**Tactic(s):** Collection  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1025  

## Description
Adversaries may search connected removable media on computers they have compromised to find files of interest. Sensitive data can be collected from any removable media (optical disk drive, USB memory, etc.) connected to the compromised system prior to Exfiltration. Interactive command shells may be in use, and common functionality within [cmd](https://attack.mitre.org/software/S0106) may be used to gather information. 

Some adversaries may also use [Automated Collection](https://attack.mitre.org/techniques/T1119) on removable media.

## Mitigations
- M1057: Data Loss Prevention

## Known Threat Groups Using This Technique
- G0007: APT28
- G0047: Gamaredon Group
- G0049: OilRig
- G0010: Turla

## Known Software Using This Technique
- S0622: AppleSeed
- S0456: Aria-body
- S0128: BADNEWS
- S0050: CosmicDuke
- S0115: Crimson
- S0538: Crutch
- S0569: Explosive
- S0036: FLASHFLOOD
- S1044: FunnyDream
- S0237: GravityRAT
- S0260: InvisiMole
- S0409: Machete
- S1146: MgBot
- S0644: ObliqueRAT
- S0113: Prikormka
- S0458: Ramsay
- S0125: Remsec
- S0090: Rover
- S0467: TajMahal
- S0136: USBStealer
