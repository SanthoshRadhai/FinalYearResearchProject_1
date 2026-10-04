# T1570: Lateral Tool Transfer


**ATT&CK ID:** T1570  
**Domain:** Mitre Attack  
**Tactic(s):** Lateral Movement  
**Platforms:** ESXi, Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1570  

## Description
Adversaries may transfer tools or other files between systems in a compromised environment. Once brought into the victim environment (i.e., [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105)) files may then be copied from one system to another to stage adversary tools or other files over the course of an operation.

Adversaries may copy files between internal victim systems to support lateral movement using inherent file sharing protocols such as file sharing over [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) to connected network shares or with authenticated connections via [Remote Desktop Protocol](https://attack.mitre.org/techniques/T1021/001).(Citation: Unit42 LockerGoga 2019)

Files can also be transferred using native or otherwise present tools on the victim system, such as scp, rsync, curl, sftp, and [ftp](https://attack.mitre.org/software/S0095). In some cases, adversaries may be able to leverage [Web Service](https://attack.mitre.org/techniques/T1102)s such as Dropbox or OneDrive to copy files from one machine to another via shared, automatically synced folders.(Citation: Dropbox Malware Sync)

## Mitigations
- M1031: Network Intrusion Prevention
- M1037: Filter Network Traffic

## Known Threat Groups Using This Technique
- G0050: APT32
- G0096: APT41
- G1030: Agrius
- G1007: Aoqin Dragon
- G1043: BlackByte
- G0114: Chimera
- G1003: Ember Bear
- G0051: FIN10
- G0093: GALLIUM
- G1032: INC Ransom
- G0059: Magic Hound
- G1051: Medusa Group
- G0034: Sandworm Team
- G1046: Storm-1811
- G0010: Turla
- G1048: UNC3886
- G1047: Velvet Ant
- G1017: Volt Typhoon
- G0102: Wizard Spider

## Known Software Using This Technique
- S0190: BITSAdmin
- S1180: BlackByte Ransomware
- S1068: BlackCat
- S0062: DustySky
- S0367: Emotet
- S0361: Expand
- S1229: Havoc
- S0698: HermeticWizard
- S1139: INC Ransomware
- S1132: IPsec Helper
- S0357: Impacket
- S0372: LockerGoga
- S0532: Lucifer
- S0457: Netwalker
- S0365: Olympic Destroyer
- S1017: OutSteel
- S0029: PsExec
- S1242: Qilin
- S9030: SameCoin
- S0140: Shamoon
- S0603: Stuxnet
- S1218: VIRTUALPIE
- S1217: VIRTUALPITA
- S0366: WannaCry
- S0106: cmd
- S0404: esentutl
- S0095: ftp
