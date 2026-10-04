# T1620: Reflective Code Loading


**ATT&CK ID:** T1620  
**Domain:** Mitre Attack  
**Tactic(s):** Stealth  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1620  

## Description
Adversaries may reflectively load code into a process in order to conceal the execution of malicious payloads. Reflective loading involves allocating then executing payloads directly within the memory of the process, vice creating a thread or process backed by a file path on disk (e.g., [Shared Modules](https://attack.mitre.org/techniques/T1129)).

Reflectively loaded payloads may be compiled binaries, anonymous files (only present in RAM), or just snubs of fileless executable code (ex: position-independent shellcode).(Citation: Introducing Donut)(Citation: S1 Custom Shellcode Tool)(Citation: Stuart ELF Memory)(Citation: 00sec Droppers)(Citation: Mandiant BYOL) For example, the `Assembly.Load()` method executed by [PowerShell](https://attack.mitre.org/techniques/T1059/001) may be abused to load raw code into the running process.(Citation: Microsoft AssemblyLoad)

Reflective code injection is very similar to [Process Injection](https://attack.mitre.org/techniques/T1055) except that the “injection” loads code into the processes’ own memory instead of that of a separate process. Reflective loading may evade process-based detections since the execution of the arbitrary code may be masked within a legitimate or otherwise benign process. Reflectively loading payloads directly into memory may also avoid creating files or other artifacts on disk, while also enabling malware to keep these payloads encrypted (or otherwise obfuscated) until execution.(Citation: Stuart ELF Memory)(Citation: 00sec Droppers)(Citation: Intezer ACBackdoor)(Citation: S1 Old Rat New Tricks)

## Known Threat Groups Using This Technique
- G0046: FIN7
- G0047: Gamaredon Group
- G0094: Kimsuky
- G0032: Lazarus Group

## Known Software Using This Technique
- S1081: BADHATCH
- S9011: BRUSHFIRE
- S1063: Brute Ratel C4
- S0154: Cobalt Strike
- S0625: Cuba
- S0695: Donut
- S0367: Emotet
- S0661: FoggyWeb
- S9033: Fooder
- S0666: Gelsemium
- S1022: IceApple
- S0681: Lizar
- S0447: Lokibot
- S1213: Lumma Stealer
- S1143: LunarLoader
- S9032: MuddyViper
- S1145: Pikabot
- S0013: PlugX
- S0194: PowerSploit
- S0692: SILENTTRINITY
- S1085: Sardonic
- S9001: SystemBC
- S0595: ThiefQuest
- S0022: Uroburos
- S0689: WhisperGate
- S1059: metaMain
