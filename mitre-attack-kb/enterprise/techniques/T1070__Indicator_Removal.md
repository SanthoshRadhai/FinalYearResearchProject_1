# T1070: Indicator Removal


**ATT&CK ID:** T1070  
**Domain:** Mitre Attack  
**Tactic(s):** Stealth  
**Platforms:** Containers, ESXi, Linux, macOS, Network Devices, Office Suite, Windows  
**Reference:** https://attack.mitre.org/techniques/T1070  

## Description
Adversaries may selectively delete or modify artifacts generated to reduce indications of their presence and blend in with legitimate activity. Rather than broadly removing evidence, adversaries may target specific artifacts that appear anomalous or are likely to draw scrutiny, while leaving sufficient data intact to maintain the appearance of normal system behavior.

Artifacts such as command histories, log entries, or file metadata may be altered in ways that align with expected user or system activity. Location, format, and type of artifact (such as command or login history) are often platform-specific, allowing adversaries to tailor modifications that minimize suspicion.

These actions may not prevent detection entirely but can delay recognition of malicious activity or reduce the fidelity of alerts by making events appear benign or consistent with routine operations. Additionally, selectively removed or modified artifacts may still be recoverable through deeper forensic analysis, though their absence or alteration can complicate timeline reconstruction and attribution.

## Sub-techniques
- T1070.003: Clear Command History
- T1070.004: File Deletion
- T1070.005: Network Share Connection Removal
- T1070.006: Timestomp
- T1070.007: Clear Network Connection History and Configurations
- T1070.008: Clear Mailbox Data
- T1070.009: Clear Persistence
- T1070.010: Relocate Malware

## Mitigations
- M1022: Restrict File and Directory Permissions
- M1029: Remote Data Storage
- M1041: Encrypt Sensitive Information

## Known Threat Groups Using This Technique
- G1044: APT42
- G1023: APT5
- G0032: Lazarus Group
- G0129: Mustang Panda

## Known Software Using This Technique
- S1161: BPFDoor
- S0239: Bankshot
- S0089: BlackEnergy
- S0527: CSPY Downloader
- S1159: DUSTTRAP
- S0673: DarkWatchman
- S0695: Donut
- S0568: EVILNUM
- S0696: Flagpro
- S1044: FunnyDream
- S0697: HermeticWiper
- S1132: IPsec Helper
- S9029: IronWind
- S0449: Maze
- S0455: Metamorfo
- S1135: MultiLayer Wiper
- S0691: Neoichor
- S0229: Orz
- S0332: Remcos
- S0448: Rising Sun
- S0461: SDBbot
- S0692: SILENTTRINITY
- S0559: SUNBURST
- S1085: Sardonic
- S0596: ShadowPad
- S0589: Sibot
- S0603: Stuxnet
