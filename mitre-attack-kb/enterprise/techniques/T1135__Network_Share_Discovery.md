# T1135: Network Share Discovery


**ATT&CK ID:** T1135  
**Domain:** Mitre Attack  
**Tactic(s):** Discovery  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1135  

## Description
Adversaries may look for folders and drives shared on remote systems as a means of identifying sources of information to gather as a precursor for Collection and to identify potential systems of interest for Lateral Movement. Networks often contain shared network drives and folders that enable users to access file directories on various systems across a network. 

File sharing over a Windows network occurs over the SMB protocol. (Citation: Wikipedia Shared Resource) (Citation: TechNet Shared Folder) [Net](https://attack.mitre.org/software/S0039) can be used to query a remote system for available shared drives using the <code>net view \\\\remotesystem</code> command. It can also be used to query shared drives on the local system using <code>net share</code>. For macOS, the <code>sharing -l</code> command lists all shared points used for smb services.

## Mitigations
- M1028: Operating System Configuration

## Known Threat Groups Using This Technique
- G0006: APT1
- G0050: APT32
- G0082: APT38
- G0087: APT39
- G0096: APT41
- G1043: BlackByte
- G0114: Chimera
- G0105: DarkVishnya
- G0035: Dragonfly
- G1016: FIN13
- G1032: INC Ransom
- G1051: Medusa Group
- G0054: Sowbug
- G0131: Tonto Team
- G0081: Tropic Trooper
- G0102: Wizard Spider

## Known Software Using This Technique
- S1129: Akira
- S0640: Avaddon
- S1053: AvosLocker
- S1081: BADHATCH
- S0638: Babuk
- S0606: Bad Rabbit
- S0534: Bazar
- S0570: BitPaymer
- S1181: BlackByte 2.0 Ransomware
- S1180: BlackByte Ransomware
- S1068: BlackCat
- S0660: Clambling
- S0611: Clop
- S0154: Cobalt Strike
- S0575: Conti
- S0488: CrackMapExec
- S0625: Cuba
- S0616: DEATHRANSOM
- S1159: DUSTTRAP
- S0659: Diavol
- S1247: Embargo
- S0367: Emotet
- S0363: Empire
- S0618: FIVEHANDS
- S0696: Flagpro
- S0617: HELLOKITTY
- S1139: INC Ransomware
- S0483: IcedID
- S0260: InvisiMole
- S1075: KOPILUWAK
- S0250: Koadic
- S0236: Kwampirs
- S1160: Latrodectus
- S1199: LockBit 2.0
- S1202: LockBit 3.0
- S1141: LunarWeb
- S0233: MURKYTOP
- S1244: Medusa Ransomware
- S0039: Net
- S0165: OSInfo
- S0365: Olympic Destroyer
- S0013: PlugX
- S0192: Pupy
- S0650: QakBot
- S1242: Qilin
- S0686: QuietSieve
- S0458: Ramsay
- S1212: RansomHub
- S1073: Royal
- S0692: SILENTTRINITY
- S1085: Sardonic
- S0444: ShimRat
- S0603: Stuxnet
- S0266: TrickBot
- S0612: WastedLocker
- S0689: WhisperGate
- S0251: Zebrocy
