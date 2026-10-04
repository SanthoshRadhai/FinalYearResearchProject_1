# T1115: Clipboard Data


**ATT&CK ID:** T1115  
**Domain:** Mitre Attack  
**Tactic(s):** Collection  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1115  

## Description
Adversaries may collect data stored in the clipboard from users copying information within or between applications. 

For example, on Windows adversaries can access clipboard data by using <code>clip.exe</code> or <code>Get-Clipboard</code>.(Citation: MSDN Clipboard)(Citation: clip_win_server)(Citation: CISA_AA21_200B) Additionally, adversaries may monitor then replace users’ clipboard with their data (e.g., [Transmitted Data Manipulation](https://attack.mitre.org/techniques/T1565/002)).(Citation: mining_ruby_reversinglabs)

macOS and Linux also have commands, such as <code>pbpaste</code>, to grab clipboard contents.(Citation: Operating with EmPyre)

## Known Threat Groups Using This Technique
- G0082: APT38
- G0087: APT39
- G0094: Kimsuky
- G0049: OilRig

## Known Software Using This Technique
- S0331: Agent Tesla
- S0373: Astaroth
- S0438: Attor
- S1226: BOOKWORM
- S1149: CHIMNEYSWEEP
- S0454: Cadelspy
- S0261: Catchamas
- S0660: Clambling
- S0050: CosmicDuke
- S0334: DarkComet
- S1111: DarkGate
- S1066: DarkTortilla
- S0363: Empire
- S0569: Explosive
- S0381: FlawedAmmyy
- S0531: Grandoreiro
- S0170: Helminth
- S1245: InvisibleFerret
- S0044: JHUHUGIT
- S0356: KONNI
- S0250: Koadic
- S0282: MacSpy
- S0409: Machete
- S0652: MarkiRAT
- S0530: Melcoz
- S0455: Metamorfo
- S1146: MgBot
- S1122: Mispadu
- S1233: PAKLOG
- S0240: ROKRAT
- S0148: RTM
- S0332: Remcos
- S0375: Remexi
- S0253: RunningRAT
- S0692: SILENTTRINITY
- S0467: TajMahal
- S0004: TinyZBot
- S0257: VERMIN
- S1207: XLoader
- S0330: Zeus Panda
- S0283: jRAT
