# T1039: Data from Network Shared Drive


**ATT&CK ID:** T1039  
**Domain:** Mitre Attack  
**Tactic(s):** Collection  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1039  

## Description
Adversaries may search network shares on computers they have compromised to find files of interest. Sensitive data can be collected from remote systems via shared network drives (host shared directory, network file server, etc.) that are accessible from the current system prior to Exfiltration. Interactive command shells may be in use, and common functionality within [cmd](https://attack.mitre.org/software/S0106) may be used to gather information.

## Known Threat Groups Using This Technique
- G0007: APT28
- G0060: BRONZE BUTLER
- G0114: Chimera
- G0117: Fox Kitten
- G0047: Gamaredon Group
- G1039: RedCurl
- G0054: Sowbug
- G0045: menuPass

## Known Software Using This Technique
- S0128: BADNEWS
- S0050: CosmicDuke
- S0554: Egregor
- S0458: Ramsay
