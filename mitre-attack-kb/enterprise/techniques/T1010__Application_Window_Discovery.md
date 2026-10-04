# T1010: Application Window Discovery


**ATT&CK ID:** T1010  
**Domain:** Mitre Attack  
**Tactic(s):** Discovery  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1010  

## Description
Adversaries may attempt to get a listing of open application windows. Window listings could convey information about how the system is used.(Citation: Prevailion DarkWatchman 2021) For example, information about application windows could be used identify potential data to collect as well as identifying security tooling ([Security Software Discovery](https://attack.mitre.org/techniques/T1518/001)) to evade.(Citation: ESET Grandoreiro April 2020)

Adversaries typically abuse system features for this type of enumeration. For example, they may gather information through native system features such as [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059) commands and [Native API](https://attack.mitre.org/techniques/T1106) functions.

## Known Threat Groups Using This Technique
- G1001: HEXANE
- G0032: Lazarus Group
- G1017: Volt Typhoon

## Known Software Using This Technique
- S0456: Aria-body
- S0438: Attor
- S0454: Cadelspy
- S0261: Catchamas
- S1159: DUSTTRAP
- S1111: DarkGate
- S0673: DarkWatchman
- S0038: Duqu
- S0696: Flagpro
- S1044: FunnyDream
- S0531: Grandoreiro
- S0431: HotCroissant
- S0260: InvisiMole
- S0265: Kazuar
- S0409: Machete
- S0455: Metamorfo
- S0198: NETWIRE
- S0033: NetTraveler
- S1090: NightClub
- S1233: PAKLOG
- S0435: PLEAD
- S0012: PoisonIvy
- S0139: PowerDuke
- S0650: QakBot
- S0262: QuasarRAT
- S0240: ROKRAT
- S0332: Remcos
- S0375: Remexi
- S0692: SILENTTRINITY
- S0157: SOUNDBITE
- S1239: TONESHELL
- S0094: Trojan.Karagany
- S0219: WINERACK
- S0385: njRAT
