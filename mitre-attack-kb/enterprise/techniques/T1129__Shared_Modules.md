# T1129: Shared Modules


**ATT&CK ID:** T1129  
**Domain:** Mitre Attack  
**Tactic(s):** Execution  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1129  

## Description
Adversaries may execute malicious payloads via loading shared modules. Shared modules are executable files that are loaded into processes to provide access to reusable code, such as specific custom functions or invoking OS API functions (i.e., [Native API](https://attack.mitre.org/techniques/T1106)).

Adversaries may use this functionality as a way to execute arbitrary payloads on a victim system. For example, adversaries can modularize functionality of their malware into shared objects that perform various functions such as managing C2 network communications or execution of specific actions on objective.

The Linux & macOS module loader can load and execute shared objects from arbitrary local paths. This functionality resides in `dlfcn.h` in functions such as `dlopen` and `dlsym`. Although macOS can execute `.so` files, common practice uses `.dylib` files.(Citation: Apple Dev Dynamic Libraries)(Citation: Linux Shared Libraries)(Citation: RotaJakiro 2021 netlab360 analysis)(Citation: Unit42 OceanLotus 2017)

The Windows module loader can be instructed to load DLLs from arbitrary local paths and arbitrary Universal Naming Convention (UNC) network paths. This functionality resides in `NTDLL.dll` and is part of the Windows [Native API](https://attack.mitre.org/techniques/T1106) which is called from functions like `LoadLibrary` at run time.(Citation: Microsoft DLL)

## Mitigations
- M1038: Execution Prevention

## Known Threat Groups Using This Technique
- G0129: Mustang Panda

## Known Software Using This Technique
- S0373: Astaroth
- S0438: Attor
- S0520: BLINDINGCAN
- S0415: BOOSTWRITE
- S1039: Bumblebee
- S0673: DarkWatchman
- S0567: Dtrack
- S0377: Ebury
- S0661: FoggyWeb
- S0203: Hydraq
- S0607: KillDisk
- S1185: LightSpy
- S0455: Metamorfo
- S0352: OSX_OCEANLOTUS.D
- S0196: PUNCHBUGGY
- S0501: PipeMon
- S1078: RotaJakiro
- S0603: Stuxnet
- S0467: TajMahal
- S1154: VersaMem
- S0032: gh0st RAT
