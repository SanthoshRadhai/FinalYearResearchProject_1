# T1490: Inhibit System Recovery


**ATT&CK ID:** T1490  
**Domain:** Mitre Attack  
**Tactic(s):** Impact  
**Platforms:** Containers, ESXi, IaaS, Linux, macOS, Network Devices, Windows  
**Reference:** https://attack.mitre.org/techniques/T1490  

## Description
Adversaries may delete or remove built-in data and turn off services designed to aid in the recovery of a corrupted system to prevent recovery.(Citation: Talos Olympic Destroyer 2018)(Citation: FireEye WannaCry 2017) This may deny access to available backups and recovery options.

Operating systems may contain features that can help fix corrupted systems, such as a backup catalog, volume shadow copies, and automatic repair features. Adversaries may disable or delete system recovery features to augment the effects of [Data Destruction](https://attack.mitre.org/techniques/T1485) and [Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486).(Citation: Talos Olympic Destroyer 2018)(Citation: FireEye WannaCry 2017) Furthermore, adversaries may disable recovery notifications, then corrupt backups.(Citation: disable_notif_synology_ransom)

A number of native Windows utilities have been used by adversaries to disable or delete system recovery features:

* <code>vssadmin.exe</code> can be used to delete all volume shadow copies on a system - <code>vssadmin.exe delete shadows /all /quiet</code>
* [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) can be used to delete volume shadow copies - <code>wmic shadowcopy delete</code>
* <code>wbadmin.exe</code> can be used to delete the Windows Backup Catalog - <code>wbadmin.exe delete catalog -quiet</code>
* <code>bcdedit.exe</code> can be used to disable automatic Windows recovery features by modifying boot configuration data - <code>bcdedit.exe /set {default} bootstatuspolicy ignoreallfailures & bcdedit /set {default} recoveryenabled no</code>
* <code>REAgentC.exe</code> can be used to disable Windows Recovery Environment (WinRE) repair/recovery options of an infected system
* <code>diskshadow.exe</code> can be used to delete all volume shadow copies on a system - <code>diskshadow delete shadows all</code> (Citation: Diskshadow) (Citation: Crytox Ransomware)

On network devices, adversaries may leverage [Disk Wipe](https://attack.mitre.org/techniques/T1561) to delete backup firmware images and reformat the file system, then [System Shutdown/Reboot](https://attack.mitre.org/techniques/T1529) to reload the device. Together this activity may leave network devices completely inoperable and inhibit recovery operations.

On ESXi servers, adversaries may delete or encrypt snapshots of virtual machines to support [Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486), preventing them from being leveraged as backups (e.g., via ` vim-cmd vmsvc/snapshot.removeall`).(Citation: Cybereason)

Adversaries may also delete “online” backups that are connected to their network – whether via network storage media or through folders that sync to cloud services.(Citation: ZDNet Ransomware Backups 2020) In cloud environments, adversaries may disable versioning and backup policies and delete snapshots, database backups, machine images, and prior versions of objects designed to be used in disaster recovery scenarios.(Citation: Dark Reading Code Spaces Cyber Attack)(Citation: Rhino Security Labs AWS S3 Ransomware)

## Mitigations
- M1018: User Account Management
- M1028: Operating System Configuration
- M1038: Execution Prevention
- M1053: Data Backup

## Known Threat Groups Using This Technique
- G1043: BlackByte
- G1051: Medusa Group
- G0034: Sandworm Team
- G1015: Scattered Spider
- G1053: Storm-0501
- G1055: VOID MANTICORE
- G0102: Wizard Spider

## Known Software Using This Technique
- S1129: Akira
- S0640: Avaddon
- S1136: BFG Agonizer
- S0638: Babuk
- S0570: BitPaymer
- S1070: Black Basta
- S1181: BlackByte 2.0 Ransomware
- S1180: BlackByte Ransomware
- S1068: BlackCat
- S0611: Clop
- S0608: Conficker
- S0575: Conti
- S0616: DEATHRANSOM
- S1111: DarkGate
- S0673: DarkWatchman
- S0659: Diavol
- S0605: EKANS
- S1247: Embargo
- S0618: FIVEHANDS
- S0132: H1N1
- S0617: HELLOKITTY
- S0697: HermeticWiper
- S1139: INC Ransomware
- S0260: InvisiMole
- S0389: JCry
- S1199: LockBit 2.0
- S1202: LockBit 3.0
- S0449: Maze
- S1244: Medusa Ransomware
- S0576: MegaCortex
- S0688: Meteor
- S1135: MultiLayer Wiper
- S0457: Netwalker
- S0365: Olympic Destroyer
- S1162: Playcrypt
- S1058: Prestige
- S0654: ProLock
- S0583: Pysa
- S1242: Qilin
- S0496: REvil
- S1150: ROADSWEEP
- S0481: Ragnar Locker
- S1212: RansomHub
- S0400: RobbinHood
- S1073: Royal
- S0446: Ryuk
- S0366: WannaCry
- S0612: WastedLocker
