# T1029: Scheduled Transfer


**ATT&CK ID:** T1029  
**Domain:** Mitre Attack  
**Tactic(s):** Exfiltration  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1029  

## Description
Adversaries may schedule data exfiltration to be performed only at certain times of day or at certain intervals. This could be done to blend traffic patterns with normal activity or availability.

When scheduled exfiltration is used, other exfiltration techniques likely apply as well to transfer the information out of the network, such as [Exfiltration Over C2 Channel](https://attack.mitre.org/techniques/T1041) or [Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048).

## Mitigations
- M1031: Network Intrusion Prevention

## Known Threat Groups Using This Technique
- G0126: Higaisa

## Known Software Using This Technique
- S0045: ADVSTORESHELL
- S0667: Chrommme
- S0154: Cobalt Strike
- S0126: ComRAT
- S0200: Dipsind
- S0696: Flagpro
- S0265: Kazuar
- S0395: LightNeuron
- S0211: Linfo
- S0409: Machete
- S1100: Ninja
- S0223: POWERSTATS
- S0596: ShadowPad
- S1019: Shark
- S0444: ShimRat
- S0668: TinyTurla
- S0283: jRAT
