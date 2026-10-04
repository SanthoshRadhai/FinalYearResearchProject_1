# T1485: Data Destruction


**ATT&CK ID:** T1485  
**Domain:** Mitre Attack  
**Tactic(s):** Impact  
**Platforms:** Containers, ESXi, IaaS, Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1485  

## Description
Adversaries may destroy data and files on specific systems or in large numbers on a network to interrupt availability to systems, services, and network resources. Data destruction is likely to render stored data irrecoverable by forensic techniques through overwriting files or data on local and remote drives.(Citation: Symantec Shamoon 2012)(Citation: FireEye Shamoon Nov 2016)(Citation: Palo Alto Shamoon Nov 2016)(Citation: Kaspersky StoneDrill 2017)(Citation: Unit 42 Shamoon3 2018)(Citation: Talos Olympic Destroyer 2018) Common operating system file deletion commands such as <code>del</code> and <code>rm</code> often only remove pointers to files without wiping the contents of the files themselves, making the files recoverable by proper forensic methodology. This behavior is distinct from [Disk Content Wipe](https://attack.mitre.org/techniques/T1561/001) and [Disk Structure Wipe](https://attack.mitre.org/techniques/T1561/002) because individual files are destroyed rather than sections of a storage disk or the disk's logical structure.

Adversaries may attempt to overwrite files and directories with randomly generated data to make it irrecoverable.(Citation: Kaspersky StoneDrill 2017)(Citation: Unit 42 Shamoon3 2018) In some cases politically oriented image files have been used to overwrite data.(Citation: FireEye Shamoon Nov 2016)(Citation: Palo Alto Shamoon Nov 2016)(Citation: Kaspersky StoneDrill 2017)

To maximize impact on the target organization in operations where network-wide availability interruption is the goal, malware designed for destroying data may have worm-like features to propagate across a network by leveraging additional techniques like [Valid Accounts](https://attack.mitre.org/techniques/T1078), [OS Credential Dumping](https://attack.mitre.org/techniques/T1003), and [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002).(Citation: Symantec Shamoon 2012)(Citation: FireEye Shamoon Nov 2016)(Citation: Palo Alto Shamoon Nov 2016)(Citation: Kaspersky StoneDrill 2017)(Citation: Talos Olympic Destroyer 2018).

In cloud environments, adversaries may leverage access to delete cloud storage objects, machine images, database instances, and other infrastructure crucial to operations to damage an organization or their customers.(Citation: Data Destruction - Threat Post)(Citation: DOJ  - Cisco Insider) Similarly, they may delete virtual machines from on-prem virtualized environments.

## Sub-techniques
- T1485.001: Lifecycle-Triggered Deletion

## Mitigations
- M1018: User Account Management
- M1032: Multi-factor Authentication
- M1053: Data Backup

## Known Threat Groups Using This Technique
- G0082: APT38
- G1004: LAPSUS$
- G0032: Lazarus Group
- G0034: Sandworm Team
- G1057: ShinyHunters
- G1053: Storm-0501
- G1056: TeamPCP
- G1055: VOID MANTICORE

## Known Software Using This Technique
- S1167: AcidPour
- S1125: AcidRain
- S1133: Apostle
- S0089: BlackEnergy
- S0693: CaddyWiper
- S9042: CanisterWorm
- S1134: DEADWOOD
- S0659: Diavol
- S9038: DynoWiper
- S0697: HermeticWiper
- S0604: Industroyer
- S0265: Kazuar
- S0607: KillDisk
- S9039: LazyWiper
- S0688: Meteor
- S9043: Mini Shai-Hulud
- S1135: MultiLayer Wiper
- S0365: Olympic Destroyer
- S0139: PowerDuke
- S0238: Proxysvc
- S0496: REvil
- S0364: RawDisk
- S0195: SDelete
- S9030: SameCoin
- S9008: Shai-Hulud
- S0140: Shamoon
- S1178: ShrinkLocker
- S0380: StoneDrill
- S0689: WhisperGate
- S0341: Xbash
