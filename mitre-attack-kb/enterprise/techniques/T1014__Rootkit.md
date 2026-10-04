# T1014: Rootkit


**ATT&CK ID:** T1014  
**Domain:** Mitre Attack  
**Tactic(s):** Stealth  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1014  

## Description
Adversaries may use rootkits to hide the presence of programs, files, network connections, services, drivers, and other system components. Rootkits are programs that hide the existence of malware by intercepting/hooking and modifying operating system API calls that supply system information. (Citation: Symantec Windows Rootkits) 

Rootkits or rootkit enabling functionality may reside at the user or kernel level in the operating system or lower, to include a hypervisor or [System Firmware](https://attack.mitre.org/techniques/T1542/001). (Citation: Wikipedia Rootkit) Rootkits have been seen for Windows, Linux, and Mac OS X systems. (Citation: CrowdStrike Linux Rootkit) (Citation: BlackHat Mac OSX Rootkit)

Rootkits that reside or modify boot sectors are known as [Bootkit](https://attack.mitre.org/techniques/T1542/003)s and specifically target the boot process of the operating system.

## Known Threat Groups Using This Technique
- G0007: APT28
- G0096: APT41
- G0106: Rocke
- G0139: TeamTNT
- G1048: UNC3886
- G0044: Winnti Group

## Known Software Using This Technique
- S1105: COATHANGER
- S0484: Carberp
- S0572: Caterpillar WebShell
- S0502: Drovorub
- S0377: Ebury
- S0135: HIDEDRV
- S0040: HTRAN
- S0047: Hacking Team UEFI Rootkit
- S0394: HiddenWasp
- S0009: Hikit
- S0601: Hildegard
- S1186: Line Dancer
- S0397: LoJax
- S1220: MEDUSA
- S0012: PoisonIvy
- S1219: REPTILE
- S0458: Ramsay
- S0468: Skidmap
- S0603: Stuxnet
- S0221: Umbreon
- S0022: Uroburos
- S0670: WarzoneRAT
- S0430: Winnti for Linux
- S0027: Zeroaccess
