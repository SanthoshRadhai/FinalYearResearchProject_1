# T1532: Archive Collected Data


**ATT&CK ID:** T1532  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1532  

## Description
Adversaries may compress and/or encrypt data that is collected prior to exfiltration. Compressing data can help to obfuscate its contents and minimize use of network resources. Encryption can be used to hide information that is being exfiltrated from detection or make exfiltration less conspicuous upon inspection by a defender. 

 

Both compression and encryption are done prior to exfiltration, and can be performed using a utility, programming library, or custom algorithm.

## Known Software Using This Technique
- S0422: Anubis
- S0540: Asacub
- S1079: BOULDSPY
- S1094: BRATA
- S1243: DCHSpy
- S0505: Desert Scorpion
- S0405: Exodus
- S0577: FrozenCell
- S0535: Golden Cup
- S0421: GolfSpy
- S1185: LightSpy
- S1082: Sunbird
- S0424: Triada
