# T1529: System Shutdown/Reboot


**ATT&CK ID:** T1529  
**Domain:** Mitre Attack  
**Tactic(s):** Impact  
**Platforms:** ESXi, Linux, macOS, Network Devices, Windows  
**Reference:** https://attack.mitre.org/techniques/T1529  

## Description
Adversaries may shutdown/reboot systems to interrupt access to, or aid in the destruction of, those systems. Operating systems may contain commands to initiate a shutdown/reboot of a machine or network device. In some cases, these commands may also be used to initiate a shutdown/reboot of a remote computer or network device via [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) (e.g. <code>reload</code>).(Citation: Microsoft Shutdown Oct 2017)(Citation: alert_TA18_106A) They may also include shutdown/reboot of a virtual machine via hypervisor / cloud consoles or command line tools.

Shutting down or rebooting systems may disrupt access to computer resources for legitimate users while also impeding incident response/recovery.

Adversaries may also use Windows API functions, such as `InitializeSystemShutdownExW` or `ExitWindowsEx`, to force a system to shut down or reboot.(Citation: CrowdStrike Blog)(Citation: Unit42 Agrius 2023) Alternatively, the `NtRaiseHardError`or `ZwRaiseHardError` Windows API functions with the `ResponseOption` parameter set to `OptionShutdownSystem` may deliver a “blue screen of death” (BSOD) to a system.(Citation: SonicWall)(Citation: NtRaiseHardError)(Citation: NotMe-BSOD) In order to leverage these API functions, an adversary may need to acquire `SeShutdownPrivilege` (e.g., via [Access Token Manipulation](https://attack.mitre.org/techniques/T1134)).(Citation: Unit42 Agrius 2023)
 In some cases, the system may not be able to boot again. 

Adversaries may attempt to shutdown/reboot a system after impacting it in other ways, such as [Disk Structure Wipe](https://attack.mitre.org/techniques/T1561/002) or [Inhibit System Recovery](https://attack.mitre.org/techniques/T1490), to hasten the intended effects on system availability.(Citation: Talos Nyetya June 2017)(Citation: Talos Olympic Destroyer 2018)

## Known Threat Groups Using This Technique
- G0067: APT37
- G0082: APT38
- G0032: Lazarus Group
- G1051: Medusa Group

## Known Software Using This Technique
- S1167: AcidPour
- S1125: AcidRain
- S1133: Apostle
- S1053: AvosLocker
- S1136: BFG Agonizer
- S1070: Black Basta
- S1149: CHIMNEYSWEEP
- S9042: CanisterWorm
- S1033: DCSrv
- S1111: DarkGate
- S9038: DynoWiper
- S0697: HermeticWiper
- S0607: KillDisk
- S1160: Latrodectus
- S0372: LockerGoga
- S0582: LookBack
- S0449: Maze
- S1135: MultiLayer Wiper
- S0368: NotPetya
- S0365: Olympic Destroyer
- S1242: Qilin
- S0332: Remcos
- S0140: Shamoon
- S1178: ShrinkLocker
- S0689: WhisperGate
- S1207: XLoader
