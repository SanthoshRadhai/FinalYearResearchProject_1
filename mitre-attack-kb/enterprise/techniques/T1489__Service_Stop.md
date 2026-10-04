# T1489: Service Stop


**ATT&CK ID:** T1489  
**Domain:** Mitre Attack  
**Tactic(s):** Impact  
**Platforms:** ESXi, IaaS, Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1489  

## Description
Adversaries may stop or disable services on a system to render those services unavailable to legitimate users. Stopping critical services or processes can inhibit or stop response to an incident or aid in the adversary's overall objectives to cause damage to the environment.(Citation: Talos Olympic Destroyer 2018)(Citation: Novetta Blockbuster) 

Adversaries may accomplish this by disabling individual services of high importance to an organization, such as <code>MSExchangeIS</code>, which will make Exchange content inaccessible.(Citation: Novetta Blockbuster) In some cases, adversaries may stop or disable many or all services to render systems unusable.(Citation: Talos Olympic Destroyer 2018) Services or processes may not allow for modification of their data stores while running. Adversaries may stop services or processes in order to conduct [Data Destruction](https://attack.mitre.org/techniques/T1485) or [Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486) on the data stores of services like Exchange and SQL Server, or on virtual machines hosted on ESXi infrastructure.(Citation: SecureWorks WannaCry Analysis)(Citation: Crowdstrike Hypervisor Jackpotting Pt 2 2021)

Threat actors may also disable or stop service in cloud environments. For example, by leveraging the `DisableAPIServiceAccess` API in AWS, a threat actor may prevent the service from creating service-linked roles on new accounts in the AWS Organization.(Citation: Datadog Security Labs Cloud Persistence 2025)(Citation: AWS DisableAWSServiceAccess)

## Mitigations
- M1018: User Account Management
- M1022: Restrict File and Directory Permissions
- M1024: Restrict Registry Permissions
- M1030: Network Segmentation
- M1060: Out-of-Band Communications Channel

## Known Threat Groups Using This Technique
- G0119: Indrik Spider
- G0094: Kimsuky
- G1004: LAPSUS$
- G0032: Lazarus Group
- G1051: Medusa Group
- G0034: Sandworm Team
- G0102: Wizard Spider

## Known Software Using This Technique
- S1194: Akira _v2
- S0640: Avaddon
- S1053: AvosLocker
- S9015: BRICKSTORM
- S0638: Babuk
- S1181: BlackByte 2.0 Ransomware
- S1068: BlackCat
- S1096: Cheerscrypt
- S0611: Clop
- S0575: Conti
- S0625: Cuba
- S9013: DRYHOOK
- S0659: Diavol
- S0605: EKANS
- S1247: Embargo
- S1211: Hannotog
- S0697: HermeticWiper
- S0431: HotCroissant
- S1139: INC Ransomware
- S0604: Industroyer
- S1245: InvisibleFerret
- S0607: KillDisk
- S1199: LockBit 2.0
- S1202: LockBit 3.0
- S0582: LookBack
- S0449: Maze
- S1244: Medusa Ransomware
- S0576: MegaCortex
- S1191: Megazord
- S0688: Meteor
- S0457: Netwalker
- S0365: Olympic Destroyer
- S9014: PHASEJAM
- S0556: Pay2Key
- S1058: Prestige
- S0583: Pysa
- S1242: Qilin
- S0496: REvil
- S1150: ROADSWEEP
- S0481: Ragnar Locker
- S1212: RansomHub
- S0400: RobbinHood
- S1073: Royal
- S0446: Ryuk
- S0533: SLOTHFULMEDIA
- S1217: VIRTUALPITA
- S0366: WannaCry
