# T1560: Archive Collected Data


**ATT&CK ID:** T1560  
**Domain:** Mitre Attack  
**Tactic(s):** Collection  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1560  

## Description
An adversary may compress and/or encrypt data that is collected prior to exfiltration. Compressing the data can help to obfuscate the collected data and minimize the amount of data sent over the network.(Citation: DOJ GRU Indictment Jul 2018) Encryption can be used to hide information that is being exfiltrated from detection or make exfiltration less conspicuous upon inspection by a defender.

Both compression and encryption are done prior to exfiltration, and can be performed using a utility, 3rd party library, or custom method.

## Sub-techniques
- T1560.001: Archive via Utility
- T1560.002: Archive via Library
- T1560.003: Archive via Custom Method

## Mitigations
- M1047: Audit

## Known Threat Groups Using This Technique
- G0007: APT28
- G0050: APT32
- G0001: Axiom
- G1043: BlackByte
- G0035: Dragonfly
- G1003: Ember Bear
- G0037: FIN6
- G0004: Ke3chang
- G0032: Lazarus Group
- G0065: Leviathan
- G1014: LuminousMoth
- G0040: Patchwork
- G0045: menuPass

## Known Software Using This Technique
- S0045: ADVSTORESHELL
- S0331: Agent Tesla
- S0622: AppleSeed
- S0456: Aria-body
- S0657: BLUELIGHT
- S0093: Backdoor.Oldrea
- S0521: BloodHound
- S1039: Bumblebee
- S0454: Cadelspy
- S0667: Chrommme
- S0187: Daserf
- S0567: Dtrack
- S0363: Empire
- S0091: Epic
- S0343: Exaramel for Windows
- S0267: FELIXROOT
- S0249: Gold Dragon
- S1206: JumbledPath
- S0356: KONNI
- S0487: Kessel
- S9036: LP-Notes
- S0395: LightNeuron
- S0681: Lizar
- S1101: LoFiSe
- S0010: Lurid
- S0409: Machete
- S9043: Mini Shai-Hulud
- S9032: MuddyViper
- S0198: NETWIRE
- S0517: Pillowmint
- S1012: PowerLess
- S0113: Prikormka
- S0279: Proton
- S1148: Raccoon Stealer
- S0375: Remexi
- S0253: RunningRAT
- S0445: ShimRatReporter
- S1140: Spica
- S0586: TAINTEDSCRIBE
- S1196: Troll Stealer
- S0257: VERMIN
- S0515: WellMail
- S0658: XCSSET
- S0251: Zebrocy
