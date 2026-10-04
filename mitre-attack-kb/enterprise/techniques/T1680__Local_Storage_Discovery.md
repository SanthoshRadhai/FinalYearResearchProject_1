# T1680: Local Storage Discovery


**ATT&CK ID:** T1680  
**Domain:** Mitre Attack  
**Tactic(s):** Discovery  
**Platforms:** ESXi, IaaS, Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1680  

## Description
Adversaries may enumerate local drives, disks, and/or volumes and their attributes like total or free space and volume serial number. This can be done to prepare for ransomware-related encryption, to perform [Lateral Movement](https://attack.mitre.org/tactics/TA0109), or as a precursor to [Direct Volume Access](https://attack.mitre.org/techniques/T1006). 

On ESXi systems, adversaries may use [Hypervisor CLI](https://attack.mitre.org/techniques/T1059/012) commands such as `esxcli` to list storage connected to the host as well as `.vmdk` files.(Citation: TrendMicro)(Citation: TrendMicro ESXI Ransomware)

On Windows systems, adversaries can use `wmic logicaldisk get` to find information about local network drives. They can also use `Get-PSDrive` in PowerShell to retrieve drives and may additionally use Windows API functions such as `GetDriveType`.(Citation: Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024)(Citation: Volexity)

Linux has commands such as `parted`, `lsblk`, `fdisk`, `lshw`, and `df` that can list information about disk partitions such as size, type, file system types, and free space. The command `diskutil` on MacOS can be used to list disks while `system_profiler SPStorageDataType` can additionally show information such as a volume’s mount path, file system, and the type of drive in the system. 

Infrastructure as a Service (IaaS) cloud providers also have commands for storage discovery such as `describe volume` in AWS, `gcloud compute disks list` in GCP, and `az disk list` in Azure.(Citation: AWS docs describe volumes)(Citation: GCP gcloud compute disks list)(Citation: azure az disk)

## Known Threat Groups Using This Technique
- G0114: Chimera
- G0142: Confucius
- G0126: Higaisa
- G0094: Kimsuky
- G0032: Lazarus Group
- G0040: Patchwork
- G0139: TeamTNT
- G1022: ToddyCat
- G0081: Tropic Trooper
- G1017: Volt Typhoon

## Known Software Using This Technique
- S0456: Aria-body
- S9031: AshTag
- S1087: AsyncRAT
- S0438: Attor
- S0473: Avenger
- S0520: BLINDINGCAN
- S0638: Babuk
- S0234: Bandook
- S0239: Bankshot
- S1070: Black Basta
- S1068: BlackCat
- S0564: BlackMould
- S0137: CORESHELL
- S0351: Cannon
- S0667: Chrommme
- S0488: CrackMapExec
- S0115: Crimson
- S0625: Cuba
- S0616: DEATHRANSOM
- S1111: DarkGate
- S9038: DynoWiper
- S0091: Epic
- S0181: FALLCHILL
- S0267: FELIXROOT
- S1044: FunnyDream
- S0617: HELLOKITTY
- S0376: HOPLIGHT
- S0697: HermeticWiper
- S1027: Heyoka Backdoor
- S1139: INC Ransomware
- S0259: InnaputRAT
- S0260: InvisiMole
- S0044: JHUHUGIT
- S0271: KEYMARBLE
- S0526: KGH_SPY
- S0356: KONNI
- S1075: KOPILUWAK
- S0265: Kazuar
- S0607: KillDisk
- S0680: LitePower
- S1199: LockBit 2.0
- S1202: LockBit 3.0
- S1016: MacMa
- S1060: Mafalda
- S1244: Medusa Ransomware
- S1026: Mongall
- S0353: NOKKI
- S0630: Nebulae
- S1147: Nightdoor
- S1100: Ninja
- S0340: Octopus
- S1228: PUBLOAD
- S0208: Pasam
- S0587: Penquin
- S0013: PlugX
- S0238: Proxysvc
- S1242: Qilin
- S0496: REvil
- S1150: ROADSWEEP
- S0458: Ramsay
- S0172: Reaver
- S0448: Rising Sun
- S1073: Royal
- S0253: RunningRAT
- S0446: Ryuk
- S0692: SILENTTRINITY
- S0533: SLOTHFULMEDIA
- S1049: SUGARUSH
- S1168: SampleCheck5000
- S1085: Sardonic
- S0596: ShadowPad
- S1089: SharpDisco
- S0516: SoreFang
- S0491: StrongPity
- S0663: SysUpdate
- S0586: TAINTEDSCRIBE
- S1239: TONESHELL
- S0263: TYPEFRAME
- S0678: Torisma
- S0689: WhisperGate
- S1065: Woody RAT
- S0251: Zebrocy
- S1151: ZeroCleare
- S0672: Zox
- S0471: build_downer
- S0472: down_new
- S1048: macOS.OSAMiner
- S0248: yty
