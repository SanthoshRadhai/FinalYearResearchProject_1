# T1486: Data Encrypted for Impact


**ATT&CK ID:** T1486  
**Domain:** Mitre Attack  
**Tactic(s):** Impact  
**Platforms:** ESXi, IaaS, Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1486  

## Description
Adversaries may encrypt data on target systems or on large numbers of systems in a network to interrupt availability to system and network resources. They can attempt to render stored data inaccessible by encrypting files or data on local and remote drives and withholding access to a decryption key. This may be done in order to extract monetary compensation from a victim in exchange for decryption or a decryption key (ransomware) or to render data permanently inaccessible in cases where the key is not saved or transmitted.(Citation: US-CERT Ransomware 2016)(Citation: FireEye WannaCry 2017)(Citation: US-CERT NotPetya 2017)(Citation: US-CERT SamSam 2018)

In the case of ransomware, it is typical that common user files like Office documents, PDFs, images, videos, audio, text, and source code files will be encrypted (and often renamed and/or tagged with specific file markers). Adversaries may need to first employ other behaviors, such as [File and Directory Permissions Modification](https://attack.mitre.org/techniques/T1222) or [System Shutdown/Reboot](https://attack.mitre.org/techniques/T1529), in order to unlock and/or gain access to manipulate these files.(Citation: CarbonBlack Conti July 2020) In some cases, adversaries may encrypt critical system files, disk partitions, and the MBR.(Citation: US-CERT NotPetya 2017) Adversaries may also encrypt virtual machines hosted on ESXi or other hypervisors.(Citation: Crowdstrike Hypervisor Jackpotting Pt 2 2021) 

To maximize impact on the target organization, malware designed for encrypting data may have worm-like features to propagate across a network by leveraging other attack techniques like [Valid Accounts](https://attack.mitre.org/techniques/T1078), [OS Credential Dumping](https://attack.mitre.org/techniques/T1003), and [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002).(Citation: FireEye WannaCry 2017)(Citation: US-CERT NotPetya 2017) Encryption malware may also leverage [Internal Defacement](https://attack.mitre.org/techniques/T1491/001), such as changing victim wallpapers or ESXi server login messages, or otherwise intimidate victims by sending ransom notes or other messages to connected printers (known as "print bombing").(Citation: NHS Digital Egregor Nov 2020)(Citation: Varonis)

In cloud environments, storage objects within compromised accounts may also be encrypted.(Citation: Rhino S3 Ransomware Part 1) For example, in AWS environments, adversaries may leverage services such as AWS’s Server-Side Encryption with Customer Provided Keys (SSE-C) to encrypt data.(Citation: Halcyon AWS Ransomware 2025)

## Mitigations
- M1040: Behavior Prevention on Endpoint
- M1053: Data Backup

## Known Threat Groups Using This Technique
- G0082: APT38
- G0096: APT41
- G1024: Akira
- G1043: BlackByte
- G0046: FIN7
- G0061: FIN8
- G1032: INC Ransom
- G0119: Indrik Spider
- G0059: Magic Hound
- G1051: Medusa Group
- G1036: Moonstone Sleet
- G0034: Sandworm Team
- G1015: Scattered Spider
- G1053: Storm-0501
- G1046: Storm-1811
- G0092: TA505
- G1056: TeamPCP
- G1055: VOID MANTICORE
- G1050: Water Galura

## Known Software Using This Technique
- S1129: Akira
- S1194: Akira _v2
- S1133: Apostle
- S0640: Avaddon
- S1053: AvosLocker
- S0638: Babuk
- S0606: Bad Rabbit
- S0570: BitPaymer
- S1070: Black Basta
- S1181: BlackByte 2.0 Ransomware
- S1180: BlackByte Ransomware
- S1068: BlackCat
- S1096: Cheerscrypt
- S0611: Clop
- S0575: Conti
- S0625: Cuba
- S1033: DCSrv
- S0616: DEATHRANSOM
- S1111: DarkGate
- S0659: Diavol
- S0605: EKANS
- S0554: Egregor
- S1247: Embargo
- S0618: FIVEHANDS
- S0617: HELLOKITTY
- S1139: INC Ransomware
- S0389: JCry
- S0607: KillDisk
- S9020: LODEINFO
- S1199: LockBit 2.0
- S1202: LockBit 3.0
- S0372: LockerGoga
- S0449: Maze
- S1244: Medusa Ransomware
- S0576: MegaCortex
- S1191: Megazord
- S1137: Moneybird
- S0457: Netwalker
- S0368: NotPetya
- S0556: Pay2Key
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
- S0370: SamSam
- S0639: Seth-Locker
- S0140: Shamoon
- S1178: ShrinkLocker
- S0242: SynAck
- S0595: ThiefQuest
- S0366: WannaCry
- S0612: WastedLocker
- S0658: XCSSET
- S0341: Xbash
